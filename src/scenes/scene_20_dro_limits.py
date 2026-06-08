"""Scene 20: DRO limits."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class DROLimitsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "DRO Limits", "Worst-case có giống target thật?")
        placeholder = Text("[20] Q* mismatch Q_real; over-pessimism", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
