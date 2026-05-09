# Data Heterogeneity & OOD Generalization — Project Overview

> **Môn:** Cơ sở Trí tuệ Nhân tạo | **Video style:** 3Blue1Brown | **Tool:** Manim Community

---

## Chủ Đề & Nguồn Gốc

Tutorial tại **CoLLAs 2024** (Conference on Lifelong Learning Agents) do **Peng Cui** và **Jiashuo Liu** (Tsinghua University) trình bày — nhóm nghiên cứu đứng sau NICO dataset và bộ "Stable Learning" papers.

| | Link |
|---|---|
| Tutorial Part 1 | https://www.youtube.com/watch?v=_kJtrMFfSJc |
| Tutorial Part 2 | https://www.youtube.com/watch?v=vHfv2ZXSWvU |
| Manim Community | https://github.com/ManimCommunity/manim |

---

## Bức Tranh Lớn: Vấn Đề Cần Giải Quyết

### Giả Định Nền Tảng Đang Vỡ

Machine Learning truyền thống dựa trên **giả định i.i.d.**: dữ liệu train và test được lấy từ cùng một phân phối xác suất. Khi giả định này đúng, **Empirical Risk Minimization (ERM)** — tối thiểu hóa loss trung bình — hoạt động tốt.

Nhưng dữ liệu thực tế luôn **heterogeneous**: đến từ nhiều nguồn, nhiều môi trường, nhiều thời điểm. Hậu quả của việc bỏ qua điều này:

- Model bám vào **spurious correlations** (tương quan giả, không ổn định) thay vì causal features
- Thất bại nghiêm trọng khi **distribution shift** xảy ra ngoài thực tế
- Kết quả thiếu công bằng với **nhóm thiểu số** (worst-group accuracy thấp)
- Kết luận khoa học sai (**false scientific discoveries**)

### Ba Hướng Tiếp Cận (Narrative Arc Của Video)

Tutorial của Peng Cui & Liu đề xuất nhìn nhận vấn đề theo **Stable Learning trilogy**:

```
Heterogeneity-aware ML
        ↑
┌───────────────────────────────┐
│ 1. INVARIANCE  │ 2. CAUSALITY │ 3. HETEROGENEITY │
│  (IRM, DRO)   │(Stable Learn)│  (Taxonomy, Env)  │
└───────────────────────────────┘
        ↑
  Ba hướng khác nhau — một đích đến:
  AI đáng tin cậy trên dữ liệu thực tế
```

---

## Các Khái Niệm Cốt Lõi

### Chuỗi Logic (Thứ Tự Video)

```
[1] i.i.d. Assumption — giả định nền tảng
      ↓ BỊ VỠ KHI
[2] Distribution Shift (Covariate / Label / Concept)
      ↓ VÌ SAO?
[3] Data Heterogeneity — dữ liệu từ nhiều environments
      ↓ HẬU QUẢ LÀ
[4] Spurious Correlations — model học sai thứ
      ↓ ERM KHÔNG ĐỦ VÌ
[5] ERM chỉ optimize average, bỏ qua heterogeneity

—————— GIẢI PHÁP (3 hướng) ——————

[6] IRM: Invariant Risk Minimization
    → Tìm features BẤT BIẾN qua environments (Invariance)

[7] DRO: Distributionally Robust Optimization
    → Tối ưu cho trường hợp XẤU NHẤT (Robustness)

[8] Stable Learning
    → Loại bỏ confounders, chỉ giữ CAUSAL features (Causality)

—————— KẾT ——————

[9] So sánh, benchmarks, future directions
```

### Bảng Khái Niệm Kỹ Thuật

| Khái niệm | Định nghĩa chính xác | Ví dụ trực quan |
|-----------|---------------------|----------------|
| **i.i.d.** | `P_train(X,Y) = P_test(X,Y)` | Train & test cùng phân phối |
| **Covariate Shift** | `P(X)` thay đổi, `P(Y\|X)` giữ | Ảnh ban ngày → ban đêm |
| **Label Shift** | `P(Y)` thay đổi | Tỷ lệ bệnh nhân khác nhau theo quốc gia |
| **Concept Drift** | `P(Y\|X)` thay đổi | Định nghĩa "spam" tiến hóa theo thời gian |
| **Spurious Correlation** | Pattern dự đoán đúng trong train nhưng **không có quan hệ nhân quả** với Y | Bò luôn trên cỏ → model học: cỏ = bò |
| **Environment** | Nhóm dữ liệu cùng điều kiện/nguồn gốc | Hospital A, Hospital B, Hospital C |
| **ERM** | `min_θ (1/n) Σᵢ L(f_θ(xᵢ), yᵢ)` — minimize loss trung bình | Standard training của mọi neural net |
| **IRM** | Tìm Φ sao cho classifier `w` optimal đồng đều ở **mọi** environments | Loại bỏ features chỉ hữu ích ở 1 env |
| **Group DRO** | `min_θ max_{g} R_g(θ)` — minimize worst-group loss | Nâng hiệu suất nhóm yếu nhất |
| **Stable Learning** | Reweight samples để features trở nên **độc lập** (decorrelated) | Loại bỏ ảnh hưởng confounders |

