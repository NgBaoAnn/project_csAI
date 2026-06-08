"""Scene 22: IRM objective."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class IRMObjectiveScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "IRM Objective", "Cùng một classifier w cho mọi environment")
        placeholder = Text("[22] X -> Phi(X) -> w -> Y; same boundary across envs", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
