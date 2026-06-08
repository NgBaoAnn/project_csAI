"""Scene 26: Deductive vs inductive."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class DeductiveInductiveScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Deductive vs Inductive", "Bắt đầu từ giả định hay dữ liệu thật?")
        placeholder = Text("[26] assumption -> method vs data -> shift -> method", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
