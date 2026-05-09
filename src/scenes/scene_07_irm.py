"""
Scene 07: IRM — Invariant Risk Minimization
Phụ trách: TV3 (Animation Lead)
Thời lượng: ~3.5 phút

Nội dung:
- Multi-environment visualization
- Invariant representation Φ
- Same classifier w across all environments
- IRMv1 gradient penalty
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class IRMScene(Scene):
    """TODO: TV3 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Invariant Risk Minimization", "Tìm features bất biến qua environments")

        # TODO: Implement
        # 1. 3 environments với data distributions
        # 2. Representation Φ(x): transform vào feature space
        # 3. KEY: same classifier w optimal ở MỌI envs
        # 4. Spurious features fade out, causal features glow
        # 5. Formula: IRM objective + IRMv1 gradient penalty
        # 6. Pros & Cons summary

        placeholder = Text("[ Scene 7: IRM — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
