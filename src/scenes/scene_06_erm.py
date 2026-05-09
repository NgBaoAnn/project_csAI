"""
Scene 06: ERM — Empirical Risk Minimization
Phụ trách: TV2 (Content Lead)
Thời lượng: ~2.5 phút

Nội dung:
- ERM formula animation
- Loss landscape visualization
- Subgroup performance gap
- ERM absorbs ALL correlations
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class ERMScene(Scene):
    """TODO: TV2 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Empirical Risk Minimization", "Baseline — và tại sao nó không đủ")

        # TODO: Implement
        # 1. ERM formula: min (1/n) Σ L(f(x), y) — animate parts
        # 2. Loss landscape: gradient descent animation
        # 3. Bar chart: subgroup performance (A=98%, B=72%, C=45%)
        # 4. Insight: "ERM optimizes AVERAGE → ignores minorities"

        placeholder = Text("[ Scene 6: ERM — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
