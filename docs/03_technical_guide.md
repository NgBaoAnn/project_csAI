# Hướng Dẫn Kỹ Thuật Manim

> **Phiên bản target:** Manim Community Edition ≥ 0.18  
> **Lưu ý quan trọng:** Đừng dùng tutorials YouTube trước 2023 — nhiều API đã thay đổi.  
> **Tài liệu gốc:** https://docs.manim.community/

---

## 1. Cài Đặt Môi Trường

### macOS
```bash
brew install ffmpeg
brew install --cask mactex-no-gui   # LaTeX ~4GB, chờ lâu

python3 -m venv venv
source venv/bin/activate
pip install manim

# Kiểm tra
manim checkhealth
```

### Windows
```powershell
# 1. Cài FFmpeg: https://ffmpeg.org/download.html → thêm vào PATH
# 2. Cài MiKTeX: https://miktex.org/download

python -m venv venv
venv\Scripts\activate
pip install manim
```

### Ubuntu/Debian
```bash
sudo apt install ffmpeg texlive-full
python3 -m venv venv && source venv/bin/activate
pip install manim
```

### Kiểm Tra
```bash
manim checkhealth   # Kiểm tra FFmpeg, LaTeX, Python version
manim --version     # Expected: Manim Community v0.18.x hoặc cao hơn
```

---

## 2. Vòng Lặp Phát Triển

```bash
cd src/

# Dev (nhanh, 480p 15fps) — LUÔN dùng khi code
manim -pql scenes/scene_01_accuracy_fail.py AccuracyFailScene

# Review với nhóm (720p 30fps)
manim -pqm scenes/scene_01_accuracy_fail.py AccuracyFailScene

# Final render (1080p 60fps) — CHỈ khi xong hoàn toàn
manim -pqh scenes/scene_01_accuracy_fail.py AccuracyFailScene

# Render một đoạn cụ thể (cắt thời gian)
manim -pql --from_animation 5 --upto_animation 10 scenes/scene_22_irm_objective.py IRMObjectiveScene
```

| Flag | Resolution | FPS | Dùng khi |
|------|-----------|-----|---------|
| `-ql` | 854×480 | 15 | Code, debug, thử nghiệm |
| `-qm` | 1280×720 | 30 | Review với nhóm |
| `-qh` | 1920×1080 | 60 | Final render |
| `-qk` | 3840×2160 | 60 | 4K (nếu cần) |

---

## 3. 3Blue1Brown Style Guide

### Ba Nguyên Tắc Cốt Lõi (Từ Grant Sanderson)
1. **Mystery trước, Definition sau** — Không bao giờ bắt đầu bằng định nghĩa. Đặt câu hỏi, xây dựng intuition, RỒII định nghĩa mới xuất hiện như kết luận tự nhiên.
2. **Visual và Narration phải đồng bộ** — Mỗi thứ trên màn hình phải nói cùng điều narration đang nói. Nếu không, người xem bị split attention.
3. **Rediscoverability** — Thiết kế sao cho người xem nghĩ *"tôi cũng có thể nghĩ ra điều đó"*.

### Color Palette (Import từ `utils/theme.py`)
```python
# Background
BG_DARK     = "#1a1a2e"    # Nền chính — dark navy (3B1B signature)

# Primary colors
BLUE_3B1B   = "#3b82f6"    # Environment 1, primary elements
AMBER_3B1B  = "#f59e0b"    # Environment 2, highlights, warnings
ORANGE_3B1B = "#f97316"    # Environment 3
EMERALD_3B1B= "#10b981"    # Causal features ✓, correct
RED_3B1B    = "#ef4444"    # Spurious features ✗, wrong, error
PURPLE_3B1B = "#8b5cf6"    # Formulas, math emphasis

# Text
TEXT_MAIN   = "#e2e8f0"    # Body text, labels
TEXT_DIM    = "#94a3b8"    # Captions, secondary info
```

### Typography
```python
FONT_MAIN = "Inter"     # Tất cả text — cần cài Inter font

SIZE_TITLE   = 56       # Scene title
SIZE_SECTION = 44       # Section headers
SIZE_BODY    = 32       # Narration, explanations
SIZE_CAPTION = 24       # Labels, small annotations
SIZE_FORMULA = 40       # MathTex formulas
```

