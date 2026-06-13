"""Scene 05: Train/test clouds tách nhau."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


TARGET_DURATION_SECONDS = 75


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
        animate_title_card(self, "Train/Test tách nhau", "Khi target cloud rời khỏi train cloud")

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

        iid_formula = MathTex(
            r"P_{\mathrm{train}}",
            r"\approx",
            r"P_{\mathrm{test}}",
            font_size=SIZE_FORMULA,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.55)
        iid_formula[0].set_color(THEME_BLUE)
        iid_formula[2].set_color(THEME_EMERALD)
        shift_formula = MathTex(
            r"P_{\mathrm{train}}",
            r"\neq",
            r"P_{\mathrm{target}}",
            font_size=SIZE_FORMULA,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.55)
        shift_formula[0].set_color(THEME_BLUE)
        shift_formula[2].set_color(THEME_AMBER)

        accuracy = Text("96.4%", font_size=SIZE_SECTION, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD)
        acc_group = VGroup(Text("accuracy", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY), accuracy).arrange(DOWN, buff=0.1).to_edge(RIGHT, buff=0.8)
        shifted_accuracy = Text(
            "69.2%",
            font_size=SIZE_SECTION,
            color=THEME_RED,
            font=FONT_PRIMARY,
            weight=BOLD,
        ).move_to(accuracy)

        insight = create_insight_box(
            "Distribution shift bắt đầu khi train và target tách nhau.",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.65)
        test_path = Line(test_cloud.get_center(), test_cloud.get_center() + RIGHT * 2.35 + DOWN * 0.35)
        test_label_path = Line(test_label.get_center(), test_label.get_center() + RIGHT * 2.35 + DOWN * 0.35)
        shift_trail = DashedLine(
            test_cloud.get_center(),
            test_path.get_end(),
            color=THEME_AMBER,
            stroke_width=2,
            dash_length=0.12,
            stroke_opacity=0.55,
        )

        self.play(Create(axes), Write(iid_formula), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 5, 0)
        self.wait(9.0)
        self.play(
            LaggedStart(
                FadeIn(train_cloud, scale=0.95),
                FadeIn(test_cloud, scale=0.95),
                FadeIn(train_label, shift=DOWN * 0.1),
                FadeIn(test_label, shift=UP * 0.1),
                lag_ratio=0.18,
            ),
            run_time=TIME_NORMAL,
            rate_func=smooth,
        )
        self.wait(13.0)
        self.play(FadeIn(acc_group, shift=LEFT * 0.2), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 5, 1)
        self.wait(13.0)
        self.play(
            Create(shift_trail),
            MoveAlongPath(test_cloud, test_path),
            MoveAlongPath(test_label, test_label_path),
            Transform(iid_formula, shift_formula),
            Transform(accuracy, shifted_accuracy),
            run_time=TIME_SLOW,
            rate_func=smooth,
        )
        self.play(
            test_cloud.animate.set_color(THEME_AMBER),
            test_label.animate.set_color(THEME_AMBER),
            Flash(accuracy, color=THEME_RED, flash_radius=0.55),
            run_time=1.0,
        )
        self.wait(17.0)
        self.play(FadeIn(insight, shift=UP * 0.2), FadeOut(shift_trail), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 5, 2)
        self.wait(12.0)

        fade_out_all(self)
