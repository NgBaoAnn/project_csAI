"""Scene 25: More data is not right data."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class MoreDataNotRightDataScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "More Data?", "Không đồng nghĩa với right data")
        placeholder = Text("[25] Data mountain, target shift outside coverage", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
