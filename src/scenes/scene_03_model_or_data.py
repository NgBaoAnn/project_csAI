"""Scene 03: Model problem hay data problem?"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


TARGET_DURATION_SECONDS = 70


class ModelOrDataScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Lỗi model?", "Hay lỗi dữ liệu?")

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

        model_title = Text("Lỗi model?", font_size=SIZE_BODY, color=THEME_BLUE, font=FONT_PRIMARY).move_to(model_box.get_top() + DOWN * 0.45)
        data_title = Text("Lỗi dữ liệu?", font_size=SIZE_BODY, color=THEME_EMERALD, font=FONT_PRIMARY).move_to(data_box.get_top() + DOWN * 0.45)

        model_items = VGroup(
            Text("số lớp", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("tham số", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("regularization", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(model_box.get_center() + DOWN * 0.2)

        data_items = VGroup(
            Text("nguồn dữ liệu", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
            Text("nhóm ẩn", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
            Text("cơ chế", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
            Text("shifts", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14).move_to(data_box.get_center() + DOWN * 0.12)

        focus = SurroundingRectangle(VGroup(data_box, data_title, data_items), color=THEME_EMERALD, buff=0.15, stroke_width=4)
        insight = create_insight_box(
            "Nhiều lỗi model thật ra là lỗi dữ liệu.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.7)
        bridge_arrow = Arrow(
            model_box.get_right() + RIGHT * 0.15,
            data_box.get_left() + LEFT * 0.15,
            color=THEME_AMBER,
            stroke_width=2.5,
            buff=0.12,
        )
        bridge_dot = Dot(bridge_arrow.get_start(), color=THEME_AMBER, radius=0.055)
        bridge_path = Line(bridge_arrow.get_start(), bridge_arrow.get_end())

        self.play(
            FadeIn(model_box, shift=RIGHT * 0.2),
            FadeIn(data_box, shift=LEFT * 0.2),
            rate_func=smooth,
            run_time=TIME_NORMAL,
        )
        play_voiceover_and_wait(self, 3, 0)
        self.wait(9.0)
        self.play(Write(model_title), Write(data_title), run_time=TIME_NORMAL)
        self.wait(9.0)
        self.play(LaggedStart(*[FadeIn(item, shift=UP * 0.1) for item in model_items], lag_ratio=0.14), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 3, 1)
        self.wait(11.0)
        self.play(GrowArrow(bridge_arrow), FadeIn(bridge_dot, scale=0.4), run_time=0.8)
        self.play(MoveAlongPath(bridge_dot, bridge_path), run_time=1.0, rate_func=smooth)
        self.play(FadeOut(bridge_dot), run_time=0.2)
        self.play(
            model_box.animate.set_stroke(opacity=0.45),
            model_items.animate.set_opacity(0.55),
            data_box.animate.set_fill(THEME_EMERALD, opacity=0.05).set_stroke(width=2.8),
            LaggedStart(*[FadeIn(item, shift=UP * 0.1) for item in data_items], lag_ratio=0.12),
            run_time=TIME_NORMAL,
        )
        self.play(Circumscribe(data_box, color=THEME_EMERALD, buff=0.08), run_time=1.5)
        self.play(ApplyWave(data_items, direction=RIGHT, amplitude=0.12), run_time=1.5)
        self.wait(11.0)
        self.play(FadeOut(bridge_arrow), Create(focus), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 3, 2)
        self.wait(16.0)

        fade_out_all(self)
