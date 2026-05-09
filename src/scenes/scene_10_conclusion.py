"""
Scene 10: Conclusion & Future Directions
Phụ trách: TV4 (Production Lead)
Thời lượng: ~2 phút

Nội dung:
- Recap hành trình
- Comparison table: ERM vs IRM vs DRO vs Stable
- Open problems
- Final message + Credits
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class ConclusionScene(Scene):
    """TODO: TV4 implement scene này."""
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Conclusion", "Tổng kết & Hướng đi tương lai")

        # TODO: Implement
        # 1. Journey recap montage
        # 2. Summary comparison table
        # 3. Open problems: self-aware, uncertainty, scalability
        # 4. Final message: "Heterogeneity is not a bug, it's a feature"
        # 5. Credits: team + references

        placeholder = Text("[ Scene 10: Conclusion — TODO ]", font_size=SIZE_BODY, color=TEXT_MUTED)
        self.play(Write(placeholder))
        self.wait(2)
