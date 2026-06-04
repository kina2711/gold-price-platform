"""Send daily gold price summary to Discord via webhook."""

from __future__ import annotations

import os
from datetime import datetime
from zoneinfo import ZoneInfo

import httpx

from pipeline.transform.metrics import day_over_day, find_brand, format_vnd, sjc_history_table, sparkline
from pipeline.load.storage import Snapshot

_ICT = ZoneInfo("Asia/Ho_Chi_Minh")
DISCORD_EMBED_COLOR = 0xFFD700  # gold


def _delta_line(label: str, delta: int | None, pct: float | None) -> str:
    if delta is None:
        return f"**{label}:** —"
    sign = "+" if delta > 0 else ""
    pct_str = f" ({sign}{pct:.2f}%)" if pct is not None else ""
    return f"**{label}:** {sign}{format_vnd(delta)}{pct_str} VND"


def build_discord_payload(snapshot: Snapshot, history: list[Snapshot], repo_url: str) -> dict:
    sjc = find_brand(snapshot.entries, "SJC")
    dod = day_over_day(history)
    now = datetime.now(_ICT)

    if sjc:
        title = f"Giá vàng VN — {snapshot.date}"
        description = (
            f"**{sjc['brand']}** · Mua **{format_vnd(sjc['buy'])}** · "
            f"Bán **{format_vnd(sjc['sell'])}** VND/lượng"
        )
        fields = [
            {
                "name": "Spread SJC",
                "value": f"{format_vnd(sjc['sell'] - sjc['buy'])} VND",
                "inline": True,
            },
            {
                "name": "Thương hiệu",
                "value": str(len(snapshot.entries)),
                "inline": True,
            },
        ]
        if dod:
            fields.append(
                {
                    "name": "So với hôm qua",
                    "value": "\n".join(
                        [
                            _delta_line("Mua", dod.buy_delta, dod.buy_pct),
                            _delta_line("Bán", dod.sell_delta, dod.sell_pct),
                        ]
                    ),
                    "inline": False,
                }
            )
            
        # Add sparkline to Discord
        rows = sjc_history_table(history, n=7) # last 7 days
        if len(rows) >= 2:
            sorted_rows = sorted(rows, key=lambda x: x[0])
            buy_trend = sparkline([r[1] for r in sorted_rows])
            sell_trend = sparkline([r[2] for r in sorted_rows])
            fields.append(
                {
                    "name": "Biểu đồ 7 ngày (SJC)",
                    "value": f"Mua: `{buy_trend}`\nBán: `{sell_trend}`",
                    "inline": False,
                }
            )
    else:
        title = f"Giá vàng VN — {snapshot.date}"
        description = f"Cập nhật {len(snapshot.entries)} thương hiệu."

    top_brands = sorted(snapshot.entries, key=lambda e: e["brand"])[:5]
    brand_lines = "\n".join(
        f"• **{e['brand']}:** {format_vnd(e['buy'])} / {format_vnd(e['sell'])}"
        for e in top_brands
    )
    fields.append({"name": "Top thương hiệu", "value": brand_lines, "inline": False})

    return {
        "username": "Gold Price Bot",
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": DISCORD_EMBED_COLOR,
                "fields": fields,
                "footer": {"text": f"Cập nhật lúc {now:%H:%M} ICT · gold-price-platform"},
                "url": repo_url,
            }
        ],
    }


def notify_discord(
    snapshot: Snapshot,
    history: list[Snapshot],
    webhook_url: str | None = None,
    repo_url: str = "https://github.com/YOUR_GITHUB_USERNAME/gold-price-platform",
) -> bool:
    url = webhook_url or os.getenv("DISCORD_WEBHOOK_URL")
    if not url:
        return False

    payload = build_discord_payload(snapshot, history, repo_url)
    response = httpx.post(url, json=payload, timeout=30.0)
    response.raise_for_status()
    return True
