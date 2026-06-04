"""CLI — update data, render README, notify Discord."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import click

from pipeline.notify.discord import notify_discord
from pipeline.dashboard.markdown_generator import render_readme
from pipeline.extract.scraper import scrape_gold_prices
from pipeline.load.storage import append_snapshot, load_history


def _repo_slug() -> str:
    return os.getenv("GITHUB_REPOSITORY", "YOUR_GITHUB_USERNAME/gold-price-platform")


@click.group()
def main() -> None:
    """Vietnam gold price monitor CLI."""


@main.command()
@click.option("--data-file", default="data/silver/prices.json", type=click.Path(path_type=Path))
def update(data_file: Path) -> None:
    """Scrape latest prices and append to JSON history."""
    quotes = scrape_gold_prices()
    if not quotes:
        click.echo("No data scraped.", err=True)
        sys.exit(1)
    snap = append_snapshot(data_file, quotes)
    click.echo(f"Saved {len(quotes)} brands -> {data_file} ({snap.timestamp})")


@main.command("render-readme")
@click.option("--data-file", default="data/silver/prices.json", type=click.Path(path_type=Path))
@click.option("--out", default="README.md", type=click.Path(path_type=Path))
def render_readme_cmd(data_file: Path, out: Path) -> None:
    """Render README.md dashboard from data/gold_prices.json."""
    if not data_file.exists():
        raise click.ClickException(f"{data_file} not found — run `gold update` first")
    content = render_readme(data_file, repo=_repo_slug())
    out.write_text(content, encoding="utf-8")
    click.echo(f"wrote {out}")


@main.command("notify-discord")
@click.option("--data-file", default="data/silver/prices.json", type=click.Path(path_type=Path))
@click.option("--webhook-url", default=None, help="Override DISCORD_WEBHOOK_URL env")
@click.option("--repo-url", default=None, help="Link in Discord embed footer")
def notify_discord_cmd(data_file: Path, webhook_url: str | None, repo_url: str | None) -> None:
    """Post today's prices to Discord webhook."""
    history = load_history(data_file)
    if not history:
        raise click.ClickException("No data — run `gold update` first")
    slug = _repo_slug()
    url = repo_url or f"https://github.com/{slug}"
    sent = notify_discord(history[-1], history, webhook_url=webhook_url, repo_url=url)
    if not sent:
        click.echo("DISCORD_WEBHOOK_URL not set — skipped.", err=True)
        sys.exit(0)
    click.echo("Discord notification sent.")


if __name__ == "__main__":
    main()
