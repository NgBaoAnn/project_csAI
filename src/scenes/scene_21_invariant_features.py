"""
Scene 21: Invariant Features
Author: TV3 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
import numpy as np


class InvariantFeaturesScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Neon Drawing Frame + Title Write
        title_text = Text("Invariant Features", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD)
        subtitle_text = Text("Feature nào còn đúng khi environment đổi?", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        intro_group = VGroup(title_text, subtitle_text).arrange(DOWN, buff=0.3)
        frame = SurroundingRectangle(intro_group, color=THEME_EMERALD, buff=0.4, corner_radius=0.1)
        glow = create_3b1b_glow(frame, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        
        self.play(Create(frame), FadeIn(glow), run_time=1.0)
        self.play(Write(title_text), FadeIn(subtitle_text, shift=UP * 0.1), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(intro_group), FadeOut(frame), FadeOut(glow), run_time=TIME_FAST)
        self.wait(1.0)
        
        # Grid layout for three environments
        env_width = 3.2
        env_height = 3.65
        spacing = 4.2
        
        # Subtitle 1
        sub1 = create_bottom_caption("Invariant learning bắt đầu từ ý tưởng: stable features nên hữu ích qua nhiều environments.")
        self.play(FadeIn(sub1))
        self.wait(4.0)
        
        # Create 3 Environment Panels
        envs = VGroup()
        env_titles = VGroup()
        env_bgs = VGroup()
        env_shapes = VGroup()
        
        # Env 1: Grassland (Greenish)
        e1_box = RoundedRectangle(width=env_width, height=env_height, corner_radius=0.1, stroke_color=THEME_BLUE, stroke_width=2)
        e1_bg = VGroup(*[
            Line([-0.8 + 0.2*i, -1.8, 0], [-0.8 + 0.2*i, -1.2, 0], color=THEME_EMERALD, stroke_width=2).rotate(0.2)
            for i in range(9)
        ]).move_to(e1_box.get_center() + DOWN * 0.8)
        e1_title = Text("Environment 1\n(Đồng cỏ)", font_size=SIZE_SMALL, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(e1_box.get_top() + DOWN * 0.42)
        e1_shape_circle = Circle(radius=0.7, color=THEME_EMERALD, fill_color=BG_DARKER, fill_opacity=1.0, stroke_width=3).move_to(e1_box.get_center() + UP * 0.35)
        e1_shape_label = Text("Hình dáng bò", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(e1_shape_circle.get_center())
        fit_to_width(e1_shape_label, max_width=e1_shape_circle.get_width() * 0.8)
        e1_shape = VGroup(e1_shape_circle, e1_shape_label)
        
        env1 = VGroup(e1_box, e1_bg, e1_title, e1_shape).shift(LEFT * spacing)
        
        # Env 2: Desert (Yellowish)
        e2_box = RoundedRectangle(width=env_width, height=env_height, corner_radius=0.1, stroke_color=THEME_AMBER, stroke_width=2)
        e2_bg = VGroup(*[
            Dot(point=[x, y, 0], color=THEME_AMBER, radius=0.03)
            for x in np.linspace(-1.2, 1.2, 8) for y in np.linspace(-1.5, -0.7, 4)
        ]).move_to(e2_box.get_center() + DOWN * 0.4)
        e2_title = Text("Environment 2\n(Sa mạc)", font_size=SIZE_SMALL, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).move_to(e2_box.get_top() + DOWN * 0.42)
        e2_shape_circle = Circle(radius=0.7, color=THEME_EMERALD, fill_color=BG_DARKER, fill_opacity=1.0, stroke_width=3).move_to(e2_box.get_center() + UP * 0.35)
        e2_shape_label = Text("Hình dáng lạc đà", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(e2_shape_circle.get_center())
        fit_to_width(e2_shape_label, max_width=e2_shape_circle.get_width() * 0.8)
        e2_shape = VGroup(e2_shape_circle, e2_shape_label)
        
        env2 = VGroup(e2_box, e2_bg, e2_title, e2_shape)
        
        # Env 3: Coast (Orange/Blueish)
        e3_box = RoundedRectangle(width=env_width, height=env_height, corner_radius=0.1, stroke_color=THEME_ORANGE, stroke_width=2)
        e3_bg = VGroup(*[
            FunctionGraph(lambda x: 0.1 * np.sin(4*x) + y, x_range=[-1.4, 1.4], color=THEME_BLUE, stroke_width=1.5)
            for y in (-1.1, -1.4, -1.7)
        ]).move_to(e3_box.get_center() + DOWN * 0.4)
        e3_title = Text("Environment 3\n(Bờ biển)", font_size=SIZE_SMALL, color=THEME_ORANGE, font=FONT_PRIMARY, weight=BOLD).move_to(e3_box.get_top() + DOWN * 0.42)
        e3_shape_circle = Circle(radius=0.7, color=THEME_EMERALD, fill_color=BG_DARKER, fill_opacity=1.0, stroke_width=3).move_to(e3_box.get_center() + UP * 0.35)
        e3_shape_label = Text("Hình dáng bò", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(e3_shape_circle.get_center())
        fit_to_width(e3_shape_label, max_width=e3_shape_circle.get_width() * 0.8)
        e3_shape = VGroup(e3_shape_circle, e3_shape_label)
        
        env3 = VGroup(e3_box, e3_bg, e3_title, e3_shape).shift(RIGHT * spacing)
        
        all_envs = VGroup(env1, env2, env3)
        all_envs.arrange(RIGHT, buff=0.55)
        fit_to_frame(all_envs, max_width=12.3, max_height=4.7)
        all_envs.move_to(UP * 0.38)
        
        # Fade in environments slowly
        self.play(FadeIn(env1[0]), FadeIn(env1[2]), run_time=TIME_NORMAL)
        self.play(FadeIn(env1[1]), FadeIn(env1[3]), run_time=TIME_NORMAL)
        self.wait(3.5)
        
        self.play(FadeIn(env2[0]), FadeIn(env2[2]), run_time=TIME_NORMAL)
        self.play(FadeIn(env2[1]), FadeIn(env2[3]), run_time=TIME_NORMAL)
        self.wait(3.5)
        
        self.play(FadeIn(env3[0]), FadeIn(env3[2]), run_time=TIME_NORMAL)
        self.play(FadeIn(env3[1]), FadeIn(env3[3]), run_time=TIME_NORMAL)
        self.wait(5.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Background có thể đổi theo môi trường: cỏ, cát, bờ biển, ánh sáng.")
        self.play(Transform(sub1, sub2))
        self.wait(4.5)
        
        # Indicate changing backgrounds (Spurious Features)
        cross1 = Cross(env1[1], stroke_color=THEME_RED, stroke_width=4).scale(0.8)
        cross2 = Cross(env2[1], stroke_color=THEME_RED, stroke_width=4).scale(0.8)
        cross3 = Cross(env3[1], stroke_color=THEME_RED, stroke_width=4).scale(0.8)
        
        spurious_label = Text("Spurious (Unstable) Features", font_size=SIZE_SMALL, color=THEME_RED, font=FONT_PRIMARY).next_to(all_envs, DOWN, buff=0.25)
        
        self.play(
            Create(cross1), Create(cross2), Create(cross3),
            FadeIn(spurious_label, shift=UP * 0.1),
            run_time=TIME_NORMAL
        )
        self.wait(7.0)
        
        # Subtitle 3
        sub3 = create_bottom_caption("Nhưng feature ổn định vẫn sống sót qua những thay đổi đó.")
        self.play(Transform(sub1, sub3))
        self.wait(4.5)
        
        # Glow the shapes (Invariant Features)
        glow1 = create_3b1b_glow(env1[3][0], color=THEME_EMERALD, n_layers=4)
        glow2 = create_3b1b_glow(env2[3][0], color=THEME_EMERALD, n_layers=4)
        glow3 = create_3b1b_glow(env3[3][0], color=THEME_EMERALD, n_layers=4)
        
        stable_label = Text("Invariant (Stable) Features", font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(all_envs, DOWN, buff=0.25)
        
        self.play(
            FadeIn(glow1), FadeIn(glow2), FadeIn(glow3),
            env1[3][0].animate.set_color(THEME_EMERALD),
            env2[3][0].animate.set_color(THEME_EMERALD),
            env3[3][0].animate.set_color(THEME_EMERALD),
            FadeOut(spurious_label),
            FadeIn(stable_label, shift=UP * 0.1),
            run_time=TIME_NORMAL
        )
        # Pulsate shapes to emphasize stability (adds 2.0s of animation)
        self.play(
            env1[3].animate.scale(1.1),
            env2[3].animate.scale(1.1),
            env3[3].animate.scale(1.1),
            run_time=1.0
        )
        self.play(
            env1[3].animate.scale(1/1.1),
            env2[3].animate.scale(1/1.1),
            env3[3].animate.scale(1/1.1),
            run_time=1.0
        )
        self.wait(7.5)
        
        # Takeaway
        insight = create_insight_box(
            "Stable features tồn tại qua sự thay đổi environment",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(
            FadeOut(sub1),
            FadeOut(stable_label),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(9.5)
        
        # Outro
        self.play(
            FadeOut(insight), FadeOut(all_envs),
            FadeOut(glow1), FadeOut(glow2), FadeOut(glow3),
            FadeOut(cross1), FadeOut(cross2), FadeOut(cross3),
            run_time=TIME_NORMAL
        )
        self.wait(2.5)
