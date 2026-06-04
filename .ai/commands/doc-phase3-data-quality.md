---
description: Tạo tài liệu Phase 3 — Data Quality Audit (DQ Report, DQ Rules, DQ Monitoring)
argument-hint: [dq-report|dq-rules|dq-monitoring|all]
---

Tạo document cụ thể cho Phase 3 — Data Quality. Chọn luồng hoặc `all`.

## LUỒNG 1: Data Quality Report

### Template
```markdown
# Data Quality Report
**Dataset**: [tên]  |  **Date**: [ngày]  |  **Overall Score**: [X/100]

## Executive Summary
- Tổng quan chất lượng dữ liệu
- Top 3 critical issues
- Recommended actions

## 6-Dimension Assessment

### 1. Completeness (Target: >95%)
| Table | Column | Total Rows | Null Count | Null % | Status | Impact |
|-------|--------|-----------|-----------|--------|--------|--------|
|       |        |           |           |        | ✅/⚠️/❌ |      |

### 2. Accuracy (Target: >99%)
| Check | Method | Sample Size | Error Count | Error % | Status | Examples |
|-------|--------|------------|------------|---------|--------|----------|
|       | Cross-ref/Manual/Rule |  |         |         | ✅/⚠️/❌ |    |

### 3. Validity (Target: >99%)
| Column | Rule | Valid Count | Invalid Count | Invalid % | Status | Invalid Examples |
|--------|------|------------|--------------|-----------|--------|-----------------|
|        | Range/Format/Enum |  |           |           | ✅/⚠️/❌ |               |

### 4. Consistency (Target: >99%)
| Check | Source A | Source B | Match Count | Mismatch | Mismatch % | Status |
|-------|---------|---------|------------|----------|-----------|--------|
|       |         |         |            |          |           | ✅/⚠️/❌ |

### 5. Uniqueness (Target: 100%)
| Table | Key Columns | Total Rows | Unique Rows | Duplicates | Dup % | Status |
|-------|------------|-----------|------------|------------|-------|--------|
|       |            |           |            |            |       | ✅/⚠️/❌ |

### 6. Timeliness (Target: <1h)
| Source | Expected SLA | Actual Delay | Max Delay | Status | Trend |
|--------|-------------|-------------|-----------|--------|-------|
|        | 1h          |             |           | ✅/⚠️/❌ | ↑/↓/→ |

## Issue Summary
| # | Issue | Dimension | Severity | Business Impact | Root Cause | Action | Owner | Deadline |
|---|-------|----------|----------|----------------|-----------|--------|-------|----------|
| 1 |       |          | P0/P1/P2 |                |           |        |       |          |

## Score Card
| Dimension | Score | Weight | Weighted Score | Trend |
|-----------|-------|--------|---------------|-------|
| Completeness | /100 | 20% |               | ↑/↓/→ |
| Accuracy | /100 | 25% |                   |       |
| Validity | /100 | 20% |                   |       |
| Consistency | /100 | 15% |                |       |
| Uniqueness | /100 | 10% |                 |       |
| Timeliness | /100 | 10% |                 |       |
| **Overall** | **/100** | **100%** |       |       |
```

---

## LUỒNG 2: Data Quality Rules Catalog

### Template
```markdown
# Data Quality Rules Catalog
**Project**: [tên]  |  **Version**: 1.0

## Rule Registry
| Rule ID | Dimension | Table | Column | Rule Description | SQL/Logic | Severity | Owner | Active |
|---------|----------|-------|--------|-----------------|-----------|----------|-------|--------|
| DQ-001  | Completeness | orders | order_id | NOT NULL | `WHERE order_id IS NULL` | P0 | DE | ✅ |
| DQ-002  | Validity | orders | amount | amount > 0 | `WHERE amount <= 0` | P0 | DE | ✅ |
| DQ-003  | Uniqueness | users | email | Unique per user | `GROUP BY email HAVING COUNT(*)>1` | P1 | DE | ✅ |
| DQ-004  | Timeliness | events | event_ts | Within 1h | `WHERE event_ts < NOW() - INTERVAL 1 HOUR` | P1 | DE | ✅ |

## Rule Categories
### Schema Rules (automated)
- NOT NULL checks
- Data type enforcement
- Enum validation
- Range checks

### Business Rules (configured)
- Cross-field validation
- Aggregate thresholds
- Referential integrity
- Temporal logic

### Statistical Rules (learned)
- Distribution drift
- Anomaly detection
- Volume deviation
- Freshness monitoring
```

---

## LUỒNG 3: Data Quality Monitoring Setup

### Template
```markdown
# Data Quality Monitoring
**Project**: [tên]

## Monitoring Architecture
```
[Data Pipeline] → [DQ Check Layer] → [Results Store]
                                          ↓
                                    [Alert Engine]
                                          ↓
                                [Slack/Email/PagerDuty]
```

## Alert Configuration
| Alert | Condition | Severity | Channel | Escalation | Auto-remediate |
|-------|----------|----------|---------|------------|---------------|
| Null spike | null% > 5% | P0 | PagerDuty | On-call DE → Manager | Block pipeline |
| Late data | delay > 1h | P1 | Slack #data-alerts | DE team | Retry 3x |
| Schema drift | New/dropped column | P1 | Slack + Email | AE team | Pause & notify |
| Volume anomaly | >50% deviation | P2 | Slack | DA team | Log only |

## Dashboard Specs
| Panel | Metric | Visualization | Refresh |
|-------|--------|--------------|---------|
| DQ Score Trend | Overall score over time | Line chart | Hourly |
| Dimension Breakdown | Score per dimension | Radar chart | Hourly |
| Top Issues | Active issues by severity | Table | Real-time |
| Pipeline Health | Pass/fail per pipeline run | Heatmap | Per run |

## Incident Response
| Severity | Response Time | Resolution Time | Escalation |
|----------|-------------|----------------|------------|
| P0 — Critical | 15 min | 1 hour | On-call → Manager → Director |
| P1 — High | 1 hour | 4 hours | Team lead |
| P2 — Medium | 4 hours | 24 hours | Team |
| P3 — Low | Next sprint | Next release | Backlog |
```
