"""Scene 16: DRO intuition."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class DROIntuitionScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "DRO Intuition", "Tối ưu cho worst-case")
        placeholder = Text("[16] ERM objective -> DRO min sup objective", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
