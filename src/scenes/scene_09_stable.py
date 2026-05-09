"""
Scene 09: Stable Learning & Causal Inference
Phụ trách: TV4 (Production Lead)
Thời lượng: ~2.5 phút

Nội dung:
- Causal graph (SCM)
- Causal features vs confounders
- Connection: Causality ↔ Invariance ↔ Stability
- Tổng hợp pipeline
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class StableLearningScene(Scene):
    """TODO: TV4 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Stable Learning", "Nhìn từ góc nhân quả")

        # TODO: Implement
        # 1. Causal graph: X₁ → Y, Z → X₁, Z → X₂ → Y
        # 2. Cross out spurious path, highlight causal path
        # 3. Connection triangle: Causality-Invariance-Stability
        # 4. Pipeline: Data → Partition → Learn → Evaluate

        placeholder = Text("[ Scene 9: Stable Learning — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