---

## Các Dataset Thực Tế (Để Dẫn Chứng Trong Video)

| Dataset | Loại | Spurious feature | Causal feature | Nguồn |
|---------|------|-----------------|---------------|-------|
| **ColoredMNIST** | Synthetic | Màu sắc chữ số | Hình dạng chữ số | IRM paper |
| **Waterbirds** | Semi-synthetic | Background (nước/đất) | Loại chim (waterbird/landbird) | Group DRO paper |
| **CelebA** | Real | Giới tính (gender) | Màu tóc (blond) | Fairness research |
| **NICO/NICO++** | Real image | Context (on grass, in water) | Main object (dog, cat) | Peng Cui's lab |

> **Gợi ý cho video:** Dùng **Waterbirds** và **ColoredMNIST** làm ví dụ chính xuyên suốt — chúng trực quan nhất và có papers chi tiết.

---

## Cấu Trúc Dự Án

```
project_csAI/
├── docs/
│   ├── 00_project_overview.md    ← file này
│   ├── 01_production_plan.md     ← timeline, phân công, git workflow
│   ├── 02_video_script.md        ← kịch bản từng scene (narration + animation)
│   └── 03_technical_guide.md    ← Manim setup, style guide, code patterns
│
├── src/
│   ├── scenes/                   ← 9 scene files
│   ├── utils/
│   │   ├── theme.py              ← color palette, font sizes, timing constants
│   │   ├── components.py         ← reusable Manim components
│   │   └── math_helpers.py       ← data clouds, causal graphs, decision boundaries
│   └── assets/images/, assets/svg/
│
├── output/                       ← rendered videos (gitignored)
├── requirements.txt              ← manim>=0.18.0, numpy
├── manim.cfg                     ← project-level render config
└── README.md
```

---

## Tài Liệu Đọc Trước (Phân Theo TV)

### Tất Cả Đọc (Bắt Buộc)
1. **IRM Paper** — Arjovsky et al. (2019): https://arxiv.org/abs/1907.02893  
   *→ Nền tảng lý thuyết của cả tutorial*
2. **Group DRO Paper** — Sagawa et al. (2020): https://arxiv.org/abs/1911.08731  
   *→ Framework thực tế và benchmark thiết yếu*
3. **OOD Survey** — Shen et al. (2021): https://arxiv.org/abs/2108.13624  
   *→ Cái nhìn tổng quan, giúp hiểu bức tranh lớn*

### TV1 (Scenes 1-3: Foundations)
- 3B1B "But what is a Neural Network?" → phân tích structure narration
- Manim Community Quickstart: https://docs.manim.community/en/stable/tutorials/quickstart.html

### TV2 (Scenes 4-6: Heterogeneity, Spurious, ERM)
- NICO dataset paper: https://arxiv.org/abs/2101.10943  
- Waterbirds/Group DRO GitHub: https://github.com/kohpangwei/group_DRO

### TV3 (Scenes 7-8: IRM, DRO)
- IRM paper (đọc kỹ Sections 3-4 về bi-level optimization)
- "Risks of Invariant Risk Minimization" — biết limitations: https://arxiv.org/abs/2010.05761
- Manim Advanced: https://docs.manim.community/en/stable/reference.html

### TV4 (Scenes 9-10: Stable Learning, Conclusion)
- Stable Prediction paper: https://arxiv.org/abs/1905.11374
- StableNet (deep learning version): https://arxiv.org/abs/2005.05007
- DaVinci Resolve basics (free) hoặc CapCut cho video assembly

---

## Tech Stack

| Tool | Mục đích | Cài đặt |
|------|---------|---------|
| Python 3.10+ | Runtime | python.org |
| Manim Community ≥0.18 | Animation engine | `pip install manim` |
| LaTeX (TeX Live / MiKTeX) | Render công thức | miktex.org |
| FFmpeg | Video encoding (Manim tự dùng) | ffmpeg.org |
| DaVinci Resolve | Video editing & assembly | blackmagicdesign.com (miễn phí) |
