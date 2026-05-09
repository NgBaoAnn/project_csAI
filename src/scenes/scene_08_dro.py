"""
Scene 08: DRO — Distributionally Robust Optimization
Phụ trách: TV3 (Animation Lead)
Thời lượng: ~3 phút

Nội dung:
- ERM vs DRO (average vs worst-case)
- Wasserstein ball / Uncertainty set
- Min-max game visualization
- Comparison: ERM vs IRM vs DRO
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class DROScene(Scene):
    """TODO: TV3 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Distributionally Robust Optimization", "Tối ưu cho trường hợp xấu nhất")

        # TODO: Implement
        # 1. Bar chart: ERM (average) vs DRO (worst-case)
        # 2. Uncertainty set: Wasserstein ball quanh training dist
        # 3. Min-max game: θ minimize, Q maximize
        # 4. Group DRO: maximize worst-group accuracy
        # 5. Comparison table: ERM vs IRM vs DRO

        placeholder = Text("[ Scene 8: DRO — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
