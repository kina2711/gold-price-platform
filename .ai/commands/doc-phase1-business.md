---
description: Tạo tài liệu Phase 1 — Business Analysis (BRD, PRS, KPI Tree, Stakeholder Map)
argument-hint: [brd|prs|kpi-tree|stakeholder|decision-framework|all]
---

Tạo document cụ thể cho Phase 1 — Business Analysis. Chọn luồng cụ thể hoặc `all`.

## LUỒNG 1: BRD (Business Requirement Document)

### Template
```markdown
# Business Requirement Document
**Project**: [tên]  |  **Version**: 1.0  |  **Author**: [tên]  |  **Date**: [ngày]  |  **Status**: Draft

## 1. Background & Context
- Bối cảnh ngành/thị trường
- Tình trạng hiện tại (as-is)
- Pain points hiện tại

## 2. Problem Statement
- Vấn đề cụ thể (quantified nếu có)
- Ai bị ảnh hưởng?
- Hậu quả nếu không giải quyết?

## 3. Business Goal
- Mục tiêu ngắn hạn (3 tháng)
- Mục tiêu trung hạn (6-12 tháng)
- Mục tiêu dài hạn (1-3 năm)

## 4. Success Criteria & KPIs
| KPI | Baseline | Target | Timeframe | Owner |
|-----|----------|--------|-----------|-------|
|     |          |        |           |       |

## 5. Stakeholders & RACI
| Stakeholder | R | A | C | I | Objective |
|------------|---|---|---|---|-----------|
|            |   |   |   |   |           |

## 6. Scope
### In Scope
- [liệt kê]
### Out of Scope
- [liệt kê]

## 7. Assumptions
1. [assumption]

## 8. Constraints
1. [constraint]

## 9. Dependencies
| Dependency | Type | Risk if Delayed |
|-----------|------|-----------------|
|           |      |                 |

## 10. Risks
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
|      |           |        |            |

## 11. Approval
| Role | Name | Date | Signature |
|------|------|------|-----------|
|      |      |      |           |
```

---

## LUỒNG 2: PRS (Product Requirement Summary)

### Template
```markdown
# Product Requirement Summary
**Product**: [tên]  |  **Version**: 1.0  |  **Date**: [ngày]

## 1. Objective
- Mục tiêu sản phẩm 1 câu

## 2. User Persona
| Persona | Role | Goal | Pain Point |
|---------|------|------|------------|
|         |      |      |            |

## 3. User Journey
### Flow chính
```
[Trigger] → [Step 1] → [Step 2] → [Decision Point] → [Step 3] → [Outcome]
```
### Happy Path
### Error Path
### Edge Cases

## 4. Business Flow
```
[Request] → [Validation] → [Processing] → [Storage] → [Response] → [Analytics]
```

## 5. Data Flow
```
[User Input] → [API] → [Service] → [DB] → [Transform] → [Dashboard/Report]
```

## 6. Functional Requirements
| ID | Requirement | Priority | Acceptance Criteria |
|----|------------|----------|-------------------|
| FR-001 | | P0/P1/P2 | |

## 7. Non-Functional Requirements
| ID | Requirement | Metric | Target |
|----|------------|--------|--------|
| NFR-001 | Performance | Latency | <200ms |
| NFR-002 | Availability | Uptime | 99.9% |

## 8. Success Metrics
| Metric | Definition | Baseline | Target | Measurement |
|--------|-----------|----------|--------|-------------|
|        |           |          |        |             |

## 9. Risks & Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
|      |        |            |
```

---

## LUỒNG 3: KPI Tree

### Template
```markdown
# KPI Tree
**Business**: [tên]  |  **North Star Metric**: [metric]

## Tree Structure
```
[North Star Metric]
├── [Driver 1]
│   ├── [Sub-driver 1.1]
│   │   ├── [Lever 1.1.1] — Owner: [team] — Target: [value]
│   │   └── [Lever 1.1.2] — Owner: [team] — Target: [value]
│   └── [Sub-driver 1.2]
│       └── [Lever 1.2.1] — Owner: [team] — Target: [value]
├── [Driver 2]
│   ├── [Sub-driver 2.1]
│   └── [Sub-driver 2.2]
└── [Driver 3]
    └── [Sub-driver 3.1]
```

## Metric Definitions
| Metric | Business Definition | Formula | Owner | Frequency | Data Source |
|--------|-------------------|---------|-------|-----------|------------|
|        |                   |         |       |           |            |

## Metric Dependencies
| Metric | Depends On | Impact Direction | Lag Time |
|--------|-----------|-----------------|----------|
|        |           | ↑ positive / ↓ inverse |  |

## Metric Classification
| Metric | Type | Category |
|--------|------|----------|
|        | Input/Output/Guardrail | Leading/Lagging |
```

---

## LUỒNG 4: Stakeholder Map

### Template
```markdown
# Stakeholder Map
**Project**: [tên]

## Power-Interest Matrix
```
         HIGH POWER
    ┌──────────┬──────────┐
    │  Manage  │   Key    │
    │  Closely │  Players │
    ├──────────┼──────────┤
    │   Keep   │   Keep   │
    │ Informed │ Satisfied│
    └──────────┴──────────┘
         LOW POWER
   LOW INTEREST    HIGH INTEREST
```

## Stakeholder Details
| Stakeholder | Role | Power | Interest | Strategy | KPI | Data Needs | Communication |
|------------|------|-------|----------|----------|-----|------------|---------------|
|            | CEO  | High  | High     | Key Player | Revenue | Exec Dashboard | Weekly |

## Communication Plan
| Stakeholder | Channel | Frequency | Format | Owner |
|------------|---------|-----------|--------|-------|
|            | Email   | Weekly    | Report | PM    |
```

---

## LUỒNG 5: Decision Framework

### Template
```markdown
# Decision Framework
**Project**: [tên]

## Business Decisions Supported
| Decision | Question | Data Required | Metric | Threshold | Action |
|----------|----------|--------------|--------|-----------|--------|
| Marketing Budget | Tăng hay giảm? | CAC, ROAS, LTV | ROAS | >3x | Tăng 20% |
| Feature Priority | Build gì trước? | Usage data, Revenue impact | Revenue/Effort ratio | >2x | Prioritize |
| Churn Prevention | Retain ai? | Churn signals, LTV | Churn probability | >70% | Trigger campaign |

## Decision Tree
```
[Situation]
├── IF [condition A] → [Action A] → Expected: [outcome]
├── IF [condition B] → [Action B] → Expected: [outcome]
└── ELSE → [Default Action] → Expected: [outcome]
```

## Data-to-Decision Flow
```
[Raw Data] → [Metric] → [Threshold] → [Alert/Report] → [Decision Maker] → [Action] → [Measure Impact]
```
```
