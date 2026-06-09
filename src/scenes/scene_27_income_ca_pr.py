"""
Scene 27: Income CA -> PR
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


class IncomeCaPrScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: CA -> PR Map Sweep
        dot_ca = Dot(point=[LEFT * 4.5 + DOWN * 0.5], color=THEME_BLUE, radius=0.15)
        lbl_ca = Text("CA", font_size=SIZE_BODY, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).next_to(dot_ca, UP, buff=0.15)

        dot_pr = Dot(point=[RIGHT * 4.5 + DOWN * 0.5], color=THEME_AMBER, radius=0.15)
        lbl_pr = Text("PR", font_size=SIZE_BODY, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).next_to(dot_pr, UP, buff=0.15)

        sweep_arrow = Arrow(dot_ca.get_right(), dot_pr.get_left(), color=THEME_PURPLE, stroke_width=4, buff=0.15)

        title_text = Text("Income Prediction: CA -> PR", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(UP * 2.2)
        subtitle_text = Text("Phân tích nguyên nhân sụt giảm", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(title_text, DOWN, buff=0.25)

        # Animate
        self.play(FadeIn(dot_ca, scale=0.5), FadeIn(lbl_ca), run_time=0.8)
        self.play(GrowArrow(sweep_arrow), Write(title_text), FadeIn(subtitle_text, shift=UP * 0.1), run_time=1.5)
        self.play(FadeIn(dot_pr, scale=0.5), FadeIn(lbl_pr), run_time=0.8)

        # seg 0: Title introduction
        play_voiceover_and_wait(self, 27, 0)

        # Clean up
        self.play(
            FadeOut(dot_ca), FadeOut(lbl_ca),
            FadeOut(sweep_arrow), FadeOut(dot_pr), FadeOut(lbl_pr),
            FadeOut(title_text), FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        self.wait(0.5)

        # Subtitle 1
        sub1 = create_bottom_caption("Trong income prediction, source là California và target là Puerto Rico.")
        self.play(FadeIn(sub1))
        # seg 1: "Trong income prediction... drop đến từ đâu?"
        play_voiceover_and_wait(self, 27, 1)

        # 2. Draw CA and PR comparison cards
        card_w, card_h = 4.2, 2.85
        spacing = 3.15

        ca_box = RoundedRectangle(width=card_w, height=card_h, corner_radius=0.1, stroke_color=THEME_BLUE, stroke_width=2.5)
        ca_title = Text("Source: California (CA)", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(ca_box.get_top() + DOWN * 0.4)
        fit_to_width(ca_title, max_width=ca_box.get_width() * 0.88)
        ca_desc = VGroup(
            Text("Thu nhập TB: $80k", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("Ngành công nghệ: Cao", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("Giờ làm việc: ~40h/tuần", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(ca_box.get_center() + DOWN * 0.3)
        ca_card = VGroup(ca_box, ca_title, ca_desc).shift(LEFT * spacing + UP * 0.82)

        pr_box = RoundedRectangle(width=card_w, height=card_h, corner_radius=0.1, stroke_color=THEME_AMBER, stroke_width=2.5)
        pr_title = Text("Target: Puerto Rico (PR)", font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).move_to(pr_box.get_top() + DOWN * 0.4)
        fit_to_width(pr_title, max_width=pr_box.get_width() * 0.88)
        pr_desc = VGroup(
            Text("Thu nhập TB: $22k", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("Ngành công nghệ: Thấp", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY),
            Text("Giờ làm việc: ~32h/tuần", font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15).move_to(pr_box.get_center() + DOWN * 0.3)
        pr_card = VGroup(pr_box, pr_title, pr_desc).shift(RIGHT * spacing + UP * 0.82)
        shift_arrow = Arrow(ca_box.get_right() + RIGHT * 0.18, pr_box.get_left() + LEFT * 0.18, color=TEXT_MUTED, stroke_width=2.5, buff=0.1)

        self.play(FadeIn(ca_card, shift=RIGHT * 0.2), FadeIn(pr_card, shift=LEFT * 0.2), Create(shift_arrow), run_time=TIME_NORMAL)
        # seg 2: "California 80k... Puerto Rico 22k..."
        play_voiceover_and_wait(self, 27, 2)

        # Subtitle 2
        sub2 = create_bottom_caption("Drop có thể đến từ X-shift: phân phối work hours hay occupation thay đổi.")
        self.play(Transform(sub1, sub2))
        # seg 3: "Drop có thể đến từ X-shift..."
        play_voiceover_and_wait(self, 27, 3)

        # Show X-shift by drawing simple histograms representing feature distributions
        ca_hist = VGroup(*[
            Rectangle(width=0.3, height=h, color=THEME_BLUE, fill_color=THEME_BLUE, fill_opacity=0.6, stroke_width=1)
            for h in (0.3, 0.7, 1.6, 2.0, 1.2, 0.4)
        ]).arrange(RIGHT, aligned_edge=DOWN, buff=0.08).move_to(ca_box.get_center() + DOWN * 0.3)

        pr_hist = VGroup(*[
            Rectangle(width=0.3, height=h, color=THEME_AMBER, fill_color=THEME_AMBER, fill_opacity=0.6, stroke_width=1)
            for h in (1.5, 1.8, 1.0, 0.5, 0.2, 0.1)
        ]).arrange(RIGHT, aligned_edge=DOWN, buff=0.08).move_to(pr_box.get_center() + DOWN * 0.3)

        # Fade out descriptions, fade in histograms to show X-shift
        self.play(
            FadeOut(ca_desc), FadeIn(ca_hist),
            FadeOut(pr_desc), FadeIn(pr_hist),
            run_time=TIME_NORMAL
        )

        x_shift_label = Text("X-shift (Covariate Shift)", font_size=SIZE_CAPTION, color=THEME_BLUE_LIGHT, font=FONT_PRIMARY).to_edge(UP, buff=0.78)
        self.play(Write(x_shift_label))
        # seg 4: "Histograms xanh và vàng cho thấy phân phối thay đổi..."
        play_voiceover_and_wait(self, 27, 4)

        # Subtitle 3
        sub3 = create_bottom_caption("Hoặc Y|X-shift: cùng occupation nhưng income mang ý nghĩa khác theo bối cảnh.")
        self.play(Transform(sub1, sub3))
        # seg 5: "Nhưng cũng có thể từ Y given X shift..."
        play_voiceover_and_wait(self, 27, 5)

        # Show Y|X-shift: Plot two regression lines showing Occupation vs Income
        axes_ca = Axes(x_range=[0, 4, 1], y_range=[0, 4, 1], x_length=2.0, y_length=1.5, axis_config={"color": TEXT_MUTED}).move_to(ca_box.get_center() + DOWN * 0.32)
        axes_pr = Axes(x_range=[0, 4, 1], y_range=[0, 4, 1], x_length=2.0, y_length=1.5, axis_config={"color": TEXT_MUTED}).move_to(pr_box.get_center() + DOWN * 0.32)

        ca_reg = axes_ca.plot(lambda x: 0.8 * x + 0.5, color=THEME_BLUE, stroke_width=3)
        pr_reg = axes_pr.plot(lambda x: 0.3 * x + 0.2, color=THEME_AMBER, stroke_width=3)

        ca_reg_label = MathTex(r"P_{\text{CA}}(Y \mid X)", font_size=20, color=THEME_BLUE).next_to(ca_reg, UP, buff=0.05).shift(LEFT * 0.3)
        pr_reg_label = MathTex(r"P_{\text{PR}}(Y \mid X)", font_size=20, color=THEME_AMBER).next_to(pr_reg, UP, buff=0.05).shift(LEFT * 0.3)

        self.play(
            FadeOut(ca_hist), FadeIn(axes_ca), Create(ca_reg), FadeIn(ca_reg_label),
            FadeOut(pr_hist), FadeIn(axes_pr), Create(pr_reg), FadeIn(pr_reg_label),
            FadeOut(x_shift_label),
            run_time=TIME_NORMAL
        )

        yx_shift_label = Text("Y|X-shift (Concept Shift)", font_size=SIZE_CAPTION, color=THEME_AMBER_LIGHT, font=FONT_PRIMARY).to_edge(UP, buff=0.75)
        self.play(Write(yx_shift_label))
        # seg 6: "Hai đường hồi quy khác slope..."
        play_voiceover_and_wait(self, 27, 6)

        # Takeaway
        insight = create_insight_box(
            "Sụt giảm mục tiêu có thể trộn lẫn X-shift và Y|X-shift.",
            color=THEME_PURPLE,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.7)

        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 7: "Target drop có thể trộn lẫn cả hai loại shift..."
        play_voiceover_and_wait(self, 27, 7)

        # Outro
        self.play(
            FadeOut(insight), FadeOut(ca_card[0]), FadeOut(ca_card[1]), FadeOut(pr_card[0]), FadeOut(pr_card[1]), FadeOut(shift_arrow),
            FadeOut(axes_ca), FadeOut(ca_reg), FadeOut(ca_reg_label),
            FadeOut(axes_pr), FadeOut(pr_reg), FadeOut(pr_reg_label),
            FadeOut(yx_shift_label),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
