"""
Scene 39: Stability + Feature Sensitivity
Author: TV4 (Animation Lead)
Duration: ~75 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


class StabilityFeatureScene(Scene):
    def make_slider(self, label_text, y_pos, active_color=THEME_BLUE):
        line = Line([2.0, y_pos, 0], [5.0, y_pos, 0], color=GRID_COLOR, stroke_width=3)
        dot = Dot([2.5, y_pos, 0], color=active_color, radius=0.08)
        label = Text(label_text, font_size=SIZE_SMALL - 6, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(line, UP, buff=0.12, aligned_edge=LEFT)
        return VGroup(line, dot, label)

    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: Concentric elastic circles and radar scan line sweep
        circle_inner = Circle(radius=0.8, color=THEME_BLUE, stroke_width=1.8, stroke_opacity=0.25)
        circle_outer = Circle(radius=1.5, color=THEME_BLUE_LIGHT, stroke_width=1.8, stroke_opacity=0.25)
        concentric = VGroup(circle_inner, circle_outer)

        self.play(FadeIn(concentric), run_time=TIME_FAST)
        self.play(concentric.animate.scale(1.2), run_time=0.9, rate_func=there_and_back)

        scan_line = Line(start=UP * 2 + LEFT * 3, end=DOWN * 2 + LEFT * 3, color=THEME_AMBER, stroke_width=3)
        self.play(FadeIn(scan_line), run_time=TIME_FAST)

        title_text = Text("Stability & Margin", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_BLUE_LIGHT, THEME_AMBER)
        title_glow = create_3b1b_glow(title_text, color=THEME_AMBER, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        subtitle_text = Text("Đo lường biên an toàn của mô hình", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)

        self.play(
            scan_line.animate.move_to(RIGHT * 3),
            FadeIn(title_group, shift=RIGHT * 0.2),
            Write(subtitle_text),
            run_time=TIME_NORMAL
        )
        self.play(FadeOut(scan_line), run_time=TIME_FAST)
        # seg 0: Title introduction
        play_voiceover_and_wait(self, 39, 0)
        self.play(FadeOut(concentric), FadeOut(title_group), FadeOut(subtitle_text), run_time=TIME_FAST)

        # Subtitle 1
        sub1 = create_bottom_caption("Để đánh giá stability, ta đo khoảng cách từ phân phối hiện tại đến vùng lỗi.")
        self.play(FadeIn(sub1))
        # seg 1: "đo khoảng cách từ phân phối tới vùng lỗi..."
        play_voiceover_and_wait(self, 39, 1)

        # Model Dot + Failure Set
        model_dot = Dot(LEFT * 4.8 + UP * 0.5, color=THEME_BLUE, radius=0.12)
        model_label = Text("Mô hình P_train", font_size=SIZE_SMALL - 6, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).next_to(model_dot, DOWN, buff=0.2)

        boundary = DashedLine(UP * 2.0 + LEFT * 2.0, DOWN * 1.5 + LEFT * 2.0, color=THEME_RED, stroke_width=3)
        failure_bg = Rectangle(width=3.5, height=3.5, stroke_width=0, fill_color=THEME_RED, fill_opacity=0.12).next_to(boundary, RIGHT, buff=0)
        failure_label = Text("Tập lỗi (Failure Set)\n(Độ chính xác sụt giảm)", font_size=SIZE_SMALL - 6, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).move_to(LEFT * 0.3 + UP * 1.4)

        self.play(
            FadeIn(model_dot), FadeIn(model_label),
            Create(boundary), FadeIn(failure_bg), FadeIn(failure_label),
            run_time=TIME_NORMAL
        )
        # seg 2: "đây là mô hình tại P_train, đây là tập lỗi..."
        play_voiceover_and_wait(self, 39, 2)

        # Stability Margin Arrow
        arrow = DoubleArrow(model_dot.get_center() + RIGHT * 0.15, LEFT * 2.0 + UP * 0.5, color=THEME_AMBER, stroke_width=3, buff=0.05)
        arrow_label = Text("Stability Margin\n(Biên độ ổn định)", font_size=SIZE_SMALL - 6, color=THEME_AMBER, font=FONT_PRIMARY).next_to(arrow, UP, buff=0.1).shift(LEFT * 0.5)

        self.play(Create(arrow), Write(arrow_label), run_time=TIME_NORMAL)
        # seg 3: "khoảng cách đó là stability margin..."
        play_voiceover_and_wait(self, 39, 3)

        # Subtitle 2 + sliders
        sub2 = create_bottom_caption("Ta cũng kiểm tra độ nhạy (sensitivity) của từng feature đối với sự thay đổi.")
        self.play(Transform(sub1, sub2))

        slider_age = self.make_slider("Feature 1: Dịch chuyển tuổi (Age Shift - Nhạy cảm)", 0.8, THEME_ORANGE)
        slider_edu = self.make_slider("Feature 2: Dịch chuyển trình độ (Education Shift - Ổn định)", -0.6, THEME_BLUE)

        self.play(FadeIn(slider_age), FadeIn(slider_edu), run_time=TIME_NORMAL)
        # seg 4: "kiểm tra độ nhạy từng feature: tuổi nhạy, học vấn ổn định..."
        play_voiceover_and_wait(self, 39, 4)

        # Subtitle 3 + sensitive shift
        sub3 = create_bottom_caption("Khi dịch chuyển một biến nhạy cảm, biên an toàn sẽ co hẹp thảm hại.")
        self.play(Transform(sub1, sub3))

        target_dot_pos = [4.5, 0.8, 0]
        target_model_pos = LEFT * 3.8 + UP * 0.5
        new_arrow = DoubleArrow(target_model_pos + RIGHT * 0.15, LEFT * 2.0 + UP * 0.5, color=THEME_RED, stroke_width=3, buff=0.05)

        self.play(
            slider_age[1].animate.move_to(target_dot_pos),
            model_dot.animate.move_to(target_model_pos),
            model_label.animate.next_to(target_model_pos, DOWN, buff=0.2),
            Transform(arrow, new_arrow),
            arrow_label.animate.set_color(THEME_RED).next_to(new_arrow, UP, buff=0.1).shift(LEFT * 0.7),
            run_time=TIME_SLOW
        )
        self.play(model_dot.animate.set_color(THEME_RED).scale(1.25), run_time=0.5)
        self.play(model_dot.animate.scale(1/1.25), run_time=0.5)
        # seg 5: "dịch biến nhạy cảm, biên an toàn co hẹp thảm hại..."
        play_voiceover_and_wait(self, 39, 5)

        # Subtitle 4
        sub4 = create_bottom_caption("Mô hình robust cần định nghĩa rõ: chống lại loại shift nào trên feature nào.")
        self.play(Transform(sub1, sub4))
        # seg 6: "mô hình robust phải nói rõ chống shift nào trên feature nào..."
        play_voiceover_and_wait(self, 39, 6)

        # Takeaway
        insight = create_insight_box(
            "Độ robust phải chỉ rõ loại dịch chuyển và các đặc trưng nhạy cảm.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)

        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 7: "độ robust phải chỉ rõ shift và feature nhạy cảm..."
        play_voiceover_and_wait(self, 39, 7)

        # Outro
        self.play(
            FadeOut(model_dot), FadeOut(model_label), FadeOut(boundary), FadeOut(failure_bg), FadeOut(failure_label),
            FadeOut(arrow), FadeOut(arrow_label), FadeOut(slider_age), FadeOut(slider_edu), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
