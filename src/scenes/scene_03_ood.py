"""
Scene 03: Out-of-Distribution Problem
Phụ trách: TV1 (Team Lead)
Thời lượng: ~2.5 phút

Nội dung:
- Định nghĩa OOD
- 3 loại distribution shift: covariate, label, concept
- Taxonomy diagram
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class OODScene(Scene):
    """TODO: TV1 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Out-of-Distribution", "Khi phân phối thay đổi")

        # TODO: Implement
        # 1. 3 panels: Covariate Shift, Label Shift, Concept Drift
        # 2. Mỗi panel: P(X), P(Y), P(Y|X) thay đổi
        # 3. Taxonomy tree summary

        placeholder = Text("[ Scene 3: OOD Problem — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
