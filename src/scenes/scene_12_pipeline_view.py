"""Scene 12: Pipeline view."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class PipelineViewScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Pipeline View", "Collection -> Training -> Evaluation -> Deployment")
        placeholder = Text("[12] Heterogeneity-aware ML là workflow xuyên suốt pipeline", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
