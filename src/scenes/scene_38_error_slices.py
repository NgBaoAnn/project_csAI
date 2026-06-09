"""
Scene 38: Error Slices
Author: TV4 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class ErrorSlicesScene(Scene):
    def make_slice_bar(self, label_text, acc_text, ratio_text, color, position):
        box = RoundedRectangle(width=7.2, height=0.76, corner_radius=0.06, stroke_color=color, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6)
        label = Text(label_text, font_size=SIZE_SMALL - 2, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=SEMIBOLD)
        label.next_to(box.get_left(), RIGHT, buff=0.4)
        ratio = Text(f"({ratio_text} dữ liệu)", font_size=SIZE_SMALL - 6, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        ratio.next_to(label, RIGHT, buff=0.15)
        acc = Text(acc_text, font_size=SIZE_SMALL - 2, color=color, font=FONT_PRIMARY, weight=BOLD)
        acc.next_to(box.get_right(), LEFT, buff=0.4)
        
        slice_group = VGroup(box, label, ratio, acc).move_to(position)
        return slice_group

    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Custom horizontal box slicing/sliding animation (Shifted DOWN * 0.8 to avoid text overlaps)
        big_box = RoundedRectangle(width=3.6, height=1.8, corner_radius=0.08, stroke_color=THEME_BLUE, stroke_width=3, fill_color=BG_PANEL, fill_opacity=0.6).shift(DOWN * 0.8)
        self.play(FadeIn(big_box), run_time=TIME_FAST)
        self.wait(0.3)
        
        slice_left = RoundedRectangle(width=1.2, height=1.8, corner_radius=0.04, stroke_color=THEME_BLUE, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6).shift(DOWN * 0.8 + LEFT * 1.2)
        slice_mid = RoundedRectangle(width=1.2, height=1.8, corner_radius=0.04, stroke_color=THEME_BLUE, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6).shift(DOWN * 0.8)
        slice_right = RoundedRectangle(width=1.2, height=1.8, corner_radius=0.04, stroke_color=THEME_BLUE, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6).shift(DOWN * 0.8 + RIGHT * 1.2)
        
        self.remove(big_box)
        self.add(slice_left, slice_mid, slice_right)
        
        title_text = Text("Error Slices", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_BLUE, THEME_RED)
        title_glow = create_3b1b_glow(title_text, color=THEME_BLUE, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 1.2)
        
        subtitle_text = Text("Tìm ra vùng dữ liệu mô hình yếu nhất", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)
        
        self.play(
            slice_left.animate.shift(LEFT * 1.6),
            slice_right.animate.shift(RIGHT * 1.6),
            FadeIn(title_group, scale=0.9),
            Write(subtitle_text),
            run_time=TIME_NORMAL
        )
        self.wait(4.0)
        
        self.play(
            FadeOut(slice_left),
            FadeOut(slice_mid),
            FadeOut(slice_right),
            FadeOut(title_group),
            FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        
        # Subtitle 1
        sub1 = create_bottom_caption("Độ chính xác trung bình 95% có thể che giấu những lỗi cực kỳ nghiêm trọng.")
        self.play(FadeIn(sub1))
        self.wait(8.0)
        
        # Draw Overall Accuracy Box (Center)
        overall_box = RoundedRectangle(width=5.0, height=2.0, corner_radius=0.12, stroke_color=THEME_BLUE, stroke_width=3, fill_color=BG_PANEL, fill_opacity=0.6).shift(UP * 0.5)
        overall_title = Text("Độ chính xác mô hình tổng thể", font_size=SIZE_SMALL - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).move_to(overall_box.get_top() + DOWN * 0.45)
        overall_val = Text("Độ chính xác 95%", font_size=38, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(overall_box.get_center() + DOWN * 0.25)
        overall_glow = create_3b1b_glow(overall_val, color=THEME_BLUE, n_layers=4, opacity=0.18)
        overall_panel = VGroup(overall_box, overall_title, overall_glow, overall_val)
        
        self.play(FadeIn(overall_panel, scale=0.95), run_time=TIME_NORMAL)
        self.wait(9.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Chúng ta cần phân tách hiệu suất của model thành các lát cắt lỗi (error slices).")
        self.play(Transform(sub1, sub2))
        
        # Fade out overall and fade in 3 slices stacked vertically (Shifted LEFT * 1.2 to prevent text overflow on the right)
        s1 = self.make_slice_bar("Nhóm dân số A", "Độ chính xác 99%", "80%", THEME_EMERALD, UP * 1.3 + LEFT * 1.2)
        s2 = self.make_slice_bar("Nhóm dân số B", "Độ chính xác 93%", "15%", THEME_EMERALD, UP * 0.4 + LEFT * 1.2)
        s3 = self.make_slice_bar("Nhóm dân số C", "Độ chính xác 43%", "Thiểu số, 5%", THEME_RED, DOWN * 0.5 + LEFT * 1.2)
        
        self.play(
            ReplacementTransform(overall_panel, VGroup(s1, s2, s3)),
            run_time=TIME_SLOW
        )
        self.wait(8.5)
        
        # Subtitle 3
        sub3 = create_bottom_caption("Phát hiện lát cắt tệ nhất giúp chúng ta biết model thực sự hỏng ở đâu.")
        self.play(Transform(sub1, sub3))
        
        # Highlight Slice 3 with Red Glow
        glow_s3 = create_3b1b_glow(s3[0], color=THEME_RED, n_layers=4, opacity=0.2)
        warning_arrow = Arrow(s3.get_right() + RIGHT * 1.5, s3.get_right() + RIGHT * 0.2, color=THEME_RED, stroke_width=4)
        warning_text = Text("Lát cắt tệ nhất\n(Lỗi nghiêm trọng)", font_size=SIZE_SMALL - 4, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).next_to(warning_arrow, RIGHT, buff=0.15).shift(UP * 0.2)
        
        self.play(
            FadeIn(glow_s3), Create(warning_arrow), Write(warning_text),
            s3.animate.scale(1.05),
            run_time=TIME_NORMAL
        )
        self.wait(12.0)
        
        # Takeaway
        insight = create_insight_box(
            "Tìm vị trí model thất bại, không chỉ tần suất thất bại.",
            color=THEME_RED,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(16.5)
        
        # Outro
        self.play(
            FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(glow_s3),
            FadeOut(warning_arrow), FadeOut(warning_text), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
