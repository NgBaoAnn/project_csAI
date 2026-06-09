"""
Scene 25: More Data != Right Data
Author: TV3 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait
from utils.math_helpers import create_data_cloud, animate_data_cloud_in

class MoreDataNotRightDataScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: Data Quality Comparison
        # Left cluster: 20 fixed grey dots
        fixed_coords = [
            (-3.5, 0.8), (-3.2, 1.2), (-3.8, 0.5), (-2.9, 0.9), (-3.4, 0.4),
            (-3.7, 1.0), (-3.1, 0.6), (-3.6, 1.3), (-2.8, 1.1), (-3.3, 0.7),
            (-3.9, 0.8), (-3.0, 1.3), (-3.5, 1.1), (-2.7, 0.5), (-3.4, 1.4),
            (-3.6, 0.3), (-3.2, 0.9), (-3.8, 1.2), (-2.9, 0.7), (-3.3, 1.0)
        ]
        cluster_dots = VGroup(*[
            Dot(point=[x, y, 0], color=TEXT_MUTED, radius=0.05)
            for x, y in fixed_coords
        ])
        label_quantity = Text("More Data\n(Số lượng)", font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY).move_to(LEFT * 3 + DOWN * 0.8)

        # Right point: a single glowing emerald dot representing "Quality"
        right_dot = Dot(point=[3.0, 0.5, 0], color=THEME_EMERALD, radius=0.18)
        glow_right = create_3b1b_glow(right_dot, color=THEME_EMERALD, n_layers=4, opacity=0.35)
        label_quality = Text("Right Data\n(Chất lượng)", font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(RIGHT * 3 + DOWN * 0.8)

        # Write title and subtitle
        title_text = Text("More Data != Right Data", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(UP * 2.2)
        subtitle_text = Text("Số lượng hay chất lượng?", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(title_text, DOWN, buff=0.25)

        # Animate
        self.play(Write(title_text), FadeIn(subtitle_text, shift=UP * 0.1), run_time=1.0)
        self.play(FadeIn(cluster_dots, shift=RIGHT * 0.3), FadeIn(label_quantity), run_time=1.2)
        self.play(FadeIn(right_dot, scale=0.5), FadeIn(glow_right), FadeIn(label_quality), run_time=1.2)

        # seg 0: Title introduction
        play_voiceover_and_wait(self, 25, 0)

        # Clean up
        self.play(
            FadeOut(title_text), FadeOut(subtitle_text),
            FadeOut(cluster_dots), FadeOut(label_quantity),
            FadeOut(right_dot), FadeOut(glow_right), FadeOut(label_quality),
            run_time=TIME_FAST
        )
        self.wait(0.5)

        # Subtitle 1
        sub1 = create_bottom_caption("Số lượng data không đảm bảo robustness; dữ liệu đúng thường rất đắt.")
        self.play(FadeIn(sub1))
        # seg 1: "Thêm data có luôn giúp model robust..."
        play_voiceover_and_wait(self, 25, 1)

        # 2. Draw coordinate axes
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            x_length=8.1,
            y_length=4.2,
            axis_config={"color": TEXT_MUTED, "stroke_width": 2}
        ).shift(UP * 0.62)

        self.play(FadeIn(axes), run_time=TIME_NORMAL)

        # Core data cloud (standard training data)
        train_cloud = create_data_cloud([-2.0, -0.5], n_points=35, std=0.6, color=TEXT_SECONDARY, seed=42)
        train_label = Text("Training Data", font_size=20, color=TEXT_SECONDARY, font="Segoe UI", weight=BOLD).next_to(train_cloud, LEFT, buff=0.2)

        self.play(FadeIn(train_cloud), Write(train_label))

        # Decision boundary (initial)
        initial_boundary = Line(axes.c2p(-3.0, 1.0, 0), axes.c2p(1.0, -2.5, 0), color=THEME_BLUE, stroke_width=3)
        b_label = Text("Decision Boundary", font_size=20, color=THEME_BLUE, font="Segoe UI", weight=BOLD).move_to(axes.c2p(-1.8, 1.8, 0))

        self.play(Create(initial_boundary), FadeIn(b_label))
        # seg 2: "Đây là training data... boundary xanh fit..."
        play_voiceover_and_wait(self, 25, 2)

        # Target shift cloud (far away, Red)
        target_cloud = create_data_cloud([2.2, 1.5], n_points=20, std=0.5, color=THEME_RED, seed=45)
        target_label = Text("Target Shift", font_size=20, color=THEME_RED, font="Segoe UI", weight=BOLD).next_to(target_cloud, RIGHT, buff=0.2)

        self.play(FadeIn(target_cloud), Write(target_label))
        # seg 3: "Nhưng target shift đỏ nằm ngoài coverage..."
        play_voiceover_and_wait(self, 25, 3)

        # Visualizing "Adding More Data in Training Distribution"
        # Create additional grey dots inside the training cloud
        more_train_dots = create_data_cloud([-2.0, -0.5], n_points=40, std=0.7, color=TEXT_MUTED, seed=99)
        self.play(FadeIn(more_train_dots, scale=0.5), run_time=TIME_SLOW)

        # Indicate that the boundary does not change
        self.play(Indicate(initial_boundary, color=THEME_BLUE), run_time=TIME_NORMAL)

        # Red warning indicating the target shift is still uncovered / failed
        target_crosses = VGroup(*[Cross(dot, stroke_color=THEME_RED, stroke_width=2).scale(0.32) for dot in target_cloud[::3]])
        self.play(Create(target_crosses), run_time=TIME_NORMAL)
        # seg 4: "Ta thêm nhiều data... boundary không đổi..."
        play_voiceover_and_wait(self, 25, 4)

        # Subtitle 2
        sub2 = create_bottom_caption("Câu hỏi đúng hơn: cần thu thêm loại data nào, ở vùng nào, cho nhóm nào?")
        self.play(Transform(sub1, sub2))
        # seg 5: "Câu hỏi đúng không phải bao nhiêu data..."
        play_voiceover_and_wait(self, 25, 5)

        # Visualizing "Right Data" - a few green dots in the target shift region
        right_dots = create_data_cloud([1.2, 0.8], n_points=8, std=0.4, color=THEME_EMERALD, seed=10)
        right_label = Text("Right Data\n(Có mục tiêu)", font_size=20, color=THEME_EMERALD, font="Segoe UI", weight=BOLD).move_to(axes.c2p(2.5, -1.5, 0))
        right_arrow = Arrow(right_label.get_top(), right_dots.get_bottom(), color=THEME_EMERALD, stroke_width=2.4, buff=0.2)

        self.play(FadeOut(target_crosses), FadeIn(right_dots, scale=0.5), Write(right_label), Create(right_arrow), run_time=TIME_NORMAL)

        # Rotate / adjust boundary to correctly separate
        adjusted_boundary = Line(axes.c2p(-3.0, -1.0, 0), axes.c2p(3.0, 2.5, 0), color=THEME_EMERALD, stroke_width=4)

        self.play(
            Transform(initial_boundary, adjusted_boundary),
            b_label.animate.set_color(THEME_EMERALD).move_to(axes.c2p(-1.8, 2.2, 0)),
            run_time=TIME_SLOW
        )
        # seg 6: "Chỉ một ít right data đúng vùng shift..."
        play_voiceover_and_wait(self, 25, 6)

        # Warning takeaway
        warning = create_insight_box(
            "More data không đồng nghĩa với right data.",
            color=THEME_RED,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)

        self.play(FadeOut(sub1), FadeIn(warning, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 7: "More data không đồng nghĩa right data..."
        play_voiceover_and_wait(self, 25, 7)

        # Outro
        self.play(
            FadeOut(warning), FadeOut(axes),
            FadeOut(train_cloud), FadeOut(train_label), FadeOut(more_train_dots),
            FadeOut(initial_boundary), FadeOut(b_label),
            FadeOut(target_cloud), FadeOut(target_label),
            FadeOut(right_dots), FadeOut(right_label), FadeOut(right_arrow),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
