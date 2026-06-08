"""Scene 32: COVID mortality."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class COVIDMortalityScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "COVID Mortality", "Một dataset, nhiều cơ chế rủi ro")
        placeholder = Text("[32] ERM feature chart -> two subgroup mechanism charts", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
