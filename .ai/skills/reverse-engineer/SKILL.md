---
name: reverse-engineer
description: Reverse engineer project theo FAANG methodology — từ Business Problem đến Rebuild Roadmap
---

# Reverse Engineer Skill

## INPUT
- GitHub URL hoặc source code path
- (Optional) Business context, dataset/schema

## QUY TRÌNH THỰC HIỆN

### Bước 1.1 — Business Problem Framework (6 câu hỏi)
1. What business problem exists?
2. Why is it important?
3. What is the business impact?
4. What decisions need to be made?
5. What data is required?
6. What metrics measure success?

→ Chưa trả lời được = DỪNG LẠI hỏi user.

### Bước 1.2 — Business Analysis
- Business Problem & Objective
- Stakeholder Analysis (Stakeholder / Objective / KPI / Data Needs)
- Decision Framework

### Bước 1.3 — Tech Stack Analysis
Liệt kê: Language, Framework, Database, Cache, Queue, Infra, Analytics, BI, CI/CD, Monitoring, Testing
Đánh giá từ 5 role: BA, DA, DE, AE, Dev

### Bước 1.4 — Data Architecture
Source → Ingestion → Raw Storage → Transform → Curated → Serving
Đánh giá: Reliability, Scalability, Data Quality, Governance, Cost

### Bước 1.5 — System Architecture
Frontend → API → Services → DB → Analytics → Monitoring
Đánh giá: Bottlenecks, Failure Points, Security, Performance, Availability

### Bước 1.6 — Rebuild Roadmap (5-7 milestones)
Chọn template: Data-Heavy / Full-Stack / ML / Analytics-BI / Hybrid
Mỗi milestone: Objective, Deliverables, Definition of Done, Effort, Dependencies

### Bước 1.7 — ⛔ MANDATORY STOP
Yêu cầu user xác nhận trước khi tiếp tục.
