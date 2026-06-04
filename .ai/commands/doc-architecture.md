---
description: Tạo tài liệu Architecture — Data Architecture, System Architecture, Data Model, ETL/ELT
argument-hint: [data-arch|system-arch|data-model|etl|all]
---

Tạo document cho Architecture layer. Chọn luồng hoặc `all`.

## LUỒNG 1: Data Architecture Document

### Template
```markdown
# Data Architecture Document
**Project**: [tên]  |  **Version**: 1.0

## Architecture Overview
```
[Source Systems]
    ├── DB: PostgreSQL (OLTP)
    ├── API: REST endpoints
    ├── Files: S3 CSV/JSON
    └── Stream: Kafka topics
         ↓
[Ingestion Layer]
    ├── Batch: Airflow DAGs (daily)
    ├── Streaming: Kafka Connect
    └── CDC: Debezium
         ↓
[Raw / Landing Zone]
    └── S3 / Data Lake (Parquet)
         ↓
[Transform Layer]
    ├── dbt models
    ├── Staging → Intermediate → Marts
    └── Data Quality checks
         ↓
[Curated / Warehouse]
    └── Snowflake / BigQuery / Redshift
         ↓
[Serving Layer]
    ├── BI: Superset dashboards
    ├── API: REST/GraphQL
    ├── ML: Feature Store
    └── Reverse ETL: Census/Hightouch
```

## Data Source Inventory
| # | Source | Type | Format | Volume | Frequency | Owner | SLA | Contract |
|---|--------|------|--------|--------|-----------|-------|-----|---------|
| 1 |        | DB/API/File/Stream | JSON/CSV/Parquet | X GB/day | Real-time/Hourly/Daily | | | Y/N |

## Data Lineage Map
```
[raw.events] → [stg.events_clean] → [int.events_enriched] → [mart.fact_events]
                                                                      ↓
[raw.users] → [stg.users_clean] → [int.users_enriched] → [mart.dim_users]
                                                                      ↓
                                                            [mart.dashboard_daily]
```

## Data Ownership Matrix
| Domain | Owner Team | Steward | Tables | SLA | Escalation |
|--------|-----------|---------|--------|-----|-----------|
|        |           |         |        |     |           |

## Data Governance
| Policy | Implementation | Status |
|--------|---------------|--------|
| Access Control | RBAC + Row-level security | ✅ |
| PII Handling | Encryption + Masking | ✅ |
| Retention | 90 days raw, 3 years curated | ✅ |
| Lineage Tracking | dbt docs + custom metadata | ⚠️ |
| Data Catalog | DataHub / Amundsen | ❌ Not yet |

## Reliability Assessment
| Dimension | Current | Target | Gap | Action |
|-----------|---------|--------|-----|--------|
| Idempotency | Partial | Full | ⚠️ | Add dedup logic |
| Retry Logic | Basic | Exponential backoff | ⚠️ | Implement |
| Schema Validation | None | Contract testing | ❌ | Priority |
| Monitoring | Airflow UI only | Full observability | ⚠️ | Add DQ dashboard |
```

---

## LUỒNG 2: System Architecture Document

### Template
```markdown
# System Architecture Document
**Project**: [tên]  |  **Version**: 1.0

## Architecture Diagram
```
[Client Layer]
    ├── Web App (React/Next.js)
    └── Mobile App (React Native)
         ↓ HTTPS
[API Layer]
    ├── API Gateway (Kong/Nginx)
    ├── Load Balancer (ALB)
    └── Rate Limiting
         ↓
[Service Layer]
    ├── Auth Service (JWT/OAuth2)
    ├── User Service
    ├── Order Service
    └── Analytics Service
         ↓
[Data Layer]
    ├── Primary DB (PostgreSQL - write)
    ├── Read Replica (PostgreSQL - read)
    ├── Cache (Redis)
    ├── Search (Elasticsearch)
    └── Queue (RabbitMQ/Kafka)
         ↓
[Analytics Layer]
    ├── Data Warehouse (Snowflake)
    ├── BI Tool (Superset)
    └── ML Platform
         ↓
[Infra Layer]
    ├── Container: Docker + K8s
    ├── CI/CD: GitHub Actions
    ├── Monitoring: Prometheus + Grafana
    └── Logging: ELK Stack
```

## Component Details
| Component | Technology | Purpose | Instances | CPU/RAM | Cost/month |
|-----------|-----------|---------|-----------|---------|-----------|
|           |           |         |           |         |           |

## Bottleneck Analysis
| Component | Current Capacity | Expected Load | Bottleneck At | Mitigation |
|-----------|-----------------|--------------|--------------|------------|
|           |                 |              |              |            |

## Failure Mode Analysis
| Failure | Probability | Impact | Detection | Recovery | RTO | RPO |
|---------|------------|--------|-----------|----------|-----|-----|
| DB down |            |        |           |          |     |     |
| API overload |       |        |           |          |     |     |
| Cache miss storm |   |        |           |          |     |     |

## Security Architecture
| Layer | Control | Implementation | Status |
|-------|---------|---------------|--------|
| Network | Firewall | VPC + Security Groups | ✅ |
| Transport | TLS | TLS 1.3 | ✅ |
| Auth | OAuth2 + JWT | Auth0/Keycloak | ✅ |
| Data | Encryption at rest | AES-256 | ✅ |
| App | Input validation | Schema validation | ⚠️ |
```

