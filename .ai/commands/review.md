---
description: Multi-role review (BA/DA/DE/AE/Dev) cho code changes hiện tại
---

Review code changes từ góc nhìn 5 roles đồng thời.

## BA Review
- Business requirement nào được đáp ứng?
- Stakeholder nào được phục vụ?
- KPI nào bị ảnh hưởng?

## DA Review
- Data quality impact?
- Analytics readiness?
- Metric definitions clear?

## DE Review
- Pipeline reliability?
- Scalability (x10, x100, x1000)?
- Fault tolerance?
- Idempotency?

## AE Review
- Data model correctness?
- Semantic layer impact?
- Single Source of Truth maintained?

## Dev Review
- Code quality (SOLID, DRY)?
- Security considerations?
- Testing coverage?
- Technical debt introduced?
- Performance acceptable?

## DECISION INTELLIGENCE

Mọi finding phải trả lời:
1. So What?
2. Why Should Anyone Care?
3. What Decision Can Be Made?
4. What Happens If We Ignore It?
