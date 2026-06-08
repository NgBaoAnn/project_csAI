"""Scene 08: Y|X-shift."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class YXShiftScene(Scene):
    def make_panel(self, title, shift, boundary_angle, color):
        frame = RoundedRectangle(width=5.0, height=3.2, corner_radius=0.08, stroke_color=color)
        frame.shift(shift)
        heading = Text(title, font_size=SIZE_CAPTION, color=color, font=FONT_PRIMARY).next_to(frame, UP, buff=0.18)
        points = VGroup()
        coords = [(-1.4, -0.7), (-0.9, 0.25), (-0.35, -0.25), (0.25, 0.55), (0.85, -0.1), (1.35, 0.7)]
        for i, (x, y) in enumerate(coords):
            dot_color = THEME_BLUE if i < 3 else THEME_RED
            points.add(Dot(frame.get_center() + RIGHT * x + UP * y, color=dot_color, radius=0.065))
        boundary = Line(LEFT * 1.9, RIGHT * 1.9, color=color, stroke_width=4).rotate(boundary_angle).move_to(frame.get_center())
        boundary_label = Text("decision boundary", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(boundary, DOWN, buff=0.15)
        return VGroup(frame, heading, points, boundary, boundary_label)

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Y|X-shift", "Cơ chế dự đoán thay đổi")

        source = self.make_panel("Source mechanism", LEFT * 2.85 + DOWN * 0.1, 0.35, THEME_BLUE)
        target = self.make_panel("Target mechanism", RIGHT * 2.85 + DOWN * 0.1, -0.45, THEME_AMBER)

        formula = MathTex(
            r"P_{source}(Y|X)",
            r"\neq",
            r"P_{target}(Y|X)",
            font_size=SIZE_FORMULA,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.55)
        formula[0].set_color(THEME_BLUE)
        formula[2].set_color(THEME_AMBER)

        mechanism_note = Text(
            "Same-looking X, different mechanism P(Y|X)",
            font_size=SIZE_CAPTION,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
        ).next_to(formula, DOWN, buff=0.25)

        insight = create_insight_box(
            "Y|X-shift changes what the data means",
            color=THEME_RED,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.65)

        self.play(Write(formula), FadeIn(mechanism_note, shift=DOWN * 0.1), run_time=TIME_NORMAL)
        self.play(FadeIn(source, shift=RIGHT * 0.15), run_time=TIME_NORMAL)
        self.play(FadeIn(target, shift=LEFT * 0.15), run_time=TIME_NORMAL)
        self.play(source[3].animate.set_color(THEME_BLUE), target[3].animate.set_color(THEME_RED), run_time=TIME_NORMAL)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
