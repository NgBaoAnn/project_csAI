"""
Scene 30: Predictive Heterogeneity
Author: TV3 (Animation Lead)
Duration: ~80 seconds
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


class PredictiveHeterogeneityScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: Decision Node Split
        parent_node = Circle(radius=0.6, color=TEXT_SECONDARY, fill_color=BG_PANEL, fill_opacity=0.8, stroke_width=3).shift(UP * 0.4)
        lbl_parent = Text("Dữ liệu (Data)", font_size=SIZE_SMALL, color=TEXT_PRIMARY, font="Segoe UI", weight=BOLD).move_to(parent_node.get_center())

        arrow_left = Arrow(parent_node.get_bottom(), LEFT * 2.0 + DOWN * 1.2, color=TEXT_MUTED, stroke_width=3, buff=0.1)
        arrow_right = Arrow(parent_node.get_bottom(), RIGHT * 2.0 + DOWN * 1.2, color=TEXT_MUTED, stroke_width=3, buff=0.1)

        child_left = Circle(radius=0.5, color=THEME_BLUE, fill_color=BG_PANEL, fill_opacity=0.8, stroke_width=3).move_to(LEFT * 2.0 + DOWN * 1.2)
        lbl_left = Text("Env 1", font_size=SIZE_SMALL - 4, color=THEME_BLUE, font="Segoe UI", weight=BOLD).move_to(child_left.get_center())

        child_right = Circle(radius=0.5, color=THEME_AMBER, fill_color=BG_PANEL, fill_opacity=0.8, stroke_width=3).move_to(RIGHT * 2.0 + DOWN * 1.2)
        lbl_right = Text("Env 2", font_size=SIZE_SMALL - 4, color=THEME_AMBER, font="Segoe UI", weight=BOLD).move_to(child_right.get_center())

        title_text = Text("Predictive Heterogeneity", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font="Segoe UI", weight=BOLD).move_to(UP * 2.2)
        subtitle_text = Text("Tìm ra cấu trúc ẩn qua mô hình dự đoán", font_size=SIZE_BODY - 4, color=TEXT_PRIMARY, font="Segoe UI", weight=MEDIUM).next_to(title_text, DOWN, buff=0.25)

        # Animate
        self.play(FadeIn(parent_node), FadeIn(lbl_parent), run_time=0.8)
        self.play(
            GrowArrow(arrow_left), GrowArrow(arrow_right),
            Write(title_text), FadeIn(subtitle_text, shift=UP * 0.1),
            run_time=1.5
        )
        glow_l = create_3b1b_glow(child_left, color=THEME_BLUE, n_layers=4, opacity=0.15)
        glow_r = create_3b1b_glow(child_right, color=THEME_AMBER, n_layers=4, opacity=0.15)
        self.play(
            FadeIn(child_left), FadeIn(lbl_left), FadeIn(glow_l),
            FadeIn(child_right), FadeIn(lbl_right), FadeIn(glow_r),
            parent_node.animate.set_color(TEXT_MUTED).set_opacity(0.4),
            lbl_parent.animate.set_color(TEXT_MUTED).set_opacity(0.4),
            run_time=1.0
        )

        # seg 0: Title introduction (gộp câu hỏi mở đầu)
        play_voiceover_and_wait(self, 30, 0)

        # Clean up
        self.play(
            FadeOut(parent_node), FadeOut(lbl_parent),
            FadeOut(arrow_left), FadeOut(arrow_right),
            FadeOut(child_left), FadeOut(lbl_left), FadeOut(glow_l),
            FadeOut(child_right), FadeOut(lbl_right), FadeOut(glow_r),
            FadeOut(title_text), FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        self.wait(0.5)

        # Subtitle 1
        sub1 = create_subtitle("Predictive heterogeneity tìm split E sao cho biết E làm tăng thông tin dự đoán của X về Y.")
        self.play(FadeIn(sub1))
        # seg 1: "Predictive heterogeneity tìm split E... I conditional > I..."
        play_voiceover_and_wait(self, 30, 1)

        # 2. Draw axes and pooled data points (grey)
        axes = Axes(x_range=[-3, 3, 1], y_range=[-3, 3, 1], x_length=5.0, y_length=3.2, axis_config={"color": TEXT_MUTED}).shift(LEFT * 1.8 + UP * 0.4)
        self.play(FadeIn(axes), run_time=TIME_NORMAL)

        # Coordinates for two groups (slopes)
        # Group 1: positive slope (y = x)
        g1_coords = [(-1.5, -1.2), (-1.0, -0.8), (-0.5, -0.4), (0.0, 0.0), (0.5, 0.4), (1.0, 0.9), (1.5, 1.3)]
        # Group 2: negative slope (y = -0.5x)
        g2_coords = [(-2.0, 0.8), (-1.2, 0.5), (-0.4, 0.2), (0.4, -0.3), (1.2, -0.6), (2.0, -0.9)]

        # Make them initially grey
        np.random.seed(30)
        all_dots = VGroup(*[
            Dot(axes.c2p(x, y + np.random.normal(0, 0.15), 0), color=TEXT_SECONDARY, radius=0.06)
            for x, y in g1_coords + g2_coords
        ])

        self.play(FadeIn(all_dots, scale=0.5), run_time=TIME_NORMAL)

        # Overall average regression line (poor fit)
        avg_line = Line(axes.c2p(-2.5, -0.2, 0), axes.c2p(2.5, 0.1, 0), color=TEXT_MUTED, stroke_width=2, stroke_opacity=0.6)

        # Label on the right panel
        avg_label = Text("Average Fit (Kém)", font_size=20, color=TEXT_PRIMARY, font="Segoe UI", weight=BOLD).move_to(RIGHT * 3.8 + UP * 1.5)
        avg_arrow = Arrow(avg_label.get_left(), axes.c2p(1.5, 0.0), color=TEXT_MUTED, stroke_width=2, buff=0.1)

        self.play(Create(avg_line), Write(avg_label), GrowArrow(avg_arrow))
        # seg 2: "Nhìn vào toàn bộ dữ liệu xám: đường trung bình fit kém..."
        play_voiceover_and_wait(self, 30, 2)

        # 3. Bad Split Demonstration
        # Random vertical partition
        bad_split_line = Line(axes.c2p(0, -1.8, 0), axes.c2p(0, 1.8, 0), color=THEME_RED, stroke_width=3)

        bad_title = Text("Bad Split: E ngẫu nhiên", font_size=22, color=THEME_RED, font="Segoe UI", weight=BOLD).move_to(RIGHT * 3.8 + UP * 1.5)
        bad_desc = Text("Trộn các subgroups thất bại trong việc\nlàm lộ ra cấu trúc ẩn.", font_size=18, color=TEXT_PRIMARY, font="Segoe UI", weight=MEDIUM).next_to(bad_title, DOWN, buff=0.25)
        bad_formula = MathTex(r"I(Y; X \mid E) \approx I(Y; X)", font_size=SIZE_SUBSECTION, color=THEME_RED).next_to(bad_desc, DOWN, buff=0.35)
        fit_to_width(bad_formula, max_width=4.4)

        self.play(
            FadeOut(avg_label), FadeOut(avg_arrow),
            Create(bad_split_line),
            Write(bad_title), FadeIn(bad_desc), Write(bad_formula),
            run_time=TIME_NORMAL
        )
        # seg 3: "Split ngẫu nhiên không giúp ích, I conditional gần bằng I..."
        play_voiceover_and_wait(self, 30, 3)

        # Fade out bad split
        self.play(
            FadeOut(bad_split_line),
            FadeOut(bad_title), FadeOut(bad_desc), FadeOut(bad_formula),
            run_time=TIME_FAST
        )

        # Subtitle 2
        sub2 = create_subtitle("Nếu split làm tăng lượng thông tin dự đoán, groups đó phản ánh cơ chế khác nhau.")
        self.play(Transform(sub1, sub2))
        self.wait(1.0)

        # 4. Good Split Demonstration
        # Color the dots by environment
        g1_dots = VGroup(*all_dots[:len(g1_coords)])
        g2_dots = VGroup(*all_dots[len(g1_coords):])

        # Separate regression lines
        g1_line = Line(axes.c2p(-2.0, -1.7, 0), axes.c2p(2.0, 1.7, 0), color=THEME_BLUE, stroke_width=3)
        g2_line = Line(axes.c2p(-2.5, 1.15, 0), axes.c2p(2.5, -1.15, 0), color=THEME_AMBER, stroke_width=3)

        # Good split labels on the right
        good_title = Text("Good Split: E ẩn", font_size=22, color=THEME_EMERALD, font="Segoe UI", weight=BOLD).move_to(RIGHT * 3.8 + UP * 1.8)
        good_desc = Text("Lộ ra hai cơ chế\ndự đoán khác biệt.", font_size=18, color=TEXT_PRIMARY, font="Segoe UI", weight=MEDIUM).next_to(good_title, DOWN, buff=0.25)
        g1_formula = MathTex(r"Env\ 1:\ P(Y \mid X, E=1)", font_size=SIZE_BODY - 4, color=THEME_BLUE).next_to(good_desc, DOWN, buff=0.35).align_to(good_desc, LEFT)
        g2_formula = MathTex(r"Env\ 2:\ P(Y \mid X, E=2)", font_size=SIZE_BODY - 4, color=THEME_AMBER).next_to(g1_formula, DOWN, buff=0.25).align_to(good_desc, LEFT)

        self.play(
            g1_dots.animate.set_color(THEME_BLUE).scale(1.15),
            g2_dots.animate.set_color(THEME_AMBER).scale(1.15),
            FadeOut(avg_line),
            run_time=TIME_NORMAL
        )
        self.play(
            Create(g1_line), Create(g2_line),
            Write(good_title), FadeIn(good_desc),
            Write(g1_formula), Write(g2_formula),
            run_time=TIME_NORMAL
        )
        # seg 4: "Split đúng theo cơ chế ẩn lộ ra hai nhóm..."
        play_voiceover_and_wait(self, 30, 4)

        # 5. Optimization Objective
        # Place objective formula on the right side
        obj_title = Text("Maximize Information Gain", font_size=22, color=THEME_EMERALD, font="Segoe UI", weight=BOLD).move_to(RIGHT * 3.8 + UP * 1.5)
        objective = MathTex(
            r"\sup_E \left[ I_v(Y; X \mid E) - I_v(Y; X) \right]",
            font_size=SIZE_FORMULA - 4,
            color=THEME_EMERALD
        ).next_to(obj_title, DOWN, buff=0.35)
        fit_to_width(objective, max_width=4.4)
        obj_desc = Text("Tìm nhóm E thay đổi mối\nquan hệ nhiều nhất.", font_size=18, color=TEXT_PRIMARY, font="Segoe UI", weight=MEDIUM).next_to(objective, DOWN, buff=0.35)

        self.play(
            FadeOut(good_title), FadeOut(good_desc),
            FadeOut(g1_formula), FadeOut(g2_formula),
            Write(obj_title), Write(objective), FadeIn(obj_desc),
            run_time=TIME_NORMAL
        )
        # seg 5: "Mục tiêu: tìm E maximize phần tăng thông tin... supremum..."
        play_voiceover_and_wait(self, 30, 5)

        # Takeaway
        insight = create_insight_box(
            "Các nhóm hữu ích sẽ làm thay đổi mối quan hệ dự đoán.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.7)

        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 6: "Các nhóm hữu ích sẽ làm thay đổi mối quan hệ dự đoán..."
        play_voiceover_and_wait(self, 30, 6)

        # Outro
        self.play(
            FadeOut(insight), FadeOut(obj_title), FadeOut(objective), FadeOut(obj_desc),
            FadeOut(axes), FadeOut(g1_dots), FadeOut(g2_dots), FadeOut(g1_line), FadeOut(g2_line),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
