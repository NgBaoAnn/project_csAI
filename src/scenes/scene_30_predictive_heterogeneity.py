"""Scene 30: Predictive heterogeneity."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class PredictiveHeterogeneityScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Predictive Heterogeneity", "Split nào làm prediction tốt hơn?")
        placeholder = Text("[30] sup_E I_v(Y;X|E) - I_v(Y;X); good split vs bad split", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
