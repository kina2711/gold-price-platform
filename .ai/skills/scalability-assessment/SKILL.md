---
name: scalability-assessment
description: Đánh giá khả năng scale x10, x100, x1000 và tìm breaking points
---

# Scalability Assessment Skill

## SCALABILITY MATRIX

| Scale | Data Volume | Users | Txn/s | Architecture Changes Needed |
|-------|------------|-------|-------|---------------------------|
| Current (x1) | | | | Baseline |
| x10 | | | | |
| x100 | | | | |
| x1000 | | | | |

## BREAKING POINTS ANALYSIS

| Component | Breaking Point | Impact | Mitigation |
|-----------|---------------|--------|------------|
| Database | | | |
| API | | | |
| Pipeline | | | |
| Storage | | | |
| Network | | | |
| Cache | | | |
| Queue | | | |

## TECH STACK EVALUATION

| Criteria | Weight | Option A | Option B | Option C |
|----------|--------|----------|----------|----------|
| Learning Curve | | | | |
| Community Support | | | | |
| Scalability | | | | |
| Performance | | | | |
| Cost | | | | |
| Team Familiarity | | | | |
| Ecosystem | | | | |
| **Weighted Score** | | | | |

## DATA QUALITY AT SCALE

| Dimension | Metric | Threshold | Current | Status |
|-----------|--------|-----------|---------|--------|
| Completeness | % non-null | >95% | | |
| Accuracy | % correct | >99% | | |
| Validity | % valid | >99% | | |
| Consistency | Cross-source | >99% | | |
| Uniqueness | % unique PK | 100% | | |
| Timeliness | Max delay | <1h | | |

## CODE QUALITY AT SCALE

| Aspect | Metric | Target | Current | Action |
|--------|--------|--------|---------|--------|
| Test Coverage | % | >80% | | |
| Cyclomatic Complexity | Max | <10 | | |
| Code Duplication | % | <5% | | |
| Documentation | % APIs | 100% | | |
| Linting | Violations | 0 | | |
| Security | Critical vulns | 0 | | |

## PHẢI TRẢ LỜI

1. Hệ thống hiện tại chịu được bao nhiêu load?
2. Điểm nghẽn đầu tiên sẽ ở đâu?
3. Cần thay đổi gì để scale x10? x100? x1000?
4. Chi phí scale tuyến tính hay exponential?
5. Có single point of failure không?
