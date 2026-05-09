"""
Scene 02: i.i.d. Assumption
Phụ trách: TV1 (Team Lead)
Thời lượng: ~2 phút

Nội dung:
- Giải thích giả định i.i.d.
- Visualize train/test distributions overlap
- Khi distributions khác nhau → model thất bại
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class IIDScene(Scene):
    """TODO: TV1 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "i.i.d. Assumption", "Giả định quan trọng nhất của ML")

        # TODO: Implement
        # 1. Vẽ 2 data clouds overlap → "Same distribution"
        # 2. Equation: P_train(X,Y) = P_test(X,Y)
        # 3. Animation: clouds tách ra → "Different distribution"
        # 4. Accuracy counter drop: 95% → 60%

        placeholder = Text("[ Scene 2: i.i.d. — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
