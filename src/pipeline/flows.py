"""Orchestration with Prefect."""

import subprocess
from pathlib import Path

from prefect import flow, task

@task(retries=2, retry_delay_seconds=10)
def extract_and_load_task():
    from pipeline.extract.scraper import scrape_gold_prices
    from pipeline.load.storage import append_snapshot
    data_file = Path("data/silver/prices.json")
    quotes = scrape_gold_prices()
    if quotes:
        append_snapshot(data_file, quotes)
        return True
    return False

@task
def run_dbt_models_task():
    # Run dbt using subprocess since it's a CLI tool
    # Need to run `dbt deps` first if packages exist, but we have none for now.
    subprocess.run(["uv", "run", "dbt", "run", "--project-dir", "dbt", "--profiles-dir", "dbt"], check=True)

@task
def render_readme_task():
    from pipeline.dashboard.markdown_generator import render_readme
    import os
    data_file = Path("data/silver/prices.json")
    out = Path("README.md")
    if data_file.exists():
        repo = os.getenv("GITHUB_REPOSITORY", "Vmt/gold-price-platform")
        content = render_readme(data_file, repo=repo)
        out.write_text(content, encoding="utf-8")

@task
def notify_discord_task():
    from pipeline.load.storage import load_history
    from pipeline.notify.discord import notify_discord
    import os
    data_file = Path("data/silver/prices.json")
    history = load_history(data_file)
    if history:
        slug = os.getenv("GITHUB_REPOSITORY", "Vmt/gold-price-platform")
        url = f"https://github.com/{slug}"
        notify_discord(history[-1], history, webhook_url=None, repo_url=url)

@flow(name="gold-price-daily-pipeline")
def daily_pipeline():
    # 1. Extract & Load to GCS/BigQuery
    extract_and_load_task()
    
    # 2. Analytics Engineering (dbt transformations)
    run_dbt_models_task()
    
    # 3. Dashboard update (Markdown README)
    render_readme_task()
    
    # 4. Notifications (Discord)
    notify_discord_task()

if __name__ == "__main__":
    daily_pipeline()
