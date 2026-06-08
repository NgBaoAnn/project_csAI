"""Scene 19: Wasserstein."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class WassersteinScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Wasserstein", "Optimal transport và geometry")
        placeholder = Text("[19] Move probability mass with transport cost", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
