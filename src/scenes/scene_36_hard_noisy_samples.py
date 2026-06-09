"""
Scene 36: Hard vs Noisy Samples
Author: TV4 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class HardNoisySamplesScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Custom warning triangle rotation morphing intro
        triangle_points = [
            UP * 1.5,
            LEFT * 1.7 + DOWN * 1.2,
            RIGHT * 1.7 + DOWN * 1.2,
            UP * 1.5
        ]
        warning_tri = VMobject(color=THEME_RED, stroke_width=4.5)
        warning_tri.set_points_as_corners(triangle_points)
        
        exclamation = Text("!", font_size=60, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).move_to(warning_tri.get_center() + DOWN * 0.15)
        exclamation_glow = create_3b1b_glow(exclamation, color=THEME_RED, n_layers=4, opacity=0.25)
        exclamation_group = VGroup(exclamation_glow, exclamation)
        
        self.play(Create(warning_tri), run_time=1.5)
        self.play(FadeIn(exclamation_group, scale=0.8), run_time=TIME_FAST)
        self.wait(0.3)
        
        warning_group = VGroup(warning_tri, exclamation_group)
        title_text = Text("Hard vs Noisy", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_RED, THEME_ORANGE)
        title_glow = create_3b1b_glow(title_text, color=THEME_RED, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        
        subtitle_text = Text("Loss cao chưa chắc là nhóm thiểu số", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)
        
        self.play(
            Rotate(warning_group, angle=-PI/2),
            FadeOut(warning_group, scale=0.8),
            FadeIn(title_group, scale=0.9),
            FadeIn(subtitle_text, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
        self.play(
            FadeOut(title_group),
            FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        
        # Subtitle 1
        sub1 = create_bottom_caption("Trong robust learning, ta thường tập trung vào các mẫu có loss cao.")
        self.play(FadeIn(sub1))
        self.wait(6.0)
        
        # Draw Coordinate Axes (Shifted slightly UP * 0.75 to prevent bottom overlaps)
        axes = Axes(x_range=[-3, 3, 1], y_range=[-2.5, 2.5, 1], x_length=7.2, y_length=4.2, axis_config={"color": TEXT_MUTED}).shift(UP * 0.75)
        self.play(FadeIn(axes), run_time=TIME_NORMAL)
        
        # Draw Majority Cluster (Blue)
        np.random.seed(36)
        maj_dots = VGroup(*[
            Dot(axes.c2p(-1.2 + np.random.normal(0, 0.4), -0.5 + np.random.normal(0, 0.45)), color=THEME_BLUE, radius=0.065)
            for _ in range(20)
        ])
        maj_label = Text("Nhóm đa số\n(Loss thấp)", font_size=SIZE_SMALL - 6, color=THEME_BLUE, font=FONT_PRIMARY).next_to(maj_dots, LEFT, buff=0.15).shift(DOWN * 0.5)
        
        self.play(FadeIn(maj_dots), Write(maj_label), run_time=TIME_NORMAL)
        self.wait(5.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Nhưng các điểm có loss cao có thể đến từ hai nguồn rất khác nhau.")
        self.play(Transform(sub1, sub2))
        self.wait(6.0)
        
        # Draw Minority/Hard Cluster (Green)
        hard_dots = VGroup(*[
            Dot(axes.c2p(1.5 + np.random.normal(0, 0.35), 0.8 + np.random.normal(0, 0.35)), color=THEME_EMERALD, radius=0.065)
            for _ in range(6)
        ])
        
        # Draw Outlier/Noisy Point (Red)
        noisy_dot = Dot(axes.c2p(-1.8, 1.8), color=THEME_RED, radius=0.08)
        
        self.play(FadeIn(hard_dots), FadeIn(noisy_dot), run_time=TIME_NORMAL)
        self.wait(4.0)
        
        # Highlight both as "High Loss"
        ring_hard = Circle(radius=0.9, color=THEME_AMBER, stroke_width=2.5, stroke_opacity=0.85).move_to(hard_dots.get_center())
        ring_noisy = Circle(radius=0.35, color=THEME_AMBER, stroke_width=2.5, stroke_opacity=0.85).move_to(noisy_dot.get_center())
        high_loss_text = Text("Vùng có Loss cao", font_size=SIZE_SMALL - 4, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).to_edge(UP, buff=0.8)
        
        self.play(
            Create(ring_hard), Create(ring_noisy),
            Write(high_loss_text),
            run_time=TIME_NORMAL
        )
        self.wait(5.5)
        
        # Subtitle 3
        sub3 = create_bottom_caption("Đó có thể là hard samples thuộc nhóm thiểu số quan trọng cần tối ưu...")
        self.play(Transform(sub1, sub3))
        
        hard_label = Text("Hard Samples\n(Nhóm thiểu số)", font_size=SIZE_SMALL - 6, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).next_to(ring_hard, DOWN, buff=0.25)
        self.play(Write(hard_label), run_time=TIME_NORMAL)
        self.wait(6.5)
        
        # Subtitle 4
        sub4 = create_bottom_caption("...hoặc chỉ là noisy samples cô lập, làm chệch hướng mô hình nếu cố fit.")
        self.play(Transform(sub1, sub4))
        
        noisy_label = Text("Noisy Sample\n(Điểm ngoại lai)", font_size=SIZE_SMALL - 6, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).next_to(ring_noisy, RIGHT, buff=0.3)
        self.play(Write(noisy_label), run_time=TIME_NORMAL)
        self.wait(7.5)
        
        # Takeaway (Shifted down to buff=0.5 to prevent bottom axes overlap)
        insight = create_insight_box(
            "Loss cao là không rõ ràng.",
            color=THEME_RED,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.5)
        
        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(12.5)
        
        # Outro
        self.play(
            FadeOut(axes), FadeOut(maj_dots), FadeOut(maj_label), FadeOut(hard_dots), FadeOut(hard_label),
            FadeOut(noisy_dot), FadeOut(noisy_label), FadeOut(ring_hard), FadeOut(ring_noisy),
            FadeOut(high_loss_text), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
