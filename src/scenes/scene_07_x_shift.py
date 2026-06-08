"""Scene 07: X-shift."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class XShiftScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "X-shift", "Input distribution thay đổi")

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 1.2, 0.5],
            x_length=8.2,
            y_length=3.2,
            tips=False,
            axis_config={"color": GRID_COLOR, "stroke_width": 2},
        ).shift(UP * 0.25)

        p_curve = axes.plot(lambda x: 0.95 * (2.718 ** (-(x + 1.2) ** 2 / 1.1)), color=THEME_BLUE, stroke_width=4)
        q_curve = axes.plot(lambda x: 0.95 * (2.718 ** (-(x - 1.15) ** 2 / 1.1)), color=THEME_AMBER, stroke_width=4)
        p_label = Text("P(X)", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_CODE).next_to(p_curve, UP, buff=0.15)
        q_label = Text("Q(X)", font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_CODE).next_to(q_curve, UP, buff=0.15)

        boundary = Line(UP * 1.8, DOWN * 1.8, color=THEME_EMERALD, stroke_width=4).shift(RIGHT * 0.25)
        boundary_label = Text(
            "same decision rule",
            font_size=SIZE_CAPTION,
            color=THEME_EMERALD,
            font=FONT_PRIMARY,
        ).next_to(boundary, RIGHT, buff=0.25)

        formula = MathTex(r"P(X)", r"\neq", r"Q(X)", font_size=SIZE_FORMULA, color=TEXT_PRIMARY).to_edge(UP, buff=0.5)
        formula[0].set_color(THEME_BLUE)
        formula[2].set_color(THEME_AMBER)

        insight = create_insight_box(
            "X-shift changes where data appears",
            color=THEME_BLUE,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.8)

        self.play(Create(axes), Write(formula), run_time=TIME_NORMAL)
        self.play(Create(p_curve), FadeIn(p_label), run_time=TIME_NORMAL)
        self.play(Create(q_curve), FadeIn(q_label), run_time=TIME_NORMAL)
        self.play(Create(boundary), FadeIn(boundary_label, shift=LEFT * 0.1), run_time=TIME_NORMAL)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
