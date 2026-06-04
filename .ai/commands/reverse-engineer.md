---
description: Reverse engineer một GitHub repo hoặc source code theo chuẩn FAANG
argument-hint: <github-url hoặc path-to-source>
---

Thực hiện BƯỚC 1 — BUSINESS ANALYSIS + PROJECT OVERVIEW + REBUILD ROADMAP.

## QUY TRÌNH

1. Nhận GitHub URL hoặc source code path
2. Trả lời 6 câu hỏi Business Problem Framework
3. Business Analysis (Problem, Objective, Stakeholders, Decision Framework)
4. Tech Stack Analysis (đánh giá từ 5 role: BA/DA/DE/AE/Dev)
5. Data Architecture (Source → Ingestion → Storage → Transform → Serving)
6. System Architecture (Frontend → API → Services → DB → Analytics)
7. Rebuild Roadmap (5-7 milestones)
8. ⛔ DỪNG LẠI — chờ user xác nhận roadmap

## GUARDS

- KHÔNG nhảy vào code trước Business Problem
- KHÔNG đưa full solution ngay
- PHẢI giải thích WHY trước HOW
- PHẢI đánh giá scale x10, x100, x1000
