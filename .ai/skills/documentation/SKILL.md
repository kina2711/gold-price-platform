---
name: documentation
description: Tạo full documentation & knowledge transfer package theo FAANG standards
---

# Documentation Skill

Sau milestone cuối, KHÔNG ĐƯỢC kết thúc. Bắt buộc tạo đầy đủ documents.

## BUSINESS DOCUMENTS

### Executive Summary
Business Problem, Impact (quantified), KPI Impact, Outcomes, Risks & Mitigations

### Project Overview
Scope, Objectives, Deliverables, Constraints, Timeline

### BRD (Business Requirement Document)
Background & Context, Problem Statement, Business Goals, Success Criteria & KPIs, Stakeholders & RACI, Risks & Assumptions, Dependencies, Out of Scope

### FRD (Functional Requirement Document)
Functional Requirements (numbered), User Stories (As a..., I want..., So that...), Acceptance Criteria, Edge Cases

## TECHNICAL DOCUMENTS

### Technical Design Document
System Architecture (diagram), Component Design, API Contracts, Security Architecture, Failure Modes & Recovery, Performance Requirements

### Data Architecture Document
Data Sources (inventory), Data Flow Diagram, Data Lineage Map, Data Ownership Matrix, Data Governance Policies, PII/Sensitive Data Handling

### Data Model Document
ERD, Table Definitions (grain, keys, relationships), Fact/Dimension/Bridge Tables, SCD Strategy, Naming Conventions

### ETL/ELT Documentation
Pipeline Inventory, Source→Destination Mapping, Transformation Logic, Schedule/SLA, Retry Strategy, Error Handling, Data Contracts

## ANALYTICS DOCUMENTS

### Metric Catalog
| Metric | Business Def | SQL | Owner | Refresh | Grain | Caveats |

### Data Dictionary
| Table | Field | Meaning | Type | Nullable | Range | Rules |

### Analytics Documentation
KPI Tree (visual), Business Questions → Metrics Mapping, Segmentation Strategy, Key Insights

### Dashboard Documentation
| Dashboard | Audience | Purpose | Metrics | Filters | Refresh | Caveats |

## QUALITY & OPERATIONS

### Data Quality Documentation
| Dimension | Rule | Threshold | Current | Alert | Owner |
Dimensions: Completeness >95%, Accuracy >99%, Validity >99%, Consistency >99%, Uniqueness 100%, Timeliness <1h

### Monitoring Documentation
Logging Strategy, Key Metrics & Dashboards, Alert Rules, Escalation Path, Incident Response

### DevOps Documentation
Docker, CI/CD Pipeline, Environment Mgmt, Deployment Strategy, Rollback, Backup, DR

### Runbook
| Scenario | Symptoms | Diagnosis | Resolution | Escalation |

## KNOWLEDGE TRANSFER

### Postmortem Template
Incident Description, Timeline, Root Cause (5 Whys), Impact, Action Items, Prevention

### Knowledge Transfer Guide
Business Context, System Overview, Data Architecture, KPIs, Deployment, Monitoring, Pitfalls, FAQ

### Lessons Learned
| Milestone | Worked | Failed | Trade-offs | Tech Debt | Improvements |

### Final Project Dossier
Tổng hợp toàn bộ documents, Table of Contents, Cross-references, Version history, Sign-off

## META
Mỗi document: Author, Date, Version, Status (Draft → Peer Review → Stakeholder Review → Final)