---

## LUỒNG 3: Data Model Document

### Template
```markdown
# Data Model Document
**Project**: [tên]  |  **Schema Type**: Star / Snowflake  |  **Version**: 1.0

## ERD Overview
```
[fact_orders] ──→ [dim_users]
      │──→ [dim_products]
      │──→ [dim_dates]
      └──→ [dim_channels]
```

## Fact Tables
| Table | Grain | Rows (est.) | Partitioned By | Clustered By | Load Strategy |
|-------|-------|------------|---------------|-------------|--------------|
| fact_orders | 1 row per order line | 10M/month | order_date | user_id | Incremental |

### fact_orders
| Column | Type | Nullable | Description | Source | Transform |
|--------|------|----------|------------|--------|-----------|
| order_id | BIGINT | NO | PK | orders.id | Direct |
| user_key | BIGINT | NO | FK→dim_users | orders.user_id | SCD lookup |
| order_date_key | INT | NO | FK→dim_dates | orders.created_at | date_to_key() |
| quantity | INT | NO | Items ordered | order_lines.qty | SUM |
| amount | DECIMAL(12,2) | NO | Order amount | order_lines.price*qty | SUM |

## Dimension Tables
| Table | Type | SCD | Rows (est.) | Change Frequency |
|-------|------|-----|------------|-----------------|
| dim_users | Type 2 | SCD2 | 5M | Daily |
| dim_products | Type 1 | SCD1 | 50K | Weekly |
| dim_dates | Date | N/A | 3650 (10 years) | Pre-generated |

### dim_users (SCD Type 2)
| Column | Type | Description | SCD Role |
|--------|------|------------|---------|
| user_key | BIGINT | Surrogate PK | Surrogate |
| user_id | BIGINT | Natural key | Natural |
| name | VARCHAR | | Tracked |
| tier | VARCHAR | | Tracked |
| valid_from | TIMESTAMP | | Meta |
| valid_to | TIMESTAMP | | Meta |
| is_current | BOOLEAN | | Meta |

## Naming Conventions
| Entity | Pattern | Example |
|--------|---------|---------|
| Fact table | fact_[noun] | fact_orders |
| Dimension | dim_[noun] | dim_users |
| Staging | stg_[source]__[entity] | stg_postgres__orders |
| Intermediate | int_[entity]_[verb] | int_orders_enriched |
| Mart | mart_[domain]_[entity] | mart_finance_revenue |
```

---

## LUỒNG 4: ETL/ELT Documentation

### Template
```markdown
# ETL/ELT Documentation
**Project**: [tên]  |  **Orchestrator**: Airflow/Prefect/Dagster

## Pipeline Inventory
| ID | Pipeline | Source | Destination | Type | Schedule | SLA | Owner | Status |
|----|---------|--------|------------|------|---------|-----|-------|--------|
| P-001 |       |        |            | Batch/Stream/CDC | cron | 2h | | Active |

## Pipeline Detail: P-001

### Overview
| Property | Value |
|----------|-------|
| Name | |
| Source | [system + table/topic] |
| Destination | [system + table/view] |
| Type | Full / Incremental / CDC |
| Schedule | `0 6 * * *` (daily 6AM UTC) |
| Avg Runtime | X minutes |
| Avg Volume | Y rows / Z MB |
| SLA | Available by 8AM UTC |

### Transformation Logic
| Step | Operation | Input | Output | Logic | Business Rule |
|------|----------|-------|--------|-------|--------------|
| 1 | Extract | source.orders | raw.orders | SELECT * WHERE updated > last_run | |
| 2 | Clean | raw.orders | stg.orders | Dedup, null handling, type cast | |
| 3 | Enrich | stg.orders + dim_users | int.orders | JOIN on user_id | Exclude test users |
| 4 | Aggregate | int.orders | mart.daily_revenue | SUM(amount) GROUP BY date | |

### Error Handling
| Error Type | Detection | Action | Retry | Alert |
|-----------|----------|--------|-------|-------|
| Source unavailable | Connection timeout | Retry 3x exponential | 1m, 5m, 15m | Slack P1 |
| Schema drift | Column count mismatch | Pause + notify | No | PagerDuty P0 |
| Data quality fail | DQ check threshold | Block downstream | No | Slack P1 |
| Partial load | Row count < expected | Log + continue | N/A | Slack P2 |

### Dependencies
```
[P-001: Extract Orders] → [P-002: Clean Orders] → [P-003: Enrich]
                                                        ↓
[P-010: Extract Users] → [P-011: Clean Users] ────────→|
                                                        ↓
                                              [P-004: Build Mart]
                                                        ↓
                                              [P-005: Refresh Dashboard]
```

### Monitoring
| Metric | Expected | Alert Threshold | Dashboard |
|--------|----------|----------------|-----------|
| Runtime | <10 min | >30 min | Airflow UI |
| Row count | ~100K | <50K or >200K | DQ Dashboard |
| Error rate | 0% | >0% | Slack alert |
| Data freshness | <2h | >4h | Monitoring |

### Rollback Plan
| Scenario | Procedure | RTO |
|----------|----------|-----|
| Bad data loaded | Reload from raw using watermark | 1h |
| Schema change | Rollback migration, rebuild | 2h |
| Full pipeline failure | Manual trigger from last checkpoint | 30min |
```