### Timing (Giữ Nhất Quán)
```python
T_FAST   = 0.4    # Transition nhanh giữa states
T_NORMAL = 1.0    # Animation tiêu chuẩn
T_SLOW   = 2.0    # Reveal quan trọng
T_PAUSE  = 1.5    # Sau key point — để "sink in"
T_LONG   = 3.0    # Major concept reveal
```

---

## 4. Code Patterns Thiết Yếu

### Template Scene (Copy cho mọi scene)
```python
from manim import *
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.theme import *
from utils.components import setup_dark_scene

# Set background COLOR trước class definition (chuẩn Manim CE 2024)
config.background_color = BG_DARK

class SceneNameHere(Scene):
    """
    Scene X: [Tên Scene]
    Author: TV[N]
    Duration: ~[X] phút
    """
    def construct(self):
        # --- [Scene logic ở đây] ---
        pass
```

### MathTex — Cách Đúng (2024)
```python
# ❌ SAI — không animate được từng phần
formula = MathTex(r"\min_\theta \frac{1}{n} \sum_i L(f_\theta(x_i), y_i)")

# ✅ ĐÚNG — dùng {{ }} để tạo submobjects
formula = MathTex(
    r"{{\min_\theta}}",      # [0] — có thể target riêng
    r"\frac{1}{n}",          # [1]
    r"\sum_i",               # [2]
    r"L(f_\theta(x_i), y_i)" # [3]
)

# Animate từng phần
self.play(FadeIn(formula[0]))
self.play(Write(formula[1]))
self.play(FadeIn(formula[2:]))  # Phần còn lại cùng lúc

# Tô màu phần cụ thể
formula[1].set_color(AMBER_3B1B)  # Highlight "average"

# Transform formula này thành formula khác (matching tokens)
formula2 = MathTex(r"{{\min_\theta}}", r"\max_Q", r"E_Q[L(\theta)]")
self.play(TransformMatchingTex(formula, formula2))
```

### Data Points Scatter
```python
import numpy as np

def make_environment_cloud(center, n=40, std=0.6, color=BLUE_3B1B, seed=0):
    """Tạo cluster điểm dữ liệu cho 1 environment"""
    np.random.seed(seed)
    return VGroup(*[
        Dot(
            point=[center[0] + np.random.normal(0, std),
                   center[1] + np.random.normal(0, std), 0],
            color=color,
            radius=0.07
        )
        for _ in range(n)
    ])

# Tạo 3 environments
env1 = make_environment_cloud([-3, 1], color=BLUE_3B1B, seed=1)
env2 = make_environment_cloud([0, -1], color=AMBER_3B1B, seed=2)
env3 = make_environment_cloud([3, 1], color=ORANGE_3B1B, seed=3)

# Animate vào từ từ (stagger)
self.play(
    LaggedStart(
        *[FadeIn(d, scale=0.3) for d in env1],
        *[FadeIn(d, scale=0.3) for d in env2],
        *[FadeIn(d, scale=0.3) for d in env3],
        lag_ratio=0.02
    ),
    run_time=2.0
)
```

### Causal Graph
```python
# Dùng Graph của Manim
vertices = ["Z", "X_c", "X_s", "Y"]
edges = [("Z", "X_c"), ("Z", "X_s"), ("X_c", "Y"), ("X_s", "Y")]

# Positions thủ công
layout = {
    "Z": [0, 2, 0],
    "X_c": [-2, 0, 0],
    "X_s": [2, 0, 0],
    "Y": [0, -2, 0]
}

graph = Graph(
    vertices, edges,
    layout=layout,
    vertex_config={
        "Z":   {"fill_color": AMBER_3B1B},
        "X_c": {"fill_color": EMERALD_3B1B},
        "X_s": {"fill_color": RED_3B1B},
        "Y":   {"fill_color": BLUE_3B1B},
    },
    edge_config={
        ("X_s", "Y"): {"stroke_color": RED_3B1B, "stroke_width": 2},
    }
)

labels = {v: MathTex(v, font_size=SIZE_CAPTION) for v in vertices}
self.play(Create(graph))

# "Gạch bỏ" spurious path
spurious_edge = graph.edges[("X_s", "Y")]
cross = Cross(spurious_edge, stroke_color=RED_3B1B, stroke_width=4)
self.play(Create(cross))
```

