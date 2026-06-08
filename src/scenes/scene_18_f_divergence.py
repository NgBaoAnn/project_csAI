"""Scene 18: f-divergence."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class FDivergenceScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "f-divergence", "Shift bằng reweighting")
        placeholder = Text("[18] Density ratio dQ/dP; 70/30 -> 40/60", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
