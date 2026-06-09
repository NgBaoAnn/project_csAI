"""
Scene 23: IRM Limits
Author: TV3 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class IRMLimitsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Warning Slit Split
        split_line = Line(LEFT * 6, RIGHT * 6, color=THEME_RED, stroke_width=3)
        title_text = Text("IRM Limits", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD)
        subtitle_text = Text("Điều gì xảy ra nếu environments không đủ tốt?", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        
        # Position title above line, subtitle below
        title_text.next_to(split_line, UP, buff=0.2)
        subtitle_text.next_to(split_line, DOWN, buff=0.2)
        
        self.play(Create(split_line), run_time=0.8)
        self.wait(0.2)
        
        glow_line = create_3b1b_glow(split_line, color=THEME_RED, n_layers=4, opacity=0.15)
        self.play(
            split_line.animate.set_color(THEME_AMBER),
            FadeIn(glow_line),
            title_text.animate.shift(UP * 0.1),
            subtitle_text.animate.shift(DOWN * 0.1),
            Write(title_text),
            FadeIn(subtitle_text),
            run_time=1.5
        )
        self.play(split_line.animate.set_color(THEME_ORANGE), run_time=0.4)
        self.play(split_line.animate.set_color(THEME_RED), run_time=0.4)
        self.wait(1.5)
        
        self.play(
            FadeOut(title_text),
            FadeOut(subtitle_text),
            FadeOut(split_line),
            FadeOut(glow_line),
            run_time=TIME_FAST
        )
        self.wait(1.0)
        
        # Subtitle 1
        sub1 = create_bottom_caption("Nếu mọi training environment giữ cùng một shortcut, shortcut đó cũng trông invariant.")
        self.play(FadeIn(sub1))
        self.wait(6.5)
        
        # Grid layout for three training environments
        panel_w, panel_h = 3.25, 2.1
        spacing = 4.2
        
        e1_box = RoundedRectangle(width=panel_w, height=panel_h, corner_radius=0.1, stroke_color=THEME_BLUE, stroke_width=2)
        e1_label = Text("Environment 1", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(e1_box.get_top() + DOWN * 0.4)
        e1_feat1 = Text("Nền cỏ (90%)", font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY)
        fit_to_width(e1_feat1, max_width=e1_box.get_width() * 0.82)
        e1_feat2 = Text("Hình dáng bò", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(e1_box.get_center() + DOWN * 0.5)
        fit_to_width(e1_feat2, max_width=e1_box.get_width() * 0.82)
        env1 = VGroup(e1_box, e1_label, e1_feat1, e1_feat2).shift(LEFT * spacing + UP * 1.5)
        
        e2_box = RoundedRectangle(width=panel_w, height=panel_h, corner_radius=0.1, stroke_color=THEME_BLUE, stroke_width=2)
        e2_label = Text("Environment 2", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(e2_box.get_top() + DOWN * 0.4)
        e2_feat1 = Text("Nền cỏ (90%)", font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY)
        fit_to_width(e2_feat1, max_width=e2_box.get_width() * 0.82)
        e2_feat2 = Text("Hình dáng bò", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(e2_box.get_center() + DOWN * 0.5)
        fit_to_width(e2_feat2, max_width=e2_box.get_width() * 0.82)
        env2 = VGroup(e2_box, e2_label, e2_feat1, e2_feat2).shift(UP * 1.5)
        
        e3_box = RoundedRectangle(width=panel_w, height=panel_h, corner_radius=0.1, stroke_color=THEME_BLUE, stroke_width=2)
        e3_label = Text("Environment 3", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(e3_box.get_top() + DOWN * 0.4)
        e3_feat1 = Text("Nền cỏ (90%)", font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY)
        fit_to_width(e3_feat1, max_width=e3_box.get_width() * 0.82)
        e3_feat2 = Text("Hình dáng bò", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(e3_box.get_center() + DOWN * 0.5)
        fit_to_width(e3_feat2, max_width=e3_box.get_width() * 0.82)
        env3 = VGroup(e3_box, e3_label, e3_feat1, e3_feat2).shift(RIGHT * spacing + UP * 1.5)
        
        train_envs = VGroup(env1, env2, env3)
        train_envs.arrange(RIGHT, buff=0.45).move_to(UP * 1.22)
        fit_to_frame(train_envs, max_width=11.2, max_height=2.6)
        self.play(FadeIn(train_envs, shift=DOWN * 0.2), run_time=TIME_SLOW)
        self.wait(6.5)
        
        # Highlight "Grass Background" as looking invariant
        inv_frame = SurroundingRectangle(VGroup(e1_feat1, e2_feat1, e3_feat1), color=THEME_EMERALD, buff=0.15)
        inv_text = Text("Có vẻ invariant khi train", font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(train_envs, DOWN, buff=0.18)
        
        self.play(Create(inv_frame), Write(inv_text), run_time=TIME_NORMAL)
        self.wait(7.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("IRM cần environments đủ đa dạng để lộ ra feature không ổn định.")
        self.play(Transform(sub1, sub2))
        self.wait(6.5)
        
        # Shift training envs and bring in Test env
        test_box = RoundedRectangle(width=panel_w, height=panel_h, corner_radius=0.1, stroke_color=THEME_RED, stroke_width=3)
        test_label = Text("Test Environment", font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).move_to(test_box.get_top() + DOWN * 0.4)
        test_feat1 = Text("Nền bãi biển (100%)", font_size=SIZE_SMALL, color=THEME_RED, font=FONT_PRIMARY)
        fit_to_width(test_feat1, max_width=test_box.get_width() * 0.82)
        test_feat2 = Text("Hình dáng bò", font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY).move_to(test_box.get_center() + DOWN * 0.5)
        fit_to_width(test_feat2, max_width=test_box.get_width() * 0.82)
        env_test = VGroup(test_box, test_label, test_feat1, test_feat2).move_to(DOWN * 0.8)
        
        self.play(
            train_envs.animate.scale(0.82).shift(UP * 0.55),
            inv_frame.animate.scale(0.82).shift(UP * 0.55),
            FadeOut(inv_text),
            FadeIn(env_test, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(6.0)
        
        # Failure indicator on beach background
        cross = Cross(test_feat1, stroke_color=THEME_RED, stroke_width=5)
        fail_text = Text("Shortcut bị phá vỡ!", font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).next_to(test_box, RIGHT, buff=0.4)
        
        self.play(Create(cross), Write(fail_text), run_time=TIME_NORMAL)
        self.wait(8.5)
        
        # Takeaway
        insight = create_insight_box(
            "Environments xấu tạo ra invariance kém.",
            color=THEME_RED,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(10.5)
        
        # Outro
        self.play(
            FadeOut(insight), FadeOut(train_envs),
            FadeOut(inv_frame), FadeOut(env_test), FadeOut(cross), FadeOut(fail_text),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
