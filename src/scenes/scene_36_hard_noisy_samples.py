"""Scene 36: Hard samples vs noisy samples."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class HardNoisySamplesScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Hard vs Noisy", "Loss cao là signal hay noise?")
        placeholder = Text("[36] Minority cluster vs isolated outlier, both high loss", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
