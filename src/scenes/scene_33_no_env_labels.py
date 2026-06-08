"""Scene 33: No environment labels."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class NoEnvLabelsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "No Environment Labels", "Pooled data làm mất source tags")
        placeholder = Text("[33] Sources with tags -> funnel -> tags disappear", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
