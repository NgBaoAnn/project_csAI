# Data Heterogeneity & OOD Generalization — 3B1B Style Video

Video giải thích trực quan theo phong cách **3Blue1Brown** cho tutorial tại CoLLAs 2024 của Peng Cui & Jiashuo Liu.

**Tutorial nguồn:**
- [Part 1](https://www.youtube.com/watch?v=_kJtrMFfSJc) — Foundations
- [Part 2](https://www.youtube.com/watch?v=vHfv2ZXSWvU) — Advanced Methods

## Quick Start

```bash
# Clone & setup
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# Render scene mẫu
cd src
manim -ql scenes/scene_01_accuracy_fail.py AccuracyFailScene -p
```

## Tài Liệu

| File | Nội dung |
|------|---------|
| [docs/00_project_overview.md](docs/00_project_overview.md) | Tổng quan: chủ đề, khái niệm cốt lõi, datasets, reading list |
| [docs/01_production_plan.md](docs/01_production_plan.md) | Timeline, phân công 4 thành viên, Git workflow |
| [docs/02_video_script.md](docs/02_video_script.md) | Kịch bản chi tiết 40 scene, ~67 phút: narration, cue Manim, transition |
| [docs/03_technical_guide.md](docs/03_technical_guide.md) | Cài đặt Manim, style guide, code patterns, troubleshooting |
| [docs/04_research_report.md](docs/04_research_report.md) | **Deep research:** IRM/DRO/Stable Learning formulations, benchmarks, bibliography |

## Phân Công Nhanh Theo Kịch Bản Mới

| TV | Scenes | Vai trò phụ |
|----|--------|------------|
| TV1 | 1-10 | Tech setup, utils, code review |
| TV2 | 11-20 | Script, storyboard, content accuracy |
| TV3 | 21-30 | math_helpers.py, animation polish toàn bộ |
| TV4 | 31-40 | Voiceover, video editing, final export |

> Video mới dùng 40 scene ngắn. Scene thường dài 85-100 giây; scene có công thức hoặc ví dụ quan trọng dài 100-110 giây; kết luận dài hơn một chút. Tổng thời lượng mục tiêu khoảng 65-68 phút.
