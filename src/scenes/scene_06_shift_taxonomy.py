"""Scene 06: Distribution shift taxonomy."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


TARGET_DURATION_SECONDS = 70


class ShiftTaxonomyScene(Scene):
    def branch(self, title, formula, color):
        box = RoundedRectangle(
            width=3.0,
            height=1.55,
            corner_radius=0.08,
            stroke_color=color,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        )
        title_obj = Text(title, font_size=SIZE_CAPTION, color=color, font=FONT_PRIMARY)
        formula_obj = Text(formula, font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_CODE)
        return VGroup(box, title_obj, formula_obj).arrange(DOWN, buff=0.12)

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Distribution Shift", "Shift không chỉ có một loại")

        root = create_insight_box("Distribution Shift", color=THEME_PURPLE, font_size=SIZE_BODY).to_edge(UP, buff=0.8)

        x_shift = self.branch("X-shift", "P(X) changes", THEME_BLUE)
        label_shift = self.branch("Label shift", "P(Y) changes", THEME_AMBER)
        yx_shift = self.branch("Y|X-shift", "P(Y|X) changes", THEME_RED)
        branches = VGroup(x_shift, label_shift, yx_shift).arrange(RIGHT, buff=0.45).shift(DOWN * 0.35)

        arrows = VGroup(*[
            Arrow(root.get_bottom(), branch.get_top(), color=TEXT_MUTED, buff=0.15, stroke_width=2)
            for branch in branches
        ])

        caption = create_insight_box(
            "Robust to what shift?",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.75)

        self.play(FadeIn(root, shift=DOWN * 0.2), run_time=TIME_NORMAL)
        self.wait(12.0)
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.15), run_time=TIME_NORMAL)
        self.wait(10.0)
        self.play(LaggedStart(*[FadeIn(branch, shift=UP * 0.2) for branch in branches], lag_ratio=0.18), run_time=TIME_SLOW)
        self.play(
            LaggedStart(
                Circumscribe(x_shift, color=THEME_BLUE, buff=0.08),
                Circumscribe(label_shift, color=THEME_AMBER, buff=0.08),
                Circumscribe(yx_shift, color=THEME_RED, buff=0.08),
                lag_ratio=0.22,
            ),
            run_time=3.0,
        )
        self.play(Indicate(root, color=THEME_PURPLE), run_time=1.0)
        self.wait(18.0)
        self.play(FadeIn(caption, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(17.0)

        fade_out_all(self)
