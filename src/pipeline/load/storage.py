"""Persist gold price snapshots as JSON history."""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

from pipeline.extract.scraper import GoldQuote

_ICT = ZoneInfo("Asia/Ho_Chi_Minh")
MAX_SNAPSHOTS = 730  # ~2 years of daily snapshots


@dataclass
class Snapshot:
    timestamp: str
    date: str
    entries: list[dict]

    @classmethod
    def from_quotes(cls, quotes: list[GoldQuote], when: datetime | None = None) -> Snapshot:
        now = when or datetime.now(_ICT)
        return cls(
            timestamp=now.strftime("%Y-%m-%d %H:%M:%S"),
            date=now.strftime("%Y-%m-%d"),
            entries=[asdict(q) for q in quotes],
        )


def load_history(path: Path) -> list[Snapshot]:
    if not path.exists():
        return []
    raw = json.loads(path.read_text(encoding="utf-8"))
    return [Snapshot(**item) for item in raw]


def save_history(path: Path, history: list[Snapshot]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    trimmed = history[-MAX_SNAPSHOTS:]
    path.write_text(
        json.dumps([s.__dict__ for s in trimmed], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def append_snapshot(path: Path, quotes: list[GoldQuote], when: datetime | None = None) -> Snapshot:
    now = when or datetime.now(_ICT)
    history = load_history(path)
    snap = Snapshot.from_quotes(quotes, now)
    history.append(snap)
    save_history(path, history)
    
    # Medallion Architecture: Save to Bronze (Raw)
    bronze_dir = Path("data/bronze") / now.strftime("%Y/%m/%d")
    bronze_dir.mkdir(parents=True, exist_ok=True)
    bronze_file = bronze_dir / f"raw_{now.strftime('%H%M%S')}.json"
    bronze_file.write_text(json.dumps(snap.__dict__, ensure_ascii=False, indent=2), encoding="utf-8")
    
    return snap


def quotes_to_dicts(quotes: list[GoldQuote]) -> list[dict]:
    return [asdict(q) for q in quotes]


def parse_snapshot_date(snap: Snapshot) -> date:
    return datetime.strptime(snap.date, "%Y-%m-%d").date()
