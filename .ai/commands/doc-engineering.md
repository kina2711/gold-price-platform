---
description: Tạo tài liệu Engineering — Technical Design, DevOps, Monitoring, Runbook, Postmortem
argument-hint: [tech-design|devops|monitoring|runbook|postmortem|all]
---

Tạo document cho Engineering layer. Chọn luồng hoặc `all`.

## LUỒNG 1: Technical Design Document

### Template
```markdown
# Technical Design Document
**Feature**: [tên]  |  **Author**: [tên]  |  **Status**: Draft/Review/Approved

## 1. Overview
- Problem being solved
- Proposed solution (1-2 sentences)
- Scope: what's included and excluded

## 2. Background
- Current state (as-is)
- Pain points
- Previous approaches tried

## 3. Proposed Design
### Architecture
```
[Component diagram]
```
### API Design
| Method | Endpoint | Request | Response | Auth |
|--------|----------|---------|----------|------|
| POST   | /api/v1/... | `{...}` | `{...}` | Bearer |

### Database Changes
| Table | Change | Migration | Rollback |
|-------|--------|----------|---------|
|       | ADD COLUMN / CREATE TABLE | V001__description.sql | V001__rollback.sql |

### Sequence Diagram
```
Client → API → Service → DB → Cache → Response
```

## 4. Alternatives Considered
| Option | Pros | Cons | Why not |
|--------|------|------|---------|
|        |      |      |         |

## 5. Security Considerations
| Threat | Risk | Mitigation |
|--------|------|------------|
| SQL Injection | | Parameterized queries |
| XSS | | Input sanitization |
| Auth bypass | | JWT validation |

## 6. Performance
| Scenario | Expected | Acceptable | Unacceptable |
|----------|----------|-----------|-------------|
| P50 latency | 50ms | <200ms | >500ms |
| P99 latency | 200ms | <1s | >2s |
| Throughput | 1000 rps | >500 rps | <100 rps |

## 7. Testing Plan
| Test Type | Scope | Tool | Coverage Target |
|-----------|-------|------|----------------|
| Unit | Functions | pytest | >80% |
| Integration | API endpoints | pytest + httpx | >70% |
| E2E | User flows | Playwright | Critical paths |
| Load | Performance | k6/Locust | P99 < 1s @ 1000 rps |

## 8. Rollout Plan
| Phase | % Traffic | Duration | Rollback Criteria |
|-------|----------|----------|------------------|
| Canary | 5% | 1 day | Error rate >1% |
| Staged | 25% → 50% | 3 days | Latency P99 >1s |
| Full | 100% | - | - |

## 9. Open Questions
| # | Question | Owner | Deadline | Resolution |
|---|---------|-------|----------|-----------|
```

---

## LUỒNG 2: DevOps Documentation

### Template
```markdown
# DevOps Documentation
**Project**: [tên]  |  **Infra**: [AWS/GCP/Azure/On-prem]

## Docker
### Dockerfile Best Practices
- Multi-stage build: ✅/❌
- Non-root user: ✅/❌
- .dockerignore: ✅/❌
- Layer caching optimized: ✅/❌
- Image size: [X MB]
- Base image: [alpine/slim/full]

### Docker Compose (dev)
| Service | Image | Ports | Volumes | Depends On |
|---------|-------|-------|---------|-----------|
|         |       |       |         |           |

## CI/CD Pipeline
```
[Push to branch]
    → Lint + Format check
    → Unit tests
    → Build Docker image
    → Integration tests
    → Security scan (Trivy/Snyk)
    → [PR approved]
    → Deploy to staging
    → E2E tests on staging
    → [Manual approval]
    → Deploy to production (canary)
    → Monitor 1h
    → Full rollout
