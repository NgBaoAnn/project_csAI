"""Scene 28: Ambiguity set theo biến."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class AmbiguityVariablesScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Ambiguity Variables", "Robust trên biến nào?")
        placeholder = Text("[28] Feature selector làm ambiguity set đổi shape", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
