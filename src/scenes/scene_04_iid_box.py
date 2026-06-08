"""Scene 04: i.i.d. bằng chiếc hộp phân phối."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


TARGET_DURATION_SECONDS = 80


class IIDBoxScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "i.i.d. Assumption", "Một chiếc hộp sinh train và test")

        box = RoundedRectangle(
            width=2.6,
            height=1.55,
            corner_radius=0.08,
            stroke_color=THEME_PURPLE,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        ).move_to(UP * 1.25)
        box_label = MathTex(r"P(X,Y)", font_size=SIZE_FORMULA, color=TEXT_PRIMARY).move_to(box)

        train_bucket = RoundedRectangle(width=2.5, height=1.2, corner_radius=0.07, stroke_color=THEME_BLUE).shift(LEFT * 2.6 + DOWN * 0.9)
        test_bucket = RoundedRectangle(width=2.5, height=1.2, corner_radius=0.07, stroke_color=THEME_EMERALD).shift(RIGHT * 2.6 + DOWN * 0.9)
        train_label = Text("train", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY).move_to(train_bucket)
        test_label = Text("test", font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY).move_to(test_bucket)

        train_arrow = Arrow(box.get_bottom(), train_bucket.get_top(), color=THEME_BLUE, buff=0.15)
        test_arrow = Arrow(box.get_bottom(), test_bucket.get_top(), color=THEME_EMERALD, buff=0.15)

        train_dots = VGroup(*[
            Dot(train_bucket.get_center() + LEFT * 0.75 + RIGHT * 0.3 * i + UP * (0.15 if i % 2 else -0.12), color=THEME_BLUE, radius=0.045)
            for i in range(6)
        ])
        test_dots = VGroup(*[
            Dot(test_bucket.get_center() + LEFT * 0.75 + RIGHT * 0.3 * i + UP * (-0.12 if i % 2 else 0.15), color=THEME_EMERALD, radius=0.045)
            for i in range(6)
        ])

        formula = MathTex(
            r"P_{\mathrm{train}}(X,Y)",
            r"=",
            r"P_{\mathrm{test}}(X,Y)",
            font_size=SIZE_FORMULA,
            color=TEXT_PRIMARY,
        ).to_edge(DOWN, buff=1.45)
        formula[0].set_color(THEME_BLUE)
        formula[2].set_color(THEME_EMERALD)
        iid_tag = create_insight_box(
            "i.i.d. = same data-generating distribution",
            color=THEME_PURPLE,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.45)
        train_sample = Dot(box.get_bottom() + DOWN * 0.05, color=THEME_BLUE, radius=0.06)
        test_sample = Dot(box.get_bottom() + DOWN * 0.05, color=THEME_EMERALD, radius=0.06)
        train_path = Line(train_sample.get_center(), train_bucket.get_center(), color=THEME_BLUE)
        test_path = Line(test_sample.get_center(), test_bucket.get_center(), color=THEME_EMERALD)
        train_trace = TracedPath(train_sample.get_center, stroke_color=THEME_BLUE, stroke_width=2, dissipating_time=0.8)
        test_trace = TracedPath(test_sample.get_center, stroke_color=THEME_EMERALD, stroke_width=2, dissipating_time=0.8)

        self.play(FadeIn(box), Write(box_label), run_time=TIME_NORMAL)
        self.wait(13.0)
        self.play(GrowArrow(train_arrow), GrowArrow(test_arrow), run_time=TIME_NORMAL)
        self.add(train_sample, test_sample, train_trace, test_trace)
        self.play(
            MoveAlongPath(train_sample, train_path),
            MoveAlongPath(test_sample, test_path),
            run_time=2.0,
        )
        self.remove(train_sample, test_sample, train_trace, test_trace)
        self.wait(10.0)
        self.play(FadeIn(train_bucket), FadeIn(test_bucket), Write(train_label), Write(test_label), run_time=TIME_NORMAL)
        self.wait(14.0)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.5) for dot in VGroup(train_dots, test_dots)], lag_ratio=0.04), run_time=TIME_NORMAL)
        self.wait(18.0)
        self.play(Write(formula), FadeIn(iid_tag, shift=UP * 0.2), run_time=TIME_SLOW)
        self.wait(13.0)

        fade_out_all(self)
