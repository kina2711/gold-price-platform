---
description: Mix nhiều project lại thành 1 hybrid project hoàn chỉnh
argument-hint: <github-url-1> <github-url-2> [github-url-3...]
---

Thực hiện MIX PROJECT PROTOCOL (Mode 2 hoặc Mode 3).

## QUY TRÌNH

### M1 — Thu thập & phân tích từng project
- Tạo Project Profile Card cho mỗi project
- Liệt kê Component Inventory (reusable components, ratings)

### M2 — So sánh chiến lược
- Multi-Dimensional Comparison Matrix (12 dimensions)
- Trade-off Analysis (4 options: Project A / B / Hybrid / Build mới)
- Compatibility Assessment (tech stack, data model, dependencies)

### M3 — Thiết kế Hybrid Architecture
- Component Selection Matrix (final decision: lấy gì từ đâu)
- Hybrid Architecture Blueprint (layer-by-layer)
- Risk Assessment (likelihood × impact)

### M4 — Unified Rebuild Roadmap
- ⛔ DỪNG LẠI — chờ user xác nhận hybrid architecture + roadmap

## KEY RULES

- KHÔNG copy-paste — luôn refactor
- Define contracts trước (API, data, event)
- Giải quyết compatibility sớm
- Test từng component riêng trước khi integrate
- Document mọi quyết định (tại sao chọn A thay B)
- Plan for rollback
