"""Scrape gold prices from 24h.com.vn (adapted from gold-price-monitoring)."""

from __future__ import annotations

import re
from dataclasses import dataclass

import requests
from bs4 import BeautifulSoup

SOURCE_URL = "https://www.24h.com.vn/gia-vang-hom-nay-c425.html"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)


@dataclass(frozen=True)
class GoldQuote:
    brand: str
    buy: int
    sell: int

    @property
    def spread(self) -> int:
        return self.sell - self.buy


def sanitize_price(price_str: str) -> int:
    """Parse VND price from 24h.com.vn (supports full and abbreviated formats)."""
    digits = re.sub(r"\D", "", price_str)
    if not digits:
        return 0
    value = int(digits)
    # Site often shows "153,500" meaning 153,500,000 VND (thousands unit)
    if value < 1_000_000:
        value *= 1000
    return value


def parse_html(html: str) -> list[GoldQuote]:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", class_="gia-vang-search-data-table")
    if not table:
        return []

    quotes: list[GoldQuote] = []
    for row in table.find_all("tr"):
        cols = row.find_all("td")
        if len(cols) < 3:
            continue

        brand_node = cols[0].find("h2")
        brand = brand_node.get_text(strip=True) if brand_node else cols[0].get_text(strip=True)

        buy_node = cols[1].find("span", class_="fixW")
        sell_node = cols[2].find("span", class_="fixW")
        buy_raw = buy_node.get_text(strip=True) if buy_node else cols[1].get_text(strip=True)
        sell_raw = sell_node.get_text(strip=True) if sell_node else cols[2].get_text(strip=True)

        buy = sanitize_price(buy_raw)
        sell = sanitize_price(sell_raw)
        if brand and (buy > 0 or sell > 0):
            quotes.append(GoldQuote(brand=brand, buy=buy, sell=sell))
    return quotes


def scrape_gold_prices(url: str = SOURCE_URL, timeout: float = 30.0) -> list[GoldQuote]:
    response = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
    response.raise_for_status()
    return parse_html(response.text)
