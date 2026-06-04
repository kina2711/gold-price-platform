---
description: Tạo tài liệu Knowledge Transfer — KT Guide, Lessons Learned, Final Dossier, Project Handoff
argument-hint: [kt-guide|lessons-learned|final-dossier|handoff|all]
---

Tạo document cho Knowledge Transfer. Chọn luồng hoặc `all`.

## LUỒNG 1: Knowledge Transfer Guide

### Template
```markdown
# Knowledge Transfer Guide
**Project**: [tên]  |  **Author**: [tên]  |  **Date**: [ngày]

## 1. Business Context
- Vấn đề kinh doanh đang giải quyết
- Stakeholders chính và mục tiêu
- KPI Framework (link đến KPI Tree)
- Quyết định mà data hỗ trợ

## 2. System Overview
- Architecture diagram (link đến System Architecture Doc)
- Tech stack summary
- Component interactions
- External dependencies

## 3. Data Architecture
- Data flow diagram (link đến Data Architecture Doc)
- Key data sources và SLAs
- Data model overview (link đến Data Model Doc)
- Data quality thresholds

## 4. Key Processes
| Process | Description | Owner | Schedule | Runbook |
|---------|-----------|-------|---------|---------|
| Daily ETL | Ingest + transform | DE team | 6AM UTC | [link] |
| DQ Monitoring | Quality checks | DE team | Per run | [link] |
| Dashboard Refresh | BI refresh | AE team | 8AM UTC | [link] |
| Model Retrain | ML pipeline | DS team | Weekly | [link] |

## 5. Access & Permissions
| System | How to Get Access | Approval By | Time |
|--------|------------------|-------------|------|
|        |                  |             |      |

## 6. Common Pitfalls & Gotchas
| # | Pitfall | Impact | Prevention |
|---|---------|--------|-----------|
| 1 | [gotcha] | [impact] | [how to avoid] |

## 7. FAQ
| Question | Answer |
|----------|--------|
|          |        |

## 8. Contacts
| Area | Primary | Secondary | Escalation |
|------|---------|-----------|-----------|
|      |         |           |           |

## 9. Onboarding Checklist (for new team member)
- [ ] Read this guide
- [ ] Get access to [systems]
- [ ] Review architecture docs
- [ ] Pair with [person] on [task]
- [ ] Complete shadow on-call rotation
- [ ] Deploy a change to staging
```

---

## LUỒNG 2: Lessons Learned

### Template
```markdown
# Lessons Learned
**Project**: [tên]  |  **Date**: [ngày]

## Per Milestone Summary

### Milestone 1: [Tên]
| Aspect | Details |
|--------|---------|
| **What Worked** | [list] |
| **What Failed** | [list] |
| **Trade-offs Made** | [list: chose X over Y because Z] |
| **Technical Debt Created** | [list: what + severity + remediation plan] |
| **Future Improvements** | [list] |
| **Key Decision** | [decision + rationale + alternatives considered] |

_(Lặp lại cho mỗi milestone)_

## Cross-Cutting Themes
| Theme | Occurrences | Root Cause | Systemic Fix |
|-------|-----------|-----------|-------------|
| [e.g. Schema drift] | Milestone 2, 4 | No data contracts | Implement schema registry |

## Recommendations for Future Projects
| # | Recommendation | Priority | Effort | Impact |
|---|---------------|----------|--------|--------|
| 1 | [recommendation] | High | Low | High |

## Technical Debt Inventory
| ID | Debt | Location | Severity | Business Impact | Remediation | Effort | Status |
|----|------|---------|----------|----------------|-------------|--------|--------|
| TD-001 | | | P0/P1/P2 | | | S/M/L | Open |
```

---

## LUỒNG 3: Final Project Dossier (Table of Contents)

### Template
```markdown
# Final Project Dossier
**Project**: [tên]  |  **Version**: 1.0  |  **Date**: [ngày]

## Table of Contents

### Part I — Business
1. [Executive Summary](./executive-summary.md)
2. [Project Overview](./project-overview.md)
3. [BRD](./brd.md)
4. [FRD](./frd.md)
5. [KPI Tree](./kpi-tree.md)
6. [Stakeholder Map](./stakeholder-map.md)

### Part II — Data
7. [Data Architecture](./data-architecture.md)
8. [Data Model](./data-model.md)
9. [Data Dictionary](./data-dictionary.md)
10. [Metric Catalog](./metric-catalog.md)
11. [ETL/ELT Documentation](./etl-documentation.md)

### Part III — Analytics
12. [EDA Report](./eda-report.md)
13. [Insight Report](./insight-report.md)
14. [Dashboard Documentation](./dashboard-documentation.md)
15. [Experiment Results](./experiment-results.md)

### Part IV — Engineering
16. [Technical Design](./technical-design.md)
17. [System Architecture](./system-architecture.md)
18. [DevOps](./devops.md)

### Part V — Operations
19. [Data Quality Report](./data-quality.md)
20. [Monitoring](./monitoring.md)
21. [Runbook](./runbook.md)
22. [Postmortem Log](./postmortem-log.md)

### Part VI — Knowledge
23. [Knowledge Transfer Guide](./kt-guide.md)
24. [Lessons Learned](./lessons-learned.md)

## Cross-Reference Matrix
| Document | Related To | Dependency |
|----------|-----------|-----------|
| BRD | KPI Tree, Stakeholder Map | BRD drives KPIs |
| Data Model | ETL Docs, Metric Catalog | Model defines ETL targets |
| Dashboard | Metric Catalog, Data Model | Dashboard consumes metrics |

## Version History
| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0     |      |        | Initial release |

## Sign-Off
| Role | Name | Date | Approval |
|------|------|------|----------|
| BA   |      |      | ☐        |
| DA   |      |      | ☐        |
| DE   |      |      | ☐        |
| AE   |      |      | ☐        |
| Dev  |      |      | ☐        |
```

---

## LUỒNG 4: Project Handoff Checklist

### Template
```markdown
# Project Handoff Checklist
**From**: [team/person]  |  **To**: [team/person]  |  **Date**: [ngày]

## Documentation
- [ ] All docs in Final Dossier complete and reviewed
- [ ] Code documentation (README, inline comments) up to date
- [ ] API documentation current
- [ ] Architecture diagrams current

## Access
- [ ] All system accesses transferred
- [ ] Secrets/credentials rotated and shared securely
- [ ] Admin permissions transferred

## Knowledge
- [ ] KT sessions completed (recorded)
- [ ] FAQ document created
- [ ] Common pitfalls documented
- [ ] On-call procedures transferred

## Operations
- [ ] Monitoring dashboards shared
- [ ] Alert routing updated
- [ ] On-call schedule updated
- [ ] Runbook reviewed with new team
- [ ] Incident escalation path updated

## Verification
- [ ] New team can deploy independently
- [ ] New team can troubleshoot common issues
- [ ] New team has completed 1 on-call rotation
- [ ] Handoff confirmed by both parties

## Sign-Off
| Party | Name | Date | Confirmed |
|-------|------|------|-----------|
| Sender |     |      | ☐         |
| Receiver |   |      | ☐         |
| Manager |    |      | ☐         |
```