### Modern `.animate` Syntax (Tránh dùng method cũ)
```python
# ❌ Cũ — không chain được
self.play(my_obj.shift(RIGHT * 2))
self.play(my_obj.set_color(EMERALD_3B1B))

# ✅ Mới — chain được, idiomatic 2024
self.play(
    my_obj.animate.shift(RIGHT * 2).set_color(EMERALD_3B1B),
    run_time=T_NORMAL
)

# Group animation với stagger
items = [Text(str(i)) for i in range(5)]
self.play(
    LaggedStart(*[FadeIn(item, shift=UP * 0.3) for item in items],
                lag_ratio=0.2),
    run_time=2.0
)
```

### Bar Chart Với Highlight
```python
chart = BarChart(
    values=[98, 71, 43],
    bar_names=["Majority\n(85%)", "Minority A\n(10%)", "Minority B\n(5%)"],
    bar_colors=[BLUE_3B1B, AMBER_3B1B, RED_3B1B],
    y_range=[0, 100, 25],
    y_length=4,
    x_length=8,
)
self.play(Create(chart))

# Highlight bar cuối (worst group)
worst_bar = chart.bars[-1]
brace = Brace(worst_bar, DOWN, color=RED_3B1B)
label = brace.get_text("Worst group: 43%", buff=0.1).set_color(RED_3B1B)
self.play(GrowFromCenter(brace), Write(label))
```

---

## 5. Checklist Trước Khi Tạo PR

**Style:**
- [ ] `config.background_color = BG_DARK` ở đầu file (không hardcode màu)
- [ ] Tất cả màu import từ `utils/theme.py` — không dùng `RED`, `BLUE` trực tiếp của Manim
- [ ] Font sizes dùng constants `SIZE_*` từ theme

**Animation Quality:**
- [ ] Không có object nào xuất hiện bằng `self.add()` trực tiếp (phải qua `self.play()`)
- [ ] `self.wait(T_PAUSE)` sau mỗi key moment
- [ ] Không có animation nào < 0.4s cho reveals quan trọng
- [ ] `LaggedStart` thay vì `AnimationGroup` khi nhiều objects cùng loại

**Technical:**
- [ ] `manim -ql` chạy không lỗi
- [ ] `manim -qm` chạy không lỗi (720p test)
- [ ] Docstring: scene name, TV author, estimated duration
- [ ] Không import thừa (chỉ `from manim import *` và utils)

---

## 6. Troubleshooting

| Lỗi | Nguyên nhân phổ biến | Cách sửa |
|-----|---------------------|---------|
| `LaTeX Error: File not found` | Package LaTeX chưa cài | Mở MiKTeX Console → Install package |
| `ModuleNotFoundError: manim` | Quên activate venv | `source venv/bin/activate` |
| `FileNotFoundError: ffmpeg` | FFmpeg chưa có trong PATH | Thêm FFmpeg vào PATH, restart terminal |
| Video đen hoàn toàn | `construct()` không có `self.play()` | Thêm ít nhất 1 animation |
| Render cực chậm | Dùng `-qh` khi dev | Đổi sang `-ql` |
| Font `Inter` không tìm thấy | Chưa cài Inter font | Tải từ fonts.google.com/specimen/Inter |
| `AttributeError: 'int'` trong Graph | Vertex type mismatch | Đảm bảo tất cả vertex names là strings |
| MathTex không render | LaTeX syntax error | Test trên https://latexeditor.lagrida.com/ trước |

### Debug Workflow
```bash
# 1. Kiểm tra health
manim checkhealth

# 2. Test LaTeX độc lập
python3 -c "from manim import *; MathTex(r'\min_\theta').render()"

# 3. Render chỉ phần đầu (5 animations đầu tiên)
manim -pql --from_animation 0 --upto_animation 5 scenes/scene_22_irm_objective.py IRMObjectiveScene
```

---

## 7. Links Tham Khảo

| Tài nguyên | Link |
|-----------|------|
| Manim CE Docs | https://docs.manim.community/ |
| Manim Examples Gallery | https://docs.manim.community/en/stable/examples.html |
| MathTex / LaTeX Reference | https://docs.manim.community/en/stable/reference/manim.mobject.text.tex_mobject.MathTex.html |
| Manim Discord | https://manim.community/discord/ |
| Online LaTeX Editor | https://latexeditor.lagrida.com/ |
| Inter Font | https://fonts.google.com/specimen/Inter |
