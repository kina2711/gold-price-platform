---
name: mix-project
description: Kết hợp thành phần tốt nhất từ nhiều dự án thành hybrid project hoàn chỉnh
---

# Mix Project Skill

## INPUT
- 2+ GitHub URLs hoặc source code paths
- (Optional) Components cụ thể muốn lấy từ mỗi project
- (Optional) Vision cho hybrid project

## 3 MODES

### Mode 2: MIX PROJECT — có sẵn 2+ repos
### Mode 3: IDEA-FIRST — ý tưởng + tham chiếu repos

## QUY TRÌNH

### M1 — Project Profile Card (cho mỗi project)

| Thuộc tính | Giá trị |
|-----------|---------|
| Project Name | |
| Business Domain | |
| Project Type | Data/Full-Stack/ML/Analytics/BI/API/Other |
| Tech Stack | |

Đánh giá 7 chiều (1-5⭐): Code Quality, Data Quality, Scalability, Security, Documentation, Testing, Maintainability
Liệt kê: Strengths, Weaknesses, Anti-patterns, Reusable Components

### M1.2 — Component Inventory
```
Project A:
├── Frontend — Rating ⭐⭐⭐⭐⭐ — Reusable ✅
├── Backend — Rating ⭐⭐⭐ — Reusable ⚠️ (cần refactor)
├── Data Pipeline — Rating ⭐⭐⭐⭐ — Reusable ✅
└── ...
```

### M2 — Comparative Analysis
- 12-dimension comparison matrix
- Trade-off Analysis (4 options per dimension)
- Compatibility: Tech Stack, Data Model, Dependencies

### M3 — Hybrid Architecture
- Component Selection Matrix (Source + Lý do + Modifications + Effort + Priority)
- Architecture Blueprint (layer-by-layer diagram)
- Risk Assessment (7 risk categories)

### M4 — ⛔ MANDATORY STOP
Yêu cầu xác nhận hybrid architecture + roadmap.

## VÍ DỤ

**E-Commerce Hybrid**: ETL (Project A) + Dashboard (Project B) + DQ (build mới)
**SaaS + ML Mashup**: Events (A) + ML pipeline (B) + Streaming (C) → unified platform
**Idea-First DQ**: Great Expectations (arch) + Monte Carlo (concepts) + Custom rules → unified DQ