```

## Environments
| Env | URL | Infra | Data | Access |
|-----|-----|-------|------|--------|
| Dev | localhost:3000 | Docker Compose | Seed data | All devs |
| Staging | staging.example.com | K8s (1 replica) | Anonymized prod | Team |
| Production | app.example.com | K8s (3 replicas) | Real | Restricted |

## Rollback Procedures
| Scenario | Procedure | RTO | Owner |
|----------|----------|-----|-------|
| Bad deployment | `kubectl rollout undo` | 2 min | On-call |
| DB migration fail | Run rollback script | 10 min | DBA |
| Data corruption | Restore from backup | 1 hour | DE + DBA |

## Backup & Disaster Recovery
| Component | Backup Frequency | Retention | Recovery Method | RTO | RPO |
|-----------|-----------------|-----------|----------------|-----|-----|
| Database | Daily snapshot + WAL | 30 days | Point-in-time restore | 1h | 5min |
| Object Storage | Cross-region replication | 90 days | Switch region | 15min | 0 |
| Config/Secrets | Git + Vault | ∞ | Redeploy | 5min | 0 |
```

---

## LUỒNG 3: Monitoring Documentation

### Template
```markdown
# Monitoring Documentation
**Project**: [tên]

## Observability Stack
| Layer | Tool | Purpose |
|-------|------|---------|
| Metrics | Prometheus + Grafana | System & app metrics |
| Logging | ELK / Loki | Centralized logs |
| Tracing | Jaeger / OpenTelemetry | Distributed tracing |
| Alerting | PagerDuty / OpsGenie | Incident management |

## Key Metrics
| Metric | Type | Source | Dashboard | Alert Threshold |
|--------|------|--------|-----------|----------------|
| Request rate | Counter | App | API Dashboard | - |
| Error rate | Gauge | App | API Dashboard | >1% |
| Latency P99 | Histogram | App | API Dashboard | >1s |
| CPU usage | Gauge | Infra | Infra Dashboard | >80% |
| Memory usage | Gauge | Infra | Infra Dashboard | >85% |
| Disk usage | Gauge | Infra | Infra Dashboard | >90% |
| Pipeline success rate | Gauge | Airflow | Data Dashboard | <100% |
| Data freshness | Gauge | Custom | Data Dashboard | >1h delay |

## Alert Routing
| Severity | Channel | Response Time | Escalation |
|----------|---------|-------------|-----------|
| P0 Critical | PagerDuty (phone) | 15 min | → Manager → Director |
| P1 High | PagerDuty (push) | 1 hour | → Team lead |
| P2 Medium | Slack #alerts | 4 hours | → Sprint backlog |
| P3 Low | Slack #alerts | Next sprint | → Backlog |
```

---

## LUỒNG 4: Runbook

### Template
```markdown
# Runbook
**Project**: [tên]  |  **Last Updated**: [ngày]

## Common Scenarios

### Scenario 1: [Tên incident]
| Property | Value |
|----------|-------|
| Severity | P0/P1/P2 |
| Symptoms | [what you see] |
| Impact | [who is affected] |

**Diagnosis Steps**:
1. Check [dashboard/log/metric]
2. Run: `[diagnostic command]`
3. Look for: [specific pattern]

**Resolution**:
1. [Step 1]
2. [Step 2]
3. Verify: [how to confirm fixed]

**Prevention**: [how to prevent recurrence]

_(Lặp lại cho mỗi scenario)_
```

---

## LUỒNG 5: Postmortem Template

### Template
```markdown
# Postmortem: [Incident Title]
**Date**: [ngày]  |  **Duration**: [Xh Ym]  |  **Severity**: P0/P1

## Summary
[1-2 sentences: what happened, impact]

## Timeline (UTC)
| Time | Event |
|------|-------|
| HH:MM | [event] |

## Root Cause (5 Whys)
1. What: [symptom]
2. Why: [direct cause]
3. Why: [deeper cause]
4. Why: [system cause]
5. Why: [process/business cause]

## Impact
| Metric | Before | During | After |
|--------|--------|--------|-------|
| Users affected | 0 | X | 0 |
| Revenue lost | $0 | $X | $0 |
| Data delayed | 0h | Xh | 0h |

## Action Items
| # | Action | Owner | Priority | Deadline | Status |
|---|--------|-------|----------|----------|--------|
| 1 | [fix]  |       | P0       |          | Done   |
| 2 | [prevent] |    | P1       |          | Open   |

## Lessons Learned
- What went well: [list]
- What went poorly: [list]
- Where we got lucky: [list]
```
