"""Scene 11: Hidden subpopulations."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class HiddenSubpopulationsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Hidden Subpopulations", "Một average model che giấu nhiều mechanisms")
        placeholder = Text("[11] Hai subgroup có Y|X khác nhau; line trung bình fit tệ", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
