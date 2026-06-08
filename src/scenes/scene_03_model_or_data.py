"""Scene 03: Model problem hay data problem?"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


TARGET_DURATION_SECONDS = 70


class ModelOrDataScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Model problem?", "Hay data problem?")

        model_box = RoundedRectangle(
            width=4.1,
            height=2.5,
            corner_radius=0.08,
            stroke_color=THEME_BLUE,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        ).shift(LEFT * 2.6)
        data_box = RoundedRectangle(
            width=4.1,
            height=2.5,
            corner_radius=0.08,
            stroke_color=THEME_EMERALD,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        ).shift(RIGHT * 2.6)

        model_title = Text("Model problem?", font_size=SIZE_BODY, color=THEME_BLUE, font=FONT_PRIMARY).move_to(model_box.get_top() + DOWN * 0.45)
        data_title = Text("Data problem?", font_size=SIZE_BODY, color=THEME_EMERALD, font=FONT_PRIMARY).move_to(data_box.get_top() + DOWN * 0.45)

        model_items = VGroup(
            Text("layers", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("parameters", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("regularization", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(model_box.get_center() + DOWN * 0.2)

        data_items = VGroup(
            Text("sources", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
            Text("subpopulations", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
            Text("mechanisms", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
            Text("shifts", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(data_box.get_center() + DOWN * 0.12)

        focus = SurroundingRectangle(VGroup(data_box, data_title, data_items), color=THEME_EMERALD, buff=0.15, stroke_width=4)
        insight = create_insight_box(
            "Many model problems are data problems",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.7)

        self.play(
            FadeIn(model_box, shift=RIGHT * 0.2),
            FadeIn(data_box, shift=LEFT * 0.2),
            run_time=TIME_NORMAL,
        )
        self.wait(9.0)
        self.play(Write(model_title), Write(data_title), run_time=TIME_NORMAL)
        self.wait(9.0)
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.1) for item in model_items], lag_ratio=0.14), run_time=TIME_NORMAL)
        self.wait(11.0)
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.1) for item in data_items], lag_ratio=0.12), run_time=TIME_NORMAL)
        self.play(Circumscribe(data_box, color=THEME_EMERALD, buff=0.08), run_time=1.5)
        self.play(ApplyWave(data_items, direction=RIGHT, amplitude=0.12), run_time=1.5)
        self.wait(13.0)
        self.play(Create(focus), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(16.0)

        fade_out_all(self)
