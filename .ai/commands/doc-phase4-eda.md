---
description: Tạo tài liệu Phase 4 — EDA (Univariate, Bivariate, Multivariate, Insight Report)
argument-hint: [univariate|bivariate|multivariate|insight-report|all]
---

Tạo document cụ thể cho Phase 4 — EDA. Chọn luồng hoặc `all`.

## LUỒNG 1: Univariate Analysis Report

### Template
```markdown
# Univariate Analysis Report
**Dataset**: [tên]  |  **Date**: [ngày]

## Numeric Variables
| Variable | Count | Mean | Median | Std | Min | Max | Skew | Kurtosis | Distribution |
|----------|-------|------|--------|-----|-----|-----|------|----------|-------------|
|          |       |      |        |     |     |     |      |          | Normal/Skewed/Bimodal |

### Observations
| # | Variable | Observation | Root Cause | Business Impact | Recommendation |
|---|----------|------------|-----------|----------------|----------------|
| 1 |          |            |           |                |                |

## Categorical Variables
| Variable | Count | Unique | Top 5 Values (%) | Entropy | Imbalance Ratio |
|----------|-------|--------|------------------|---------|----------------|
|          |       |        |                  |         |                |

### Observations
| # | Variable | Observation | Root Cause | Business Impact | Recommendation |
|---|----------|------------|-----------|----------------|----------------|

## DateTime Variables
| Variable | Min | Max | Range | Gaps | Seasonality | Trend |
|----------|-----|-----|-------|------|-------------|-------|
|          |     |     |       | Y/N  | Y/N         | ↑/↓/→ |
```

---

## LUỒNG 2: Bivariate Analysis Report

### Template
```markdown
# Bivariate Analysis Report
**Dataset**: [tên]  |  **Date**: [ngày]

## Correlation Matrix (Top Pairs)
| Variable A | Variable B | Correlation | P-value | Strength | Direction | Business Meaning |
|-----------|-----------|------------|---------|----------|-----------|-----------------|
|           |           |            |         | Strong/Mod/Weak | +/- |              |

## Numeric vs Numeric
| Pair | Method | Result | Significance | Visualization | Insight |
|------|--------|--------|-------------|--------------|---------|
|      | Pearson/Spearman |  | p<0.05? | Scatter/Heatmap | |

## Categorical vs Numeric
| Category | Numeric | Method | Result | Significance | Insight |
|----------|---------|--------|--------|-------------|---------|
|          |         | T-test/ANOVA/Mann-Whitney | | | |

## Categorical vs Categorical
| Var A | Var B | Method | Chi² | P-value | Cramér's V | Insight |
|-------|-------|--------|------|---------|-----------|---------|
|       |       | Chi-squared | | | |         |

### Key Findings
| # | Finding | Variables | Root Cause | Business Impact | Recommendation | Priority |
|---|---------|----------|-----------|----------------|----------------|----------|
| 1 |         |          |           |                |                | P0/P1/P2 |
```

---

## LUỒNG 3: Multivariate Analysis Report

### Template
```markdown
# Multivariate Analysis Report
**Dataset**: [tên]  |  **Date**: [ngày]

## Segmentation Analysis
| Segment | Size | % of Total | Key Characteristics | Business Value |
|---------|------|-----------|-------------------|---------------|
|         |      |           |                   | High/Med/Low  |

## Feature Importance
| Feature | Importance Score | Method | Business Interpretation |
|---------|-----------------|--------|----------------------|
|         |                 | Random Forest/PCA/Mutual Info | |

## Cluster Analysis (nếu applicable)
| Cluster | Size | Key Features | Business Label | Revenue Share |
|---------|------|-------------|---------------|--------------|
| 0       |      |             | "Power Users"  |              |
| 1       |      |             | "At Risk"      |              |

## Interaction Effects
| Var A | Var B | Interaction | Business Meaning | Actionable |
|-------|-------|------------|-----------------|-----------|
|       |       |            |                 | Y/N       |
```

---

## LUỒNG 4: EDA Insight Report (Tổng hợp)

### Template
```markdown
# EDA Insight Report
**Project**: [tên]  |  **Date**: [ngày]  |  **Analyst**: [tên]

## Executive Summary
- Tổng quan dataset
- Top 5 insights
- Critical actions cần thực hiện

## Insight Catalog
| # | Observation | Why | Business Impact | Recommendation | Priority | Owner | Status |
|---|------------|-----|----------------|----------------|----------|-------|--------|
| 1 |            |     |                |                | P0       |       | Open   |
| 2 |            |     |                |                | P1       |       | Open   |

## Decision Intelligence
Cho mỗi insight:
1. **So What?** — Vậy thì sao?
2. **Why Should Anyone Care?** — Tại sao cần quan tâm?
3. **What Decision Can Be Made?** — Ra quyết định gì?
4. **What Happens If We Ignore It?** — Bỏ qua thì sao?

## Next Steps
| Action | Owner | Deadline | Priority | Dependency |
|--------|-------|----------|----------|-----------|
|        |       |          |          |           |

## Appendix
- Statistical tests performed
- Methodology notes
- Data limitations & caveats
```
