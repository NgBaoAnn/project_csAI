"""Scene 31: Crop yield."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class CropYieldScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Crop Yield", "Biến crop type ẩn lộ ra qua prediction")
        placeholder = Text("[31] True crop type map vs learned split map", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
