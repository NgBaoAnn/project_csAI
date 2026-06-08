"""Scene 17: Uncertainty set."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class UncertaintySetScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Uncertainty Set", "Worst-case nằm trong vùng nào?")
        placeholder = Text("[17] Ball quanh P_train, slider rho", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
