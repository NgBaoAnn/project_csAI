"""Scene 14: Average risk hides worst groups."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class AverageRiskScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Average Risk", "95% có thể che giấu 43%")
        placeholder = Text("[14] Bar chart majority/minority/worst group", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
