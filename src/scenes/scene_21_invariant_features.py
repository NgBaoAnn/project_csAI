"""Scene 21: Invariant features."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class InvariantFeaturesScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Invariant Features", "Feature nào còn đúng khi environment đổi?")
        placeholder = Text("[21] Cow/camel qua nhiều backgrounds; shape ổn định", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
