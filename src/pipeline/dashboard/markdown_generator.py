"""Render README.md dashboard from pipeline price history."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from urllib.parse import quote_plus
from zoneinfo import ZoneInfo

from pipeline.transform.metrics import (
    day_over_day,
    find_brand,
    format_vnd,
    latest_snapshot,
    recent_days,
    sjc_history_table,
    sparkline,
)
from pipeline.load.storage import load_history

_ICT = ZoneInfo("Asia/Ho_Chi_Minh")
_REPO = "YOUR_GITHUB_USERNAME/gold-price-platform"  # overridden at render time


def _shield(label: str, message: str, color: str) -> str:
    return (
        "https://img.shields.io/static/v1"
        f"?label={quote_plus(label)}&message={quote_plus(message)}&color={color}"
    )


def _delta_cell(delta: int | None, pct: float | None) -> str:
    if delta is None:
        return "—"
    sign = "+" if delta > 0 else ""
    pct_str = f" ({sign}{pct:.2f}%)" if pct is not None else ""
    emoji = "📈" if delta > 0 else ("📉" if delta < 0 else "➡️")
    return f"{emoji} {sign}{format_vnd(delta)}{pct_str}"


def render_readme(data_path: Path, repo: str = _REPO) -> str:
    history = load_history(data_path)
    if not history:
        return "# 📈 Gold Price Data Pipeline\n\n*No data available — run `pipeline update`.*\n"

    latest = latest_snapshot(history)
    assert latest is not None
    dod = day_over_day(history)
    sjc = find_brand(latest.entries, "SJC")

    sections = [
        _header(history, latest, sjc, repo),
        _section_architecture(),
        _section_today(latest),
        _section_brands(latest),
        _section_sjc_trend(history),
        _section_day_change(dod),
        _section_roadmap(),
        _footer(history, repo),
    ]
    return "\n\n".join(sections) + "\n"


def _header(history, latest, sjc, repo: str) -> str:
    now = datetime.now(_ICT)
    sjc_buy = format_vnd(sjc["buy"]) if sjc else "N/A"
    sjc_sell = format_vnd(sjc["sell"]) if sjc else "N/A"
    badges = [
        f"![daily-update](https://github.com/{repo}/actions/workflows/daily-update.yml/badge.svg)",
        f"![snapshots]({_shield('snapshots', f'{len(history):,}', 'blue')})",
        f"![license]({_shield('license', 'MIT', 'yellow')})",
        f"![architecture]({_shield('architecture', 'Medallion (ELT)', 'purple')})",
    ]
    return (
        "# 📈 Gold Price Data Pipeline\n\n"
        "An enterprise-grade Data Engineering & Analytics Engineering pipeline built to automatically ingest, transform, and alert on Vietnam's domestic gold prices using the Medallion Architecture.\n\n"
        + " ".join(badges)
        + f"\n\n> **Latest Pipeline Run:** {latest.date} {latest.timestamp.split(' ', 1)[-1]} (ICT) \n"
        f"> **Key Metric (SJC):** Buy **{sjc_buy}** VND — Sell **{sjc_sell}** VND"
    )

def _section_architecture() -> str:
    return """## 🏗 System Architecture (ELT)

We employ a robust ELT approach coupled with the **Medallion Data Architecture**:

```mermaid
graph LR
    A[External Source API] -->|Extract| B(Bronze Layer)
    B -->|Transform & Clean| C(Silver Layer)
    C -->|Aggregations| D(Gold Layer / Metrics)
    D -->|Notify| E[Discord Webhook Alert]
    D -->|Dashboard| F[README.md UI]
    
    style B fill:#CD7F32,stroke:#333,stroke-width:2px
    style C fill:#C0C0C0,stroke:#333,stroke-width:2px
    style D fill:#FFD700,stroke:#333,stroke-width:2px
```

