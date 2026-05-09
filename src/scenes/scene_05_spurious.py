"""
Scene 05: Spurious Correlations
Phụ trách: TV2 (Content Lead)
Thời lượng: ~2.5 phút

Nội dung:
- Ví dụ "Cow on Grass" — spurious vs causal features
- Causal graph: confounder visualization
- Câu hỏi: Làm sao tránh spurious correlations?
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.math_helpers import *


class SpuriousScene(Scene):
    """TODO: TV2 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Spurious Correlations", "Tương quan giả — bẫy của Machine Learning")

        # TODO: Implement
        # 1. Training panels: cow+grass → cow, camel+desert → camel
        # 2. Model learns: grass → cow (WRONG!)
        # 3. Test: cow on beach → model fails
        # 4. Causal graph: Z → X, Z → Y (confounder)
        # 5. Highlight: causal (shape) vs spurious (background)

        placeholder = Text("[ Scene 5: Spurious Correlations — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
