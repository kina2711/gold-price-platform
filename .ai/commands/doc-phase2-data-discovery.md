---
description: Tạo tài liệu Phase 2 — Data Discovery (Dataset Overview, Data Dictionary, Data Profiling)
argument-hint: [dataset-overview|data-dictionary|data-profiling|all]
---

Tạo document cụ thể cho Phase 2 — Data Discovery. Chọn luồng hoặc `all`.

## LUỒNG 1: Dataset Overview

### Template
```markdown
# Dataset Overview
**Project**: [tên]  |  **Date**: [ngày]  |  **Analyst**: [tên]

## Source Inventory
| # | Source | Type | Format | Size | Rows | Columns | Freshness | Owner |
|---|--------|------|--------|------|------|---------|-----------|-------|
| 1 |        | DB/API/File/Stream | CSV/JSON/Parquet | | | | | |

## Dataset Summary
| Dataset | Granularity | Time Range | Update Frequency | Primary Key | Foreign Keys |
|---------|------------|------------|-----------------|-------------|-------------|
|         | Transaction/Daily/User | | Realtime/Hourly/Daily | | |

## Column Type Distribution
| Dataset | Numeric | Categorical | DateTime | Boolean | Text | Binary | Total |
|---------|---------|------------|----------|---------|------|--------|-------|
|         |         |            |          |         |      |        |       |

## Cardinality Analysis
| Column | Unique Values | Total Rows | Cardinality Ratio | Type |
|--------|--------------|-----------|-------------------|------|
|        |              |           | High/Medium/Low   | ID/Category/Measure |

## Key Observations
1. [observation + business impact]
2. [observation + business impact]

## Data Gaps Identified
| Gap | Severity | Business Impact | Recommendation |
|-----|----------|----------------|----------------|
|     | High/Med/Low |            |                |
```

---

## LUỒNG 2: Data Dictionary

### Template
```markdown
# Data Dictionary
**Project**: [tên]  |  **Version**: 1.0  |  **Last Updated**: [ngày]

## [Table/Dataset Name]

### Table Metadata
| Property | Value |
|----------|-------|
| Description | |
| Granularity | |
| Primary Key | |
| Row Count | |
| Update Frequency | |
| Owner | |
| Source System | |

### Column Definitions
| # | Column | Business Meaning | Data Type | Nullable | Default | Example | Expected Range | Validation Rules | Business Rules | Risks/Caveats |
|---|--------|-----------------|-----------|----------|---------|---------|---------------|-----------------|---------------|---------------|
| 1 |        |                 |           | Y/N      |         |         |               |                 |               |               |

### Enum/Lookup Values
| Column | Value | Meaning | Active |
|--------|-------|---------|--------|
|        |       |         | Y/N    |

### Relationships
| Column | References | Cardinality | Nullable | On Delete |
|--------|-----------|-------------|----------|-----------|
|        | table.column | 1:1/1:N/N:M | | CASCADE/SET NULL |

### Change Log
| Date | Column | Change | Reason | Author |
|------|--------|--------|--------|--------|
|      |        |        |        |        |
```

---

## LUỒNG 3: Data Profiling Report

### Template
```markdown
# Data Profiling Report
**Dataset**: [tên]  |  **Date**: [ngày]  |  **Rows Profiled**: [N]

## Statistical Summary (Numeric Columns)
| Column | Count | Null% | Mean | Median | Std | Min | Max | P25 | P75 | Skew | Outliers |
|--------|-------|-------|------|--------|-----|-----|-----|-----|-----|------|----------|
|        |       |       |      |        |     |     |     |     |     |      |          |

## Categorical Summary
| Column | Count | Null% | Unique | Top Value | Top Freq | Entropy |
|--------|-------|-------|--------|-----------|----------|---------|
|        |       |       |        |           |          |         |

## DateTime Summary
| Column | Count | Null% | Min Date | Max Date | Range | Gaps Found |
|--------|-------|-------|----------|----------|-------|------------|
|        |       |       |          |          |       | Y/N        |

## Null Analysis
| Column | Null Count | Null % | Pattern | Business Impact | Action |
|--------|-----------|--------|---------|----------------|--------|
|        |           |        | Random/Systematic | |        |

## Duplicate Analysis
| Key Columns | Duplicate Rows | % of Total | Root Cause | Action |
|-------------|---------------|-----------|------------|--------|
|             |               |           |            |        |

## Anomalies Detected
| Column | Anomaly Type | Count | Example Values | Severity | Action |
|--------|-------------|-------|---------------|----------|--------|
|        | Outlier/Format/Range/Encoding | | | High/Med/Low | |
```
