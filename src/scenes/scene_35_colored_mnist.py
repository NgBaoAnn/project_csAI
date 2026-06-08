"""Scene 35: ColoredMNIST."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class ColoredMNISTScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "ColoredMNIST", "Màu hay hình dạng là signal ổn định?")
        placeholder = Text("[35] Color spurious, shape stable; test correlation inversion", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
