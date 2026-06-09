"""
Scene 33: No Environment Labels
Author: TV4 (Animation Lead)
Duration: ~65 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait
import numpy as np


class NoEnvLabelsScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: 3 converging dots spiral and purple ripple explosion
        dot_a = Dot(LEFT * 2.5 + UP * 1.8, color=THEME_BLUE, radius=0.22)
        dot_b = Dot(RIGHT * 2.5 + UP * 1.8, color=THEME_AMBER, radius=0.22)
        dot_c = Dot(DOWN * 1.8, color=THEME_ORANGE, radius=0.22)

        dots = VGroup(dot_a, dot_b, dot_c)
        self.play(FadeIn(dots), run_time=TIME_NORMAL)

        self.play(
            Rotate(dots, angle=2.2 * PI, about_point=ORIGIN),
            dots.animate.scale(0.05).move_to(ORIGIN),
            run_time=2.5, rate_func=smooth
        )

        ripple = Circle(radius=0.1, color=THEME_PURPLE, stroke_width=8)
        self.add(ripple)
        self.play(
            FadeOut(dots),
            ripple.animate.scale(45).set_stroke(width=0, opacity=0),
            run_time=1.5, rate_func=smooth
        )

        title_text = Text("No Env Labels", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_PURPLE, THEME_BLUE_LIGHT)
        title_glow = create_3b1b_glow(title_text, color=THEME_PURPLE, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        subtitle_text = Text("Khi nguồn gốc dữ liệu bị xóa bỏ", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)

        self.play(FadeIn(title_group, scale=0.85), Write(subtitle_text), run_time=TIME_NORMAL)
        # seg 0: Title introduction
        play_voiceover_and_wait(self, 33, 0)
        self.play(FadeOut(title_group), FadeOut(subtitle_text), FadeOut(ripple), run_time=TIME_FAST)

        # Subtitle 1
        sub1 = create_bottom_caption("Các dataset lớn thường gộp dữ liệu từ nhiều nguồn khác nhau.")
        self.play(FadeIn(sub1))
        # seg 1: "dataset hiện đại gộp nhiều nguồn..."
        play_voiceover_and_wait(self, 33, 1)

        # Draw 3 Sources with Tag Colors
        source_a = VGroup(
            RoundedRectangle(width=1.8, height=1.0, corner_radius=0.05, stroke_color=THEME_BLUE, stroke_width=2),
            Text("Nguồn A", font_size=SIZE_SMALL - 4, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD)
        ).shift(LEFT * 4.2 + UP * 2.4)
        source_b = VGroup(
            RoundedRectangle(width=1.8, height=1.0, corner_radius=0.05, stroke_color=THEME_AMBER, stroke_width=2),
            Text("Nguồn B", font_size=SIZE_SMALL - 4, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD)
        ).shift(UP * 2.4)
        source_c = VGroup(
            RoundedRectangle(width=1.8, height=1.0, corner_radius=0.05, stroke_color=THEME_ORANGE, stroke_width=2),
            Text("Nguồn C", font_size=SIZE_SMALL - 4, color=THEME_ORANGE, font=FONT_PRIMARY, weight=BOLD)
        ).shift(RIGHT * 4.2 + UP * 2.4)

        dots_a = VGroup(*[Dot(source_a.get_center() + DOWN * 0.8 + RIGHT * x * 0.3 + UP * y * 0.3, color=THEME_BLUE, radius=0.06) for x in (-1, 0, 1) for y in (-0.5, 0.5)])
        dots_b = VGroup(*[Dot(source_b.get_center() + DOWN * 0.8 + RIGHT * x * 0.3 + UP * y * 0.3, color=THEME_AMBER, radius=0.06) for x in (-1, 0, 1) for y in (-0.5, 0.5)])
        dots_c = VGroup(*[Dot(source_c.get_center() + DOWN * 0.8 + RIGHT * x * 0.3 + UP * y * 0.3, color=THEME_ORANGE, radius=0.06) for x in (-1, 0, 1) for y in (-0.5, 0.5)])

        self.play(
            FadeIn(source_a), FadeIn(source_b), FadeIn(source_c),
            FadeIn(dots_a), FadeIn(dots_b), FadeIn(dots_c),
            run_time=TIME_NORMAL
        )
        # seg 2: "ba nguồn riêng biệt, mỗi nguồn có environment label..."
        play_voiceover_and_wait(self, 33, 2)

        # Subtitle 2
        sub2 = create_bottom_caption("Nhưng khi tích hợp, các nhãn môi trường (environment labels) đều bị mất.")
        self.play(Transform(sub1, sub2))
        # seg 3: "khi tích hợp, nhãn môi trường bị xóa mất..."
        play_voiceover_and_wait(self, 33, 3)

        # Draw a pooling funnel
        funnel_left = Line(LEFT * 1.8 + UP * 1.0, LEFT * 0.5 + UP * 0.0, color=THEME_PURPLE, stroke_width=3)
        funnel_right = Line(RIGHT * 1.8 + UP * 1.0, RIGHT * 0.5 + UP * 0.0, color=THEME_PURPLE, stroke_width=3)
        funnel_neck_l = Line(LEFT * 0.5 + UP * 0.0, LEFT * 0.5 + DOWN * 0.5, color=THEME_PURPLE, stroke_width=3)
        funnel_neck_r = Line(RIGHT * 0.5 + UP * 0.0, RIGHT * 0.5 + DOWN * 0.5, color=THEME_PURPLE, stroke_width=3)
        funnel = VGroup(funnel_left, funnel_right, funnel_neck_l, funnel_neck_r)

        self.play(Create(funnel), run_time=TIME_NORMAL)
        self.wait(0.5)

        pooled_cloud_center = DOWN * 1.2
        np.random.seed(33)
        n_dots = len(dots_a) + len(dots_b) + len(dots_c)
        pooled_dots = VGroup(*[
            Dot(pooled_cloud_center + RIGHT * np.random.normal(0, 0.8) + UP * np.random.normal(0, 0.35), color=TEXT_MUTED, radius=0.06)
            for _ in range(n_dots)
        ])

        self.play(
            dots_a.animate.move_to(UP * 0.35).set_color(THEME_BLUE),
            dots_b.animate.move_to(UP * 0.35).set_color(THEME_AMBER),
            dots_c.animate.move_to(UP * 0.35).set_color(THEME_ORANGE),
            run_time=2.0
        )
        self.play(
            ReplacementTransform(VGroup(dots_a, dots_b, dots_c), pooled_dots),
            FadeOut(source_a), FadeOut(source_b), FadeOut(source_c),
            run_time=2.0
        )

        pooled_label = Text("Dữ liệu gộp (Tất cả màu xám)", font_size=SIZE_SMALL - 2, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(pooled_dots, DOWN, buff=0.2)
        self.play(Write(pooled_label), run_time=TIME_NORMAL)
        # seg 4: "giờ chỉ còn dữ liệu gộp xám, invariant learning mất phương hướng..."
        play_voiceover_and_wait(self, 33, 4)

        # Takeaway
        insight = create_insight_box(
            "Đôi khi các environment phải được tự học.",
            color=THEME_RED,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.45)

        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 5: "đôi khi environment phải được tự học..."
        play_voiceover_and_wait(self, 33, 5)

        # Outro
        self.play(
            FadeOut(funnel), FadeOut(pooled_dots), FadeOut(pooled_label), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
