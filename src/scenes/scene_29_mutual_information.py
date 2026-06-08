"""Scene 29: Mutual information."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class MutualInformationScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Mutual Information", "Information = uncertainty reduction")
        placeholder = Text("[29] H(Y), H(Y|X), I(X;Y) = H(Y) - H(Y|X)", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
