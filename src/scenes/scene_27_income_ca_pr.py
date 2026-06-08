"""Scene 27: Income prediction CA -> PR."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class IncomeCAPRScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Income Prediction", "California -> Puerto Rico")
        placeholder = Text("[27] X-shift và Y|X-shift cùng góp phần vào performance drop", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
