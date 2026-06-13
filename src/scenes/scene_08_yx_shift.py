"""Scene 08: Y|X-shift."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


TARGET_DURATION_SECONDS = 80


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
        boundary_label = Text("ranh giới dự đoán", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(boundary, DOWN, buff=0.15)
        return VGroup(frame, heading, points, boundary, boundary_label)

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Y|X-shift", "Cơ chế dự đoán thay đổi")

        source = self.make_panel("Cơ chế source", LEFT * 2.85 + DOWN * 0.1, 0.35, THEME_BLUE)
        target = self.make_panel("Cơ chế target", RIGHT * 2.85 + DOWN * 0.1, -0.45, THEME_AMBER)

        formula = MathTex(
            r"P_{\mathrm{source}}(Y|X)",
            r"\neq",
            r"P_{\mathrm{target}}(Y|X)",
            font_size=SIZE_FORMULA,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.55)
        formula[0].set_color(THEME_BLUE)
        formula[2].set_color(THEME_AMBER)

        mechanism_note = Text(
            "X nhìn giống nhau, nhưng P(Y|X) khác",
            font_size=SIZE_CAPTION,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
        ).next_to(formula, DOWN, buff=0.25)
        mechanism_sweep = Line(
            mechanism_note.get_left() + DOWN * 0.18,
            mechanism_note.get_right() + DOWN * 0.18,
            color=THEME_AMBER,
            stroke_width=2.5,
        )

        insight = create_insight_box(
            "Y|X-shift đổi ý nghĩa của dữ liệu.",
            color=THEME_RED,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.65)

        self.play(Write(formula), FadeIn(mechanism_note, shift=DOWN * 0.1), run_time=TIME_NORMAL, rate_func=smooth)
        play_voiceover_and_wait(self, 8, 0)
        self.wait(14.0)
        self.play(FadeIn(source, shift=RIGHT * 0.15), run_time=TIME_NORMAL, rate_func=smooth)
        self.wait(14.0)
        self.play(TransformFromCopy(source[2], target[2]), FadeIn(target[0], shift=LEFT * 0.15), FadeIn(target[1], shift=LEFT * 0.15), FadeIn(target[3], shift=LEFT * 0.15), FadeIn(target[4], shift=LEFT * 0.15), run_time=TIME_NORMAL, rate_func=smooth)
        play_voiceover_and_wait(self, 8, 1)
        self.wait(18.0)
        self.play(
            ShowPassingFlash(mechanism_sweep, time_width=0.55),
            source[3].animate.set_color(THEME_BLUE),
            Rotate(target[3], angle=-0.22, about_point=target[3].get_center()),
            target[3].animate.set_color(THEME_RED),
            run_time=TIME_NORMAL,
        )
        self.play(Circumscribe(target, color=THEME_RED, buff=0.08), run_time=1.5)
        self.wait(18.5)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 8, 2)
        self.wait(5.0)

        fade_out_all(self)
