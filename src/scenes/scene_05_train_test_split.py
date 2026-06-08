"""Scene 05: Train/test clouds tách nhau."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class TrainTestSplitScene(Scene):
    def cloud(self, center, color):
        offsets = [
            (-0.55, -0.12), (-0.35, 0.28), (-0.18, -0.32), (0.05, 0.18),
            (0.22, -0.02), (0.4, 0.32), (0.55, -0.22), (-0.05, 0.48),
            (-0.62, 0.35), (0.62, 0.1), (0.18, -0.5), (-0.32, -0.48),
        ]
        return VGroup(*[
            Dot([center[0] + x, center[1] + y, 0], radius=0.055, color=color)
            for x, y in offsets
        ])

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Train/Test Divergence", "Khi target cloud rời khỏi train cloud")

        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=8,
            y_length=4.2,
            tips=False,
            axis_config={"color": GRID_COLOR, "stroke_width": 2},
        ).shift(UP * 0.2)

        train_cloud = self.cloud((-1.1, 0.1), THEME_BLUE)
        test_cloud = self.cloud((-0.95, 0.15), THEME_EMERALD)
        train_label = Text("train", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY).next_to(train_cloud, UP)
        test_label = Text("test", font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(test_cloud, DOWN)

        iid_formula = MathTex(r"P_{train}", r"\approx", r"P_{test}", font_size=SIZE_FORMULA, color=TEXT_PRIMARY).to_edge(UP, buff=0.55)
        shift_formula = MathTex(r"P_{train}", r"\neq", r"P_{target}", font_size=SIZE_FORMULA, color=TEXT_PRIMARY).to_edge(UP, buff=0.55)
        shift_formula[2].set_color(THEME_AMBER)

        accuracy = DecimalNumber(96.4, num_decimal_places=1, font_size=SIZE_SECTION, color=THEME_EMERALD)
        percent = Text("%", font_size=SIZE_SECTION, color=THEME_EMERALD, font=FONT_PRIMARY)
        acc_group = VGroup(Text("accuracy", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY), VGroup(accuracy, percent).arrange(RIGHT, buff=0.08)).arrange(DOWN, buff=0.1).to_edge(RIGHT, buff=0.8)

        insight = create_insight_box(
            "Distribution shift begins when train and target diverge",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.65)

        self.play(Create(axes), Write(iid_formula), run_time=TIME_NORMAL)
        self.play(FadeIn(train_cloud), FadeIn(test_cloud), FadeIn(train_label), FadeIn(test_label), run_time=TIME_NORMAL)
        self.play(FadeIn(acc_group, shift=LEFT * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)
        self.play(
            test_cloud.animate.shift(RIGHT * 2.35 + DOWN * 0.35).set_color(THEME_AMBER),
            test_label.animate.shift(RIGHT * 2.35 + DOWN * 0.35).set_color(THEME_AMBER),
            Transform(iid_formula, shift_formula),
            accuracy.animate.set_value(69.2).set_color(THEME_RED),
            percent.animate.set_color(THEME_RED),
            run_time=TIME_SLOW,
        )
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
