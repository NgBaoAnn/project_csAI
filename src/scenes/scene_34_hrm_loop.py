"""Scene 34: Heterogeneous Risk Minimization loop."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class HRMLoopScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "HRM Loop", "Learn environments, then learn invariance")
        placeholder = Text("[34] Heterogeneity identification <-> invariant prediction", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
