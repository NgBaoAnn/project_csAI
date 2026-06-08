"""Scene 39: Stability and feature sensitivity."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class StabilityFeatureScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Stability", "Robust với shift nào, feature nào?")
        placeholder = Text("[39] Distance to failure set + feature sensitivity sliders", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
