"""Scene 07: X-shift."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


TARGET_DURATION_SECONDS = 75


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
        q_curve_ghost = p_curve.copy().set_color(THEME_AMBER).set_stroke(opacity=0.38)
        p_label = MathTex(r"P(X)", font_size=SIZE_CAPTION, color=THEME_BLUE).next_to(axes.c2p(-1.2, 0.95), UP, buff=0.15)
        q_label = MathTex(r"Q(X)", font_size=SIZE_CAPTION, color=THEME_AMBER).next_to(axes.c2p(1.15, 0.95), UP, buff=0.15)

        boundary = Line(UP * 1.8, DOWN * 1.8, color=THEME_EMERALD, stroke_width=4).shift(RIGHT * 0.25)
        boundary_label = Text(
            "cùng rule dự đoán",
            font_size=SIZE_CAPTION,
            color=THEME_EMERALD,
            font=FONT_PRIMARY,
        ).next_to(boundary.get_top(), RIGHT, buff=0.25)

        formula = MathTex(r"P(X)", r"\neq", r"Q(X)", font_size=SIZE_FORMULA, color=TEXT_PRIMARY).to_edge(UP, buff=0.5)
        formula[0].set_color(THEME_BLUE)
        formula[2].set_color(THEME_AMBER)

        insight = create_insight_box(
            "X-shift đổi nơi dữ liệu xuất hiện.",
            color=THEME_BLUE,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.8)

        self.play(Create(axes), Write(formula), run_time=TIME_NORMAL, rate_func=smooth)
        self.wait(10.0)
        self.play(TransformFromCopy(formula[0], p_label), Create(p_curve), run_time=TIME_NORMAL)
        self.wait(12.0)
        self.play(Create(q_curve_ghost), TransformFromCopy(formula[2], q_label), run_time=0.8)
        self.play(Transform(q_curve_ghost, q_curve), run_time=1.4, rate_func=smooth)
        q_curve = q_curve_ghost
        self.wait(14.8)
        self.play(Create(boundary), FadeIn(boundary_label, shift=LEFT * 0.1), run_time=TIME_NORMAL, rate_func=smooth)
        self.play(Indicate(boundary, color=THEME_EMERALD), Circumscribe(boundary_label, color=THEME_EMERALD), run_time=1.5)
        self.wait(13.5)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(13.0)

        fade_out_all(self)
