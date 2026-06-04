"""Analytics helpers for README dashboard."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from pipeline.load.storage import Snapshot, parse_snapshot_date


@dataclass
class BrandDay:
    date: date
    brand: str
    buy: int
    sell: int
    spread: int


@dataclass
class DayChange:
    brand: str
    buy_delta: int | None
    sell_delta: int | None
    buy_pct: float | None
    sell_pct: float | None


def daily_latest(history: list[Snapshot]) -> dict[date, Snapshot]:
    """Last snapshot per calendar day."""
    by_day: dict[date, Snapshot] = {}
    for snap in history:
        by_day[parse_snapshot_date(snap)] = snap
    return by_day


def latest_snapshot(history: list[Snapshot]) -> Snapshot | None:
    return history[-1] if history else None


def recent_days(history: list[Snapshot], n: int = 10) -> list[Snapshot]:
    by_day = daily_latest(history)
    days = sorted(by_day.keys(), reverse=True)[:n]
    return [by_day[d] for d in sorted(days)]


def find_brand(entries: list[dict], brand_substr: str) -> dict | None:
    needle = brand_substr.lower()
    for e in entries:
        if needle in e["brand"].lower():
            return e
    return entries[0] if entries else None


def format_vnd(amount: int) -> str:
    return f"{amount:,}".replace(",", ".")


def day_over_day(history: list[Snapshot], brand_substr: str = "SJC") -> DayChange | None:
    by_day = daily_latest(history)
    days = sorted(by_day.keys())
    if len(days) < 2:
        return None

    today_snap = by_day[days[-1]]
    prev_snap = by_day[days[-2]]
    cur = find_brand(today_snap.entries, brand_substr)
    prev = find_brand(prev_snap.entries, brand_substr)
    if not cur or not prev:
        return None

    buy_delta = cur["buy"] - prev["buy"]
    sell_delta = cur["sell"] - prev["sell"]
    buy_pct = (buy_delta / prev["buy"] * 100) if prev["buy"] else None
    sell_pct = (sell_delta / prev["sell"] * 100) if prev["sell"] else None
    return DayChange(
        brand=cur["brand"],
        buy_delta=buy_delta,
        sell_delta=sell_delta,
        buy_pct=buy_pct,
        sell_pct=sell_pct,
    )


def brand_table(entries: list[dict]) -> list[BrandDay]:
    d = date.today()
    rows: list[BrandDay] = []
    for e in sorted(entries, key=lambda x: x["brand"]):
        rows.append(
            BrandDay(
                date=d,
                brand=e["brand"],
                buy=e["buy"],
                sell=e["sell"],
                spread=e["sell"] - e["buy"],
            )
        )
    return rows


def sjc_history_table(history: list[Snapshot], n: int = 10) -> list[tuple[date, int, int, int]]:
    rows: list[tuple[date, int, int, int]] = []
    for snap in recent_days(history, n):
        sjc = find_brand(snap.entries, "SJC")
        if sjc:
            rows.append((parse_snapshot_date(snap), sjc["buy"], sjc["sell"], sjc["sell"] - sjc["buy"]))
    return rows


def sparkline(data: list[float]) -> str:
    """Generate a sparkline string from a list of numbers."""
    if not data:
        return ""
    bars = " ▂▃▄▅▆▇█"
    d_min = min(data)
    d_max = max(data)
    range_val = d_max - d_min
    if range_val == 0:
        return bars[0] * len(data)
    return "".join(bars[int((val - d_min) / range_val * 7)] for val in data)
