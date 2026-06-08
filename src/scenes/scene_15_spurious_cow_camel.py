"""Scene 15: Spurious cow/camel."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class SpuriousCowCamelScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Spurious Correlation", "Bò, lạc đà, và background")
        placeholder = Text("[15] Background glow red; shape glow green", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
