---
description: Tạo tài liệu Phase 8 — Dashboard Design (Executive, Operational, Analytical, Spec)
argument-hint: [executive|operational|analytical|dashboard-spec|all]
---

Tạo document cho Phase 8 — Dashboard Design. Chọn loại dashboard hoặc `all`.

## LUỒNG 1: Executive Dashboard Spec

### Template
```markdown
# Executive Dashboard Specification
**Audience**: C-Suite, VP+  |  **Purpose**: Strategic decisions  |  **Refresh**: Daily

## KPI Header (Top Row)
| KPI | Current | Target | vs Target | vs Last Period | Trend |
|-----|---------|--------|----------|---------------|-------|
| Revenue | $X | $Y | +Z% ✅ | +W% | ↑ |
| Active Users | | | | | |
| Conversion | | | | | |
| NPS | | | | | |

## Charts
| # | Chart | Type | Metrics | Dimensions | Time Range | Drill-down |
|---|-------|------|---------|------------|-----------|------------|
| 1 | Revenue Trend | Line + Area | Revenue, Target | Daily | 90 days | → by region |
| 2 | User Growth | Stacked Bar | New/Returning | Weekly | 52 weeks | → by channel |
| 3 | Conversion Funnel | Funnel | View→Cart→Purchase | - | 30 days | → by platform |

## Filters
| Filter | Values | Default | Multi-select |
|--------|--------|---------|-------------|
| Date Range | Custom | Last 30 days | N/A |
| Region | All/US/EU/APAC | All | Yes |
| Platform | All/Web/iOS/Android | All | Yes |

## Design Notes
- Maximum 6-8 KPIs visible without scrolling
- Color: green=good, red=bad, gray=neutral
- Mobile-responsive required
- Print-friendly layout
```

---

## LUỒNG 2: Operational Dashboard Spec

### Template
```markdown
# Operational Dashboard Specification
**Audience**: Operations, On-call  |  **Purpose**: Day-to-day monitoring  |  **Refresh**: Real-time / 5min

## Health Status (Top Row)
| System | Status | Uptime | Last Incident | Response Time |
|--------|--------|--------|-------------|--------------|
|        | 🟢/🟡/🔴 | 99.X% |             | Xms          |

## Charts
| # | Chart | Type | Metric | Alert Threshold | Action when Triggered |
|---|-------|------|--------|----------------|---------------------|
| 1 | Pipeline Status | Heatmap | Pass/Fail per run | Any fail | Investigate logs |
| 2 | Data Freshness | Gauge | Minutes since last update | >60 min | Check pipeline |
| 3 | Error Rate | Line | Errors/min | >10/min | Page on-call |
| 4 | Queue Depth | Area | Messages pending | >1000 | Scale consumers |

## Alerts Integration
| Alert | Source | Display | Clickable |
|-------|--------|---------|----------|
| P0 Critical | PagerDuty | Red banner, sound | → Incident page |
| P1 Warning | Slack | Yellow card | → Channel |
| P2 Info | Log | Expandable row | → Log search |
```

---

## LUỒNG 3: Analytical Dashboard Spec

### Template
```markdown
# Analytical Dashboard Specification
**Audience**: Data Analysts, Product Managers  |  **Purpose**: Deep-dive analysis  |  **Refresh**: Daily

## Analysis Panels
| # | Panel | Purpose | Interaction |
|---|-------|---------|------------|
| 1 | Segmentation Explorer | Slice metrics by any dimension | Multi-filter + drill-down |
| 2 | Cohort Analysis | Retention by signup cohort | Heatmap + line chart toggle |
| 3 | Funnel Builder | Custom funnel steps | Drag-drop steps |
| 4 | Time Series Decomposition | Trend, seasonality, residual | Auto-detect + manual |
| 5 | Comparison View | Compare segments/periods | Side-by-side |

## Filters (phải flexible)
| Filter | Type | Behavior |
|--------|------|----------|
| Date Range | Date picker | Custom range, presets (7d/30d/90d/YTD) |
| Dimensions | Multi-select dropdown | Any dimension column |
| Measures | Selectable | Switch between metrics |
| Granularity | Toggle | Hourly/Daily/Weekly/Monthly |
| Segment | Builder | AND/OR conditions |
```

---

## LUỒNG 4: Dashboard Specification Template (Generic)

### Template
```markdown
# Dashboard Specification: [Tên Dashboard]

## Overview
| Property | Value |
|----------|-------|
| Name | |
| ID | DASH-XXX |
| Audience | |
| Purpose | |
| Decision Supported | |
| Refresh Frequency | |
| Data Source | |
| Owner | |
| Platform | Superset/Metabase/Tableau/Looker/Custom |

## Layout Wireframe
```
┌─────────────────────────────────────┐
│  [KPI 1]  [KPI 2]  [KPI 3] [KPI 4] │  ← Header KPIs
├──────────────────┬──────────────────┤
│                  │                  │
│   [Chart 1]      │   [Chart 2]     │  ← Main charts
│                  │                  │
├──────────────────┴──────────────────┤
│                                     │
│           [Chart 3]                 │  ← Full width
│                                     │
├──────────────────┬──────────────────┤
│   [Table 1]      │   [Chart 4]     │  ← Detail
└──────────────────┴──────────────────┘
```

## Component Specifications
| # | Component | Type | Data | Filters | Drill-down | Notes |
|---|-----------|------|------|---------|-----------|-------|
| 1 |           | KPI Card / Line / Bar / Table / Pie / Funnel / Heatmap | | | | |

## Access Control
| Role | Access Level | Rows Visible |
|------|-------------|-------------|
| Admin | Full + Edit | All |
| Manager | View + Export | Own region |
| Analyst | View + Drill | Own team |
| Viewer | View only | Summary only |

## Performance Requirements
| Metric | Target |
|--------|--------|
| Initial load | <3 seconds |
| Filter response | <1 second |
| Export | <5 seconds |
| Max concurrent users | 50 |
```
