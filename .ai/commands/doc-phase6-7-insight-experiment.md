---
description: Tạo tài liệu Phase 6 & 7 — Insight Report & Experimentation Design
argument-hint: [insight-report|experiment-design|ab-test-plan|all]
---

Tạo document cho Phase 6 (Insight Generation) & Phase 7 (Experimentation).

## LUỒNG 1: Insight Report

### Template
```markdown
# Insight Report
**Project**: [tên]  |  **Period**: [date range]  |  **Author**: [tên]

## Executive Summary
- [1 paragraph tóm tắt key findings]
- Impact: [quantified]
- Urgency: [High/Medium/Low]

## Insight Details

### Insight #1: [Title]
| Aspect | Detail |
|--------|--------|
| **Observation** | [What did we find? — data-backed] |
| **Why** | [Root cause analysis — 5 Whys nếu cần] |
| **Business Impact** | [Quantified: $X revenue, Y% users affected] |
| **Recommendation** | [Specific, actionable next step] |
| **Priority** | P0 / P1 / P2 |
| **Owner** | [team/person] |
| **Deadline** | [date] |

**Decision Intelligence**:
- **So What?** [impact summary]
- **Why Care?** [business relevance]
- **Decision?** [action to take]
- **If Ignored?** [consequence]

**Supporting Data**:
| Metric | Before | After/Current | Change | Significance |
|--------|--------|-------------|--------|-------------|
|        |        |             |        | p < 0.05?   |

_(Lặp lại cho mỗi insight)_

## Insight Priority Matrix
| | High Impact | Low Impact |
|---|-----------|-----------|
| **Easy to Fix** | 🟢 Quick Wins | 🔵 Fill-ins |
| **Hard to Fix** | 🟡 Major Projects | ⚪ Deprioritize |

## Action Items
| # | Action | Source Insight | Owner | Priority | Deadline | Status |
|---|--------|--------------|-------|----------|----------|--------|
| 1 |        | Insight #X   |       | P0       |          | Open   |
```

---

## LUỒNG 2: Experiment Design Document

### Template
```markdown
# Experiment Design Document
**Experiment**: [tên]  |  **ID**: EXP-XXX  |  **Owner**: [tên]

## 1. Background
- Insight/observation dẫn đến experiment này
- Business context

## 2. Hypothesis
**H0 (Null)**: [Treatment sẽ KHÔNG có effect lên metric X]
**H1 (Alternative)**: [Treatment sẽ tăng/giảm metric X ít nhất Y%]

## 3. Metric Framework
| Type | Metric | Current Value | Expected Change | Measurement |
|------|--------|-------------|----------------|-------------|
| **Primary (Success)** | | | +X% | |
| **Secondary** | | | | |
| **Guardrail** | | | Không giảm >Y% | |

## 4. Design
| Property | Value |
|----------|-------|
| Type | A/B Test / A/B/n / Multivariate |
| Randomization Unit | User / Session / Device |
| Allocation | 50/50 (Control/Treatment) |
| Duration | [X weeks] |
| Target Population | [segment] |
| Exclusions | [who is excluded] |

## 5. Sample Size Calculation
| Parameter | Value |
|-----------|-------|
| Baseline conversion | X% |
| Minimum Detectable Effect (MDE) | Y% relative |
| Significance level (α) | 0.05 |
| Power (1-β) | 0.80 |
| **Required sample per variant** | **N** |
| **Estimated duration** | **X days** |

## 6. Statistical Plan
| Property | Value |
|----------|-------|
| Test type | Two-sided Z-test / T-test / Chi-squared |
| Correction | Bonferroni (if multiple comparisons) |
| Confidence level | 95% |
| Early stopping | Sequential testing with O'Brien-Fleming bounds |

## 7. Risks
| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| Novelty effect | Medium | False positive | Run >2 weeks |
| Sample ratio mismatch | Low | Invalid result | Monitor daily |
| Interference | Medium | Biased result | Isolate populations |

## 8. Launch Checklist
- [ ] Tracking implemented & QA'd
- [ ] Sample size validated
- [ ] Guardrail metrics monitored
- [ ] Rollback plan ready
- [ ] Stakeholders notified

## 9. Results Template
| Variant | N | Metric Value | CI (95%) | P-value | Significant? |
|---------|---|-------------|----------|---------|-------------|
| Control |   |             |          |         |             |
| Treatment |  |            |          |         |             |

## 10. Decision
- [ ] Ship treatment
- [ ] Iterate & re-test
- [ ] Kill experiment
**Rationale**: [why]
```

---

## LUỒNG 3: A/B Test Plan (simplified)

### Template
```markdown
# A/B Test Plan: [Tên]

| Field | Value |
|-------|-------|
| Hypothesis | If [change], then [metric] will [increase/decrease] by [X%] |
| Primary Metric | |
| Guardrail Metric | |
| Traffic Split | 50/50 |
| Duration | X weeks |
| Sample Size | N per variant |
| MDE | Y% |
| Significance | α = 0.05 |
| Power | 1 - β = 0.80 |

## Go / No-Go Criteria
| Criteria | Threshold | Action |
|----------|----------|--------|
| Primary metric | +X% with p<0.05 | Ship |
| Guardrail metric | Drop >Y% | Kill |
| Sample ratio | >1% mismatch | Investigate |
```
