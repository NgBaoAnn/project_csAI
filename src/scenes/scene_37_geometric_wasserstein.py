"""Scene 37: Geometric Wasserstein."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class GeometricWassersteinScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Geometric Wasserstein", "Robustness đi theo data manifold")
        placeholder = Text("[37] Graph neighborhood, manifold transport, avoid outlier", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
