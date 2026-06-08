"""Scene 13: ERM formula."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class ERMFormulaScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "ERM Formula", "Loss trung bình trên training data")
        placeholder = Text("[13] Build min_theta 1/n sum L(f_theta(x_i), y_i)", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
