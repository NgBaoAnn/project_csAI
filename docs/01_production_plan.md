# Kế Hoạch Sản Xuất & Phân Công

## Timeline Tổng Quan

| Phase | Ngày | Công việc | Deliverable |
|-------|------|----------|------------|
| **0. Setup** | 1–2 | Cài môi trường, test render, đọc docs | Mọi người render được scene mẫu |
| **1. Script** | 3–7 | Nghiên cứu chủ đề, viết narration, vẽ storyboard | Kịch bản + storyboard đã review |
| **2. Prototype** | 8–12 | Code scene skeleton, low-quality render, peer review | Tất cả scenes chạy được `-ql` |
| **3. Production** | 13–22 | Polish animation, LaTeX formulas, transitions | Tất cả scenes render `-qh` 1080p |
| **4. Assembly** | 23–26 | Thu âm voiceover, ghép video, nhạc nền, subtitles | Draft video v1 |
| **5. Finalize** | 27–28 | Sửa feedback, export final, nộp bài | Final MP4 + source code |

### Checkpoint họp nhóm
- **Ngày 7** — Review script & storyboard (tất cả cùng xem)
- **Ngày 12** — Review prototype animations (online)
- **Ngày 20** — Review production scenes (online)
- **Ngày 25** — Xem draft video (offline nếu được)

---

## Phân Công 4 Thành Viên

> **Cập nhật theo kịch bản mới:** video mục tiêu dài khoảng **50 phút**, vẫn chia thành **40 scene ngắn**. Scene thường dài 65-75 giây; scene có công thức hoặc ví dụ quan trọng dài 80-85 giây; scene kết luận khoảng 100 giây.

### TV1 — Tech Lead
**Scenes:** 1-10 (Hook, i.i.d., shift taxonomy, heterogeneity foundations)  
**Vai trò phụ:**
- Setup repo, `manim.cfg`, `requirements.txt`, Git branching
- Viết & maintain `utils/theme.py` và `utils/components.py`
- Code review tất cả PRs trước khi merge

**Đọc trước:**
- Manim Community Docs (Quickstart, Scene, MathTex)
- Survey paper: "Towards OOD Generalization" (Shen et al.)

---

### TV2 — Content Lead
**Scenes:** 11-20 (hidden subpopulations, pipeline view, ERM, spurious, DRO foundations)  
**Vai trò phụ:**
- Viết narration script hoàn chỉnh cho **toàn bộ** video
- Vẽ storyboard sơ bộ cho tất cả scenes
- Kiểm tra tính chính xác nội dung so với tutorial gốc

**Đọc trước:**
- Tutorial video Part 1 (xem kỹ, note concepts)
- "Heterogeneous Risk Minimization" (Liu et al.)
- Waterbirds / ColoredMNIST dataset descriptions

---

### TV3 — Animation Lead
**Scenes:** 21-30 (IRM, CLIP, inductive approach, mutual information, predictive heterogeneity)  
**Vai trò phụ:**
- Viết `utils/math_helpers.py` (data clouds, causal graphs, decision boundaries)
- Polish animation quality cho **toàn bộ** video sau khi TV1/TV2 xong
- Code smooth transitions giữa các scenes

**Đọc trước:**
- "Invariant Risk Minimization" — Arjovsky et al. (2019)
- "Distributionally Robust Neural Networks" — Sagawa et al. (2020)
- Manim docs: Advanced animations, Graph, 3D scenes

---

### TV4 — Production Lead
**Scenes:** 31-40 (case studies, HRM, geometry-aware DRO, evaluation, deployment, conclusion)  
**Vai trò phụ:**
- Thu âm voiceover (hoặc organize nhóm thu)
- Ghép video: sync audio, thêm nhạc nền, subtitles
- Export final & quality check

**Đọc trước:**
- Tutorial video Part 2 (phần stable learning, causal inference)
- "Stable Prediction across Unknown Environments" (Kuang et al.)
- DaVinci Resolve basics (video editing, audio sync)

---

## Phân Chia Công Bằng

| | Scenes (thời lượng) | Vai trò phụ | Tổng load |
|---|---|---|---|
| TV1 | 10 scenes (~12:25) | Setup + utils + code review | ●●●● |
| TV2 | 10 scenes (~12:30) | Toàn bộ script + storyboard + content QA | ●●●● |
| TV3 | 10 scenes (~12:30) | Math helpers + polish toàn bộ animations | ●●●● |
| TV4 | 10 scenes (~12:35) | Voiceover + toàn bộ video editing | ●●●● |

> Load được cân bằng theo cụm 10 scene/người. TV1 giữ foundations, TV2 giữ ERM/DRO foundations, TV3 giữ IRM/inductive/predictive heterogeneity, TV4 giữ case studies/evaluation/conclusion.

## Scene Map Theo Kịch Bản Mới

| Scene | Nội dung | TV | Thời lượng |
|---|---|---|---|
| 1-10 | Hook, i.i.d., shift taxonomy, heterogeneity foundations | TV1 | ~12:25 |
| 11-20 | Subpopulations, ERM, spurious, DRO foundations | TV2 | ~12:30 |
| 21-30 | IRM, CLIP, inductive approach, predictive heterogeneity | TV3 | ~12:30 |
| 31-40 | Case studies, HRM, geometry, evaluation, conclusion | TV4 | ~12:35 |
| **Tổng** |  |  | **~50:00** |

---

## Git Workflow

```
main
├── feature/tv1/foundations       # TV1: scene 1-10 + utils
├── feature/tv2/erm-dro           # TV2: scene 11-20
├── feature/tv3/irm-predictive    # TV3: scene 21-30 + animation polish
└── feature/tv4/pipeline-final    # TV4: scene 31-40 + production
```

**Quy trình:**
1. Làm trên branch của mình
2. Tạo PR → assign TV1 review
3. Cần ít nhất 1 approval mới merge vào `main`
4. Không commit trực tiếp lên `main`

---

## Rủi Ro & Cách Xử Lý

| Rủi ro | Giải pháp |
|--------|-----------|
| Manim render chậm | Chỉ dùng `-qh` khi final; dev luôn dùng `-ql` |
| LaTeX không hoạt động | `pip install latex` fallback, hoặc dùng `Text()` tạm thời |
| Merge conflict | Mỗi người làm file riêng; code chung chỉ ở `utils/` |
| Thành viên bận/trễ | Buffer 2 ngày cuối Phase 3; thông báo sớm trong group chat |
| Voiceover không đạt chất lượng | Thu thử ở ngày 22, còn 4 ngày để re-record nếu cần |
