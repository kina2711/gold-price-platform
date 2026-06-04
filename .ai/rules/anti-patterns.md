# Anti-Patterns Detection

Luôn quét và cảnh báo khi phát hiện anti-patterns theo role.

## BA Anti-Patterns
- ❌ Không có clear business problem → giải pháp tìm vấn đề
- ❌ KPIs không actionable (vanity metrics)
- ❌ Missing stakeholder alignment
- ❌ Scope creep không kiểm soát

## DA Anti-Patterns
- ❌ Nhảy vào modeling mà không EDA
- ❌ Insight không có recommendation
- ❌ Không validate data quality trước khi phân tích
- ❌ Correlation = Causation fallacy

## DE Anti-Patterns
- ❌ No idempotency trong pipeline
- ❌ No monitoring / silent failures
- ❌ Tight coupling giữa ingestion và transformation
- ❌ No data contracts → schema drift

## AE Anti-Patterns
- ❌ Wide tables thay vì star schema
- ❌ Business logic trong BI tool thay vì transformation layer
- ❌ Multiple sources of truth cho cùng 1 metric
- ❌ No documentation cho transformation logic

## Dev Anti-Patterns
- ❌ God objects / monolithic functions
- ❌ No error handling
- ❌ Hardcoded credentials
- ❌ No tests
- ❌ Over-engineering cho scale chưa cần
- ❌ Under-engineering cho scale sắp cần
