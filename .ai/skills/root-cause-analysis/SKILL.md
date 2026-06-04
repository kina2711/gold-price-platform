---
name: root-cause-analysis
description: Phân tích Root Cause theo 5 Whys, Fishbone, Driver Tree
---

# Root Cause Analysis Skill

Không được dừng ở mô tả vấn đề. Bắt buộc đi sâu 5 levels.

## 5 WHYS METHOD

| Level | Question | Mục đích |
|-------|----------|----------|
| 1 | What happened? | Mô tả hiện tượng |
| 2 | Why? | Nguyên nhân trực tiếp |
| 3 | Why behind Why? | Nguyên nhân gốc rễ kỹ thuật |
| 4 | System Root Cause | Lỗi hệ thống / thiết kế |
| 5 | Business Root Cause | Lỗi từ business process / decision |

### Ví dụ
```
L1: Revenue trên dashboard thấp hơn thực tế 15%
L2: ETL pipeline bỏ sót transactions từ payment gateway thứ 3
L3: Pipeline chỉ handle 2 sources, không có fallback cho source mới
L4: Không có data contract / schema validation ở ingestion layer
L5: Khi thêm payment partner mới, không có process update pipeline
```
→ Short-term: fix pipeline → Medium-term: data contracts → Long-term: change management

## FISHBONE (ISHIKAWA) DIAGRAM

Phân loại theo 6 nhóm: People, Process, Technology, Data, Environment, Management

```
        People ──── Technology
           \         /
Process ── [PROBLEM] ── Data
           /         \
   Environment ── Management
```

## DRIVER TREE ANALYSIS

```
[North Star Metric]
├── [Driver 1]
│   ├── [Sub-driver 1.1] ← Root cause?
│   └── [Sub-driver 1.2]
├── [Driver 2]
│   └── [Sub-driver 2.1] ← Or here?
└── [Driver 3]
```

## OUTPUT FORMAT

Mỗi RCA phải có:
1. Problem Statement
2. 5 Whys chain
3. Root Cause Classification (People/Process/Tech/Data/Env/Mgmt)
4. Action Items (Short-term / Medium-term / Long-term)
5. Prevention Measures
