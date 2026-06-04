# 📈 Gold Price Data Pipeline

An enterprise-grade Data Engineering & Analytics Engineering pipeline built to automatically ingest, transform, and alert on Vietnam's domestic gold prices using the Medallion Architecture.

![daily-update](https://github.com/kina2711/gold-price-platform/actions/workflows/daily-update.yml/badge.svg) ![snapshots](https://img.shields.io/static/v1?label=snapshots&message=7&color=blue) ![license](https://img.shields.io/static/v1?label=license&message=MIT&color=yellow) ![architecture](https://img.shields.io/static/v1?label=architecture&message=Medallion+%28ELT%29&color=purple)

> **Latest Pipeline Run:** 2026-06-04 16:42:34 (ICT) 
> **Key Metric (SJC):** Buy **153.000.000** VND — Sell **156.000.000** VND

## 🏗 System Architecture (ELT)

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
- **Gold (In-Memory/UI)**: Business-level aggregations (trends, spread calculations, day-over-day changes).

## 🎯 Gold Layer: Executive Metrics (2026-06-04)

| Metric | Value (VND/lượng) |
|---|---|
| Ask (Buy) | **153.000.000** |
| Bid (Sell) | **156.000.000** |
| Spread | 3.000.000 |

## 🏷 Market Overview by Brand

| Brand | Ask (VND) | Bid (VND) | Spread |
|---|---:|---:|---:|
| BTMC SJC | 153.000.000 | 156.000.000 | 3.000.000 |
| BTMH | 153.000.000 | 156.000.000 | 3.000.000 |
| DOJI HN | 153.000.000 | 156.000.000 | 3.000.000 |
| DOJI SG | 153.000.000 | 156.000.000 | 3.000.000 |
| PNJ Hà Nội | 153.000.000 | 156.000.000 | 3.000.000 |
| PNJ TP.HCM | 153.000.000 | 156.000.000 | 3.000.000 |
| Phú Qúy SJC | 153.000.000 | 156.000.000 | 3.000.000 |
| SJC | 153.000.000 | 156.000.000 | 3.000.000 |


## 📅 Historical Trend (10 Days)

**7-Day Sparkline:** Ask ` ` · Bid ` `

| Date | Ask | Bid | Spread |
|---|---:|---:|---:|
| 04/06/2026 | 153.000.000 | 156.000.000 | 3.000.000 |




## 🚀 Data Engineering Roadmap

- [x] **Phase 1:** Build local ELT Pipeline using Python & GitHub Actions.
- [x] **Phase 2:** Implement Medallion Architecture (Bronze/Silver/Gold).
- [ ] **Phase 3:** Cloud Integration (Google Cloud Storage + BigQuery).
- [ ] **Phase 4:** Analytics Engineering (Migrate transforms to `dbt`).
- [ ] **Phase 5:** Orchestration (Migrate from GitHub Actions to Apache Airflow or Prefect).

---

_Pipeline triggered at **2026-06-04 16:42 +07** via [GitHub Actions](.github/workflows/daily-update.yml)._  
_Data Lineage: [`data/silver/prices.json`](data/silver/prices.json) · 7 historical snapshots (2026-06-04 → 2026-06-04)._  
_Setup & Configurations: [`docs/USAGE.md`](docs/USAGE.md). License: [MIT](LICENSE)._