- **Bronze (`data/bronze/`)**: Raw immutable JSON snapshots appended continuously.
- **Silver (`data/silver/`)**: Cleaned, deduplicated, and normalized historical tabular data.
- **Gold (In-Memory/UI)**: Business-level aggregations (trends, spread calculations, day-over-day changes)."""

def _section_today(latest) -> str:
    sjc = find_brand(latest.entries, "SJC")
    if not sjc:
        return "## 🎯 Gold Layer: Today's Executive Metrics\n\n*No SJC data found.*"
    return (
        f"## 🎯 Gold Layer: Executive Metrics ({latest.date})\n\n"
        "| Metric | Value (VND/lượng) |\n|---|---|\n"
        f"| Ask (Buy) | **{format_vnd(sjc['buy'])}** |\n"
        f"| Bid (Sell) | **{format_vnd(sjc['sell'])}** |\n"
        f"| Spread | {format_vnd(sjc['sell'] - sjc['buy'])} |"
    )

def _section_brands(latest) -> str:
    lines = [
        "## 🏷 Market Overview by Brand\n\n",
        "| Brand | Ask (VND) | Bid (VND) | Spread |\n",
        "|---|---:|---:|---:|\n",
    ]
    for e in sorted(latest.entries, key=lambda x: x["brand"]):
        lines.append(
            f"| {e['brand']} | {format_vnd(e['buy'])} | {format_vnd(e['sell'])} "
            f"| {format_vnd(e['sell'] - e['buy'])} |\n"
        )
    return "".join(lines)


def _section_sjc_trend(history) -> str:
    rows = sjc_history_table(history, n=10)
    if not rows:
        return ""
    
    sorted_rows = sorted(rows, key=lambda x: x[0])
    buy_trend = sparkline([r[1] for r in sorted_rows])
    sell_trend = sparkline([r[2] for r in sorted_rows])

    lines = [
        "## 📅 Historical Trend (10 Days)\n\n",
        f"**7-Day Sparkline:** Ask `{buy_trend}` · Bid `{sell_trend}`\n\n",
        "| Date | Ask | Bid | Spread |\n",
        "|---|---:|---:|---:|\n",
    ]
    for d, buy, sell, spread in rows:
        lines.append(
            f"| {d:%d/%m/%Y} | {format_vnd(buy)} | {format_vnd(sell)} | {format_vnd(spread)} |\n"
        )
    return "".join(lines)


def _section_day_change(dod) -> str:
    if not dod:
        return ""
    return (
        "## 📊 Day-Over-Day (DoD) Volatility\n\n"
        "| Indicator | Delta (VND) |\n|---|---|\n"
        f"| Ask Price | {_delta_cell(dod.buy_delta, dod.buy_pct)} |\n"
        f"| Bid Price | {_delta_cell(dod.sell_delta, dod.sell_pct)} |"
    )

def _section_roadmap() -> str:
    return """## 🚀 Data Engineering Roadmap

- [x] **Phase 1:** Build local ELT Pipeline using Python & GitHub Actions.
- [x] **Phase 2:** Implement Medallion Architecture (Bronze/Silver/Gold).
- [x] **Phase 3:** Cloud Integration (Google Cloud Storage + BigQuery).
- [x] **Phase 4:** Analytics Engineering (Migrate transforms to `dbt`).
- [x] **Phase 5:** Orchestration (Migrate from GitHub Actions to Apache Airflow or Prefect)."""

def _footer(history, repo: str) -> str:
    now = datetime.now(_ICT)
    first = history[0].date
    last = history[-1].date
    return (
        "---\n\n"
        f"_Pipeline triggered at **{now:%Y-%m-%d %H:%M %Z}** via "
        f"[GitHub Actions](.github/workflows/daily-update.yml)._  \n"
        f"_Data Lineage: [`data/silver/prices.json`](data/silver/prices.json) · "
        f"{len(history):,} historical snapshots ({first} → {last})._  \n"
        "_Setup & Configurations: [`docs/USAGE.md`](docs/USAGE.md). License: [MIT](LICENSE)._"
    )
