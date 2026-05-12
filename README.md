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
manim -ql scenes/scene_01_intro.py IntroScene -p
```

## Tài Liệu

| File | Nội dung |
|------|---------|
| [docs/00_project_overview.md](docs/00_project_overview.md) | Tổng quan: chủ đề, khái niệm cốt lõi, datasets, reading list |
| [docs/01_production_plan.md](docs/01_production_plan.md) | Timeline, phân công 4 thành viên, Git workflow |
| [docs/02_video_script.md](docs/02_video_script.md) | Kịch bản chi tiết từng scene: narration + animation (3B1B style) |
| [docs/03_technical_guide.md](docs/03_technical_guide.md) | Cài đặt Manim, style guide, code patterns, troubleshooting |
| [docs/04_research_report.md](docs/04_research_report.md) | **Deep research:** IRM/DRO/Stable Learning formulations, benchmarks, bibliography |
| [docs/06_tv2_full_narration_storyboard_accuracy.md](docs/06_tv2_full_narration_storyboard_accuracy.md) | TV2 final package: full narration 10 scenes, storyboard all scenes, transcript-based accuracy review |

## Phân Công Nhanh

| TV | Scenes | Vai trò phụ |
|----|--------|------------|
| TV1 | 1, 2, 3 | Tech setup, utils, code review |
| TV2 | 4, 5, 6 | Script, storyboard, content accuracy |
| TV3 | 7, 8 | math_helpers.py, animation polish toàn bộ |
| TV4 | 9, 10 | Voiceover, video editing, final export |
