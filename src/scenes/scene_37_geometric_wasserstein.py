"""
Scene 37: Geometric Wasserstein
Author: TV4 (Animation Lead)
Duration: ~75 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class GeometricWassersteinScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Custom phase-shifted sine wave animation
        intro_axes = Axes(x_range=[-4, 4, 1], y_range=[-1.5, 1.5, 1], x_length=8.0, y_length=3.0)
        sine_wave = intro_axes.plot(lambda x: 0.8 * np.sin(2 * x), x_range=[-3.5, 3.5], color=THEME_EMERALD, stroke_width=3.5)
        
        self.play(Create(sine_wave), run_time=TIME_NORMAL)
        
        phase = ValueTracker(0)
        def get_sine_graph():
            p = phase.get_value()
            return intro_axes.plot(lambda x: 0.8 * np.sin(2 * x - p), x_range=[-3.5, 3.5], color=THEME_EMERALD, stroke_width=3.5)
            
        self.remove(sine_wave)
        sine_live = always_redraw(get_sine_graph)
        self.add(sine_live)
        
        title_text = Text("Geometric Wasserstein", font_size=SIZE_TITLE - 4, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_EMERALD, THEME_BLUE)
        title_glow = create_3b1b_glow(title_text, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        
        subtitle_text = Text("Tích hợp cấu trúc hình học vào robust learning", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)
        
        self.play(
            phase.animate.set_value(2.5 * PI),
            FadeIn(title_group, scale=0.9),
            Write(subtitle_text),
            run_time=2.2,
            rate_func=linear
        )
        
        self.play(
            FadeOut(sine_live),
            FadeOut(title_group),
            FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        
        # Subtitle 1
        sub1 = create_bottom_caption("Geometric Wasserstein đưa cấu trúc hình học manifold của dữ liệu vào DRO.")
        self.play(FadeIn(sub1))
        self.wait(7.0)
        
        # Draw Axes
        axes = Axes(x_range=[-3.5, 3.5, 1], y_range=[-2, 2.5, 1], x_length=8.0, y_length=4.5, axis_config={"color": TEXT_MUTED}).shift(UP * 0.5)
        self.play(FadeIn(axes), run_time=TIME_NORMAL)
        
        # Draw Manifold Curve
        manifold_curve = axes.plot(lambda x: 0.15 * x**2 - 1.2, x_range=[-3.0, 3.0], color=THEME_BLUE, stroke_width=3.5)
        manifold_label = Text("Manifold dữ liệu", font_size=SIZE_SMALL - 6, color=THEME_BLUE, font=FONT_PRIMARY).next_to(manifold_curve.get_start(), UP, buff=0.25).shift(LEFT * 0.3)
        
        self.play(Create(manifold_curve), Write(manifold_label), run_time=TIME_NORMAL)
        self.wait(6.0)
        
        # Draw points on manifold (Green)
        xs = [-2.5, -1.5, -0.5, 0.5, 1.5, 2.5]
        dots = VGroup(*[
            Dot(axes.c2p(x, 0.15 * x**2 - 1.2), color=THEME_EMERALD, radius=0.07)
            for x in xs
        ])
        
        # Draw noisy outlier (Red)
        noisy_dot = Dot(axes.c2p(0, 1.5), color=THEME_RED, radius=0.08)
        noisy_label = Text("Mẫu nhiễu ngoại lai\n(Bị cô lập)", font_size=SIZE_SMALL - 6, color=THEME_RED, font=FONT_PRIMARY).next_to(noisy_dot, LEFT, buff=0.25)
        
        self.play(FadeIn(dots), FadeIn(noisy_dot), Write(noisy_label), run_time=TIME_NORMAL)
        self.wait(7.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Mẫu khó (hard samples) thường nằm trên manifold; mẫu nhiễu thì cô lập.")
        self.play(Transform(sub1, sub2))
        self.wait(8.0)
        
        # Show Standard Wasserstein: direct transport to outlier (Bad!)
        std_arrows = VGroup(
            Arrow(dots[1].get_center(), noisy_dot.get_center(), color=THEME_RED, stroke_width=2, buff=0.15),
            Arrow(dots[4].get_center(), noisy_dot.get_center(), color=THEME_RED, stroke_width=2, buff=0.15)
        )
        std_label = Text("Standard Wasserstein\n(Bị hút vào mẫu nhiễu)", font_size=SIZE_SMALL - 6, color=THEME_RED, font=FONT_PRIMARY).shift(RIGHT * 3.2 + UP * 1.8)
        
        self.play(Create(std_arrows), Write(std_label), run_time=TIME_NORMAL)
        self.wait(7.5)
        
        # Fade out Standard arrows
        self.play(FadeOut(std_arrows), FadeOut(std_label), run_time=TIME_FAST)
        self.wait(0.5)
        
        # Subtitle 3
        sub3 = create_bottom_caption("Geometric Wasserstein buộc dòng vận chuyển xác suất phải chạy dọc theo manifold.")
        self.play(Transform(sub1, sub3))
        
        # Show Geometric Wasserstein: arrows follow manifold
        geo_arrows = VGroup()
        for i in range(len(dots) - 1):
            arrow = CurvedArrow(dots[i].get_center(), dots[i+1].get_center(), angle=-TAU/7, color=THEME_EMERALD, stroke_width=3)
            geo_arrows.add(arrow)
            
        geo_label = Text("Geometric Wasserstein\n(Tôn trọng hình học, bỏ qua ngoại lai)", font_size=SIZE_SMALL - 6, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).shift(RIGHT * 3.2 + UP * 1.8)
        
        self.play(Create(geo_arrows), Write(geo_label), run_time=TIME_NORMAL)
        
        # Glow the manifold curve to show restriction
        glow_curve = create_3b1b_glow(manifold_curve, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        self.play(FadeIn(glow_curve), run_time=TIME_NORMAL)
        self.wait(11.0)
        
        # Takeaway
        insight = create_insight_box(
            "Độ robust nên tôn trọng hình học dữ liệu.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(13.0)
        
        # Outro
        self.play(
            FadeOut(axes), FadeOut(manifold_curve), FadeOut(manifold_label), FadeOut(dots),
            FadeOut(noisy_dot), FadeOut(noisy_label), FadeOut(geo_arrows), FadeOut(geo_label),
            FadeOut(glow_curve), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
