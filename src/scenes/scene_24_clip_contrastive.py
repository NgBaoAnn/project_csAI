"""Scene 24: CLIP contrastive learning."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class CLIPContrastiveScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "CLIP", "Image-text contrastive learning")
        placeholder = Text("[24] Image encoder + text encoder -> shared embedding", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
