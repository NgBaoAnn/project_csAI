"""Scene 01: Accuracy cao nhưng fail ngoài đời."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class AccuracyFailScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "99% Accuracy", "Nhưng vẫn sai ngoài đời?")

        label = Text(
            "Test accuracy",
            font_size=SIZE_SECTION,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
        ).to_edge(UP, buff=0.9)

        score = DecimalNumber(
            99.1,
            num_decimal_places=1,
            font_size=96,
            color=THEME_EMERALD,
        )
        percent = Text("%", font_size=72, color=THEME_EMERALD, font=FONT_PRIMARY)
        counter = VGroup(score, percent).arrange(RIGHT, buff=0.12).move_to(ORIGIN)

        lab_caption = Text(
            "Trong lab: mọi thứ có vẻ ổn",
            font_size=SIZE_BODY,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
        ).next_to(counter, DOWN, buff=0.7)

        self.play(FadeIn(label, shift=DOWN * 0.2), run_time=TIME_NORMAL)
        self.play(Write(counter), run_time=TIME_SLOW)
        self.play(FadeIn(lab_caption, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        cracks = VGroup(
            Line(UP * 0.2 + LEFT * 0.25, DOWN * 0.7 + RIGHT * 0.05, color=THEME_RED),
            Line(DOWN * 0.05 + RIGHT * 0.05, UP * 0.45 + RIGHT * 0.65, color=THEME_RED),
            Line(DOWN * 0.15 + RIGHT * 0.1, DOWN * 0.65 + RIGHT * 0.65, color=THEME_RED),
        ).set_stroke(width=5).move_to(counter)

        warning = create_insight_box(
            "High test accuracy is not deployment reliability",
            color=THEME_RED,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.9)

        deployment = Text(
            "Ngoài đời: distribution có thể đã đổi",
            font_size=SIZE_BODY,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
        ).next_to(counter, UP, buff=0.35)

        self.play(
            Create(cracks),
            counter.animate.set_color(THEME_RED),
            run_time=TIME_NORMAL,
        )
        self.play(Transform(lab_caption, deployment), run_time=TIME_NORMAL)
        self.play(FadeIn(warning, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
