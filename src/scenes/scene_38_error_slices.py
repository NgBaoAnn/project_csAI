"""Scene 38: Error slices."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class ErrorSlicesScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Error Slices", "Model yếu ở vùng dữ liệu nào?")
        placeholder = Text("[38] Accuracy 95% breaks into slices, worst slice highlighted", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
