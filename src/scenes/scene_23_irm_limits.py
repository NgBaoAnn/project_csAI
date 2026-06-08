"""Scene 23: IRM limits."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class IRMLimitsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "IRM Limits", "Bad environments -> bad invariance")
        placeholder = Text("[23] Spurious correlation giống nhau trong train trông như invariant", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
