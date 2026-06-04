---
description: Tạo tài liệu Phase 5 — Metric Design (Metric Catalog, Metric Spec, SQL Logic)
argument-hint: [metric-catalog|metric-spec|sql-logic|all]
---

Tạo document cụ thể cho Phase 5 — Metric Design. Chọn luồng hoặc `all`.

## LUỒNG 1: Metric Catalog

### Template
```markdown
# Metric Catalog
**Project**: [tên]  |  **Version**: 1.0  |  **Last Updated**: [ngày]

## Metric Registry
| ID | Metric Name | Business Definition | Category | Type | Owner | Status |
|----|------------|-------------------|----------|------|-------|--------|
| M-001 |         |                   | Revenue/Growth/Quality | Input/Output/Guardrail | | Active |

## Metric Details (cho từng metric)

### M-001: [Metric Name]
| Property | Value |
|----------|-------|
| Business Definition | [plain language] |
| Technical Definition | [precise formula] |
| SQL Logic | [query] |
| Grain | Daily/Weekly/Monthly |
| Dimensions | [cut by what] |
| Data Source | [table/view] |
| Refresh Frequency | Real-time/Hourly/Daily |
| Owner | [team/person] |
| Consumers | [who uses this] |
| Caveats | [edge cases, known issues] |
| Created | [date] |
| Last Modified | [date] |

### Metric Hierarchy
```
[North Star: Revenue]
├── [L1: Traffic] — Owner: Marketing
│   ├── [L2: Organic Traffic] — Owner: SEO
│   └── [L2: Paid Traffic] — Owner: Performance Marketing
├── [L1: Conversion Rate] — Owner: Product
│   ├── [L2: View → Cart] — Owner: Product
│   └── [L2: Cart → Purchase] — Owner: Checkout Team
└── [L1: AOV] — Owner: Merchandising
```
```

---

## LUỒNG 2: Metric Specification (per metric)

### Template
```markdown
# Metric Specification: [Metric Name]
**ID**: M-XXX  |  **Owner**: [team]  |  **Version**: 1.0

## 1. Business Context
- Why does this metric exist?
- What decision does it support?
- Who cares about this metric?

## 2. Definition
| Aspect | Detail |
|--------|--------|
| Business Definition | [plain language cho business user] |
| Technical Definition | [exact formula: numerator / denominator × 100] |
| Unit | %, $, count, ratio |
| Direction | Higher is better / Lower is better |

## 3. Calculation
### Formula
```
metric = (numerator_condition) / (denominator_condition) × 100
```

### SQL
```sql
SELECT
    date_trunc('day', event_ts) AS metric_date,
    COUNT(CASE WHEN action = 'purchase' THEN 1 END)::FLOAT
    / NULLIF(COUNT(CASE WHEN action = 'view' THEN 1 END), 0) * 100
    AS conversion_rate
FROM events
WHERE event_ts >= :start_date
GROUP BY 1
```

### Edge Cases
| Case | Handling | Rationale |
|------|---------|-----------|
| Denominator = 0 | Return NULL, not 0 | Tránh misleading |
| Partial day | Exclude incomplete days | Accuracy > timeliness |
| Refunds | Exclude | Count net purchases only |

## 4. Dimensions (sliceable by)
| Dimension | Source | Cardinality | Notes |
|-----------|--------|------------|-------|
| Country | users.country | ~200 | |
| Platform | events.platform | 3 (web/ios/android) | |
| Channel | attribution.channel | ~10 | Last-touch model |

## 5. Refresh & SLA
| Property | Value |
|----------|-------|
| Refresh Frequency | Daily at 06:00 UTC |
| Data Delay | T+1 |
| SLA | Available by 08:00 UTC |
| Backfill Policy | Last 7 days on failure |

## 6. Dependencies
| Depends On | Type | Impact if Broken |
|-----------|------|-----------------|
| events table | Source | Metric unavailable |
| users table | Enrichment | Missing dimensions |
| attribution model | Logic | Channel breakdown wrong |

## 7. Validation Rules
| Rule | Expected | Alert if |
|------|----------|----------|
| Daily volume | >10K events | <5K events |
| Value range | 0-100% | <0 or >100% |
| Day-over-day change | ±20% | >50% change |

## 8. Changelog
| Date | Change | Author | Reason |
|------|--------|--------|--------|
|      |        |        |        |
```

---

## LUỒNG 3: SQL Logic Documentation

### Template
```markdown
# SQL Logic Documentation
**Project**: [tên]  |  **Version**: 1.0

## Query Registry
| ID | Metric | Table | Complexity | Performance | Last Tested |
|----|--------|-------|-----------|-------------|-------------|
| Q-001 | | | Simple/Medium/Complex | <1s / <10s / >10s | |

## Query Details

### Q-001: [Metric Name]
**Purpose**: [what this query calculates]
**Input**: [source tables]
**Output**: [result schema]

```sql
-- ============================
-- Metric: [name]
-- Author: [name]
-- Created: [date]
-- Description: [what it does]
-- Dependencies: [tables used]
-- Performance: ~Xs on N rows
-- ============================

WITH base AS (
    -- Step 1: Filter raw data
    SELECT ...
    FROM ...
    WHERE ...
),
aggregated AS (
    -- Step 2: Aggregate
    SELECT ...
    FROM base
    GROUP BY ...
)
-- Step 3: Final calculation
SELECT ...
FROM aggregated
```

**Performance Notes**:
- Expected runtime: [X seconds]
- Rows processed: [N]
- Indexes used: [list]
- Optimization opportunities: [list]

**Test Cases**:
| Test | Input | Expected Output | Status |
|------|-------|----------------|--------|
| Happy path | | | ✅/❌ |
| Empty data | | NULL/0 | ✅/❌ |
| Edge case | | | ✅/❌ |
```
