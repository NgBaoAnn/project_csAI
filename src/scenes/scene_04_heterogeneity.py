"""
Scene 04: Data Heterogeneity
Phụ trách: TV2 (Content Lead)
Thời lượng: ~3 phút

Nội dung:
- Data heterogeneity = data từ nhiều environments
- Animation: mixed data → tách thành environments
- Key insight: "Heterogeneity is information, not noise"
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class HeterogeneityScene(Scene):
    """TODO: TV2 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Data Heterogeneity", "Đa dạng dữ liệu — chìa khóa hay rào cản?")

        # TODO: Implement
        # 1. Big pool of mixed data points (all same color)
        # 2. Animation: points re-color into 3 environments
        # 3. Labels: Hospital A, Hospital B, Hospital C
        # 4. Insight box: "Heterogeneity is INFORMATION"

        placeholder = Text("[ Scene 4: Data Heterogeneity — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
