"""
Scene 26: Deductive vs Inductive
Author: TV3 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
class DeductiveInductiveScene(Scene):
    def make_node(self, text, color, pos):
        box = RoundedRectangle(width=3.35, height=0.65, corner_radius=0.05, stroke_color=color, fill_color=BG_DARKER, fill_opacity=0.9, stroke_width=1.8)
        label = create_text_block(text, font_size=SIZE_SMALL, color=color, max_chars=30, weight=MEDIUM)
        fit_to_width(label, max_width=2.95)
        node = VGroup(box, label).move_to(pos)
        return node

    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Two-column Slide
        lbl_deductive = Text("Deductive", font_size=SIZE_TITLE - 8, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).shift(LEFT * 6 + UP * 0.5)
        lbl_inductive = Text("Inductive", font_size=SIZE_TITLE - 8, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).shift(RIGHT * 6 + UP * 0.5)
        
        title_text = Text("Deductive vs Inductive", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(UP * 2.2)
        subtitle_text = Text("Ta nên bắt đầu từ đâu?", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(title_text, DOWN, buff=0.25)
        
        self.play(
            lbl_deductive.animate.move_to(LEFT * 2.2 + UP * 0.5),
            lbl_inductive.animate.move_to(RIGHT * 2.2 + UP * 0.5),
            Write(title_text),
            FadeIn(subtitle_text, shift=UP * 0.1),
            run_time=1.5
        )
        
        # Draw green dividing line
        mid_line = Line(UP * 1.0, DOWN * 0.5, color=THEME_EMERALD, stroke_width=4)
        glow_mid = create_3b1b_glow(mid_line, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        
        self.play(Create(mid_line), FadeIn(glow_mid), run_time=1.0)
        self.wait(1.5)
        
        # Clean up
        self.play(
            FadeOut(lbl_deductive),
            FadeOut(lbl_inductive),
            FadeOut(title_text),
            FadeOut(subtitle_text),
            FadeOut(mid_line),
            FadeOut(glow_mid),
            run_time=TIME_FAST
        )
        self.wait(1.0)
        
        # Subtitle 1
        sub1 = create_subtitle("Hướng tiếp cận diễn dịch đi từ các giả định lý thuyết rồi mới áp dụng thuật toán lên dữ liệu.")
        self.play(FadeIn(sub1))
        self.wait(5.0)
        
        # Vertical divider line
        divider = Line(UP * 2.45, DOWN * 2.0, color=GRID_COLOR, stroke_width=2)
        self.play(Create(divider))
        
        # Column headers
        header_left = Text("Deductive (Diễn dịch)", font_size=SIZE_BODY, color=TEXT_SECONDARY, font=FONT_PRIMARY, weight=BOLD).shift(LEFT * 3.5 + UP * 2.75)
        header_right = Text("Inductive (Quy nạp)", font_size=SIZE_BODY, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).shift(RIGHT * 3.5 + UP * 2.75)
        
        self.play(Write(header_left), Write(header_right))
        self.wait(5.0)
        
        # --- Deductive Flow (Left) ---
        d1 = self.make_node("1. Giả định lý thuyết", TEXT_SECONDARY, LEFT * 3.5 + UP * 1.8)
        d2 = self.make_node("2. Thiết kế thuật toán", TEXT_SECONDARY, LEFT * 3.5 + UP * 0.4)
        d3 = self.make_node("3. Áp dụng vào dữ liệu", TEXT_SECONDARY, LEFT * 3.5 + DOWN * 1.0)
        
        arrow_d1 = Arrow(d1.get_bottom(), d2.get_top(), color=TEXT_MUTED, stroke_width=3, buff=0.1)
        arrow_d2 = Arrow(d2.get_bottom(), d3.get_top(), color=TEXT_MUTED, stroke_width=3, buff=0.1)
        
        self.play(FadeIn(d1, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        self.play(Create(arrow_d1), FadeIn(d2, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        self.play(Create(arrow_d2), FadeIn(d3, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        self.wait(6.0)
        
        # Subtitle 2
        sub2 = create_subtitle("Ngược lại, hướng quy nạp bắt đầu từ dữ liệu thực tế, quan sát các mẫu lỗi và kiểu shift...")
        self.play(Transform(sub1, sub2))
        self.wait(5.0)
        
        # --- Inductive Flow (Right) ---
        i1 = self.make_node("1. Lỗi thực tế", THEME_AMBER, RIGHT * 3.5 + UP * 2.0)
        i2 = self.make_node("2. Phân tích kiểu shift", THEME_AMBER, RIGHT * 3.5 + UP * 0.8)
        i3 = self.make_node("3. Giả định tùy chỉnh", THEME_AMBER, RIGHT * 3.5 + DOWN * 0.4)
        i4 = self.make_node("4. Lựa chọn phương pháp", THEME_EMERALD, RIGHT * 3.5 + DOWN * 1.6)
        
        arrow_i1 = Arrow(i1.get_bottom(), i2.get_top(), color=THEME_AMBER, stroke_width=3, buff=0.1)
        arrow_i2 = Arrow(i2.get_bottom(), i3.get_top(), color=THEME_AMBER, stroke_width=3, buff=0.1)
        arrow_i3 = Arrow(i3.get_bottom(), i4.get_top(), color=THEME_EMERALD, stroke_width=3, buff=0.1)
        
        self.play(FadeIn(i1, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        self.play(Create(arrow_i1), FadeIn(i2, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        self.wait(5.5)
        
        # Subtitle 3
        sub3 = create_subtitle("...từ đó mới thiết kế giả định và phương pháp phù hợp nhất cho bài toán.")
        self.play(Transform(sub1, sub3))
        self.wait(5.0)
        
        self.play(Create(arrow_i2), FadeIn(i3, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        self.play(Create(arrow_i3), FadeIn(i4, shift=DOWN * 0.15), run_time=TIME_NORMAL)
        
        # Highlight Inductive Path with Glow
        i_glow = create_3b1b_glow(i4[0], color=THEME_EMERALD, n_layers=4)
        self.play(FadeIn(i_glow), i4[1].animate.set_color(THEME_EMERALD), run_time=TIME_NORMAL)
        self.wait(6.5)
        
        # Takeaway
        insight = create_insight_box(
            "Bắt đầu từ các dịch chuyển quan sát được.",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.7)
        
        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(9.0)
        
        # Outro
        self.play(
            FadeOut(insight), FadeOut(divider),
            FadeOut(header_left), FadeOut(header_right),
            FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(arrow_d1), FadeOut(arrow_d2),
            FadeOut(i1), FadeOut(i2), FadeOut(i3), FadeOut(i4), FadeOut(arrow_i1), FadeOut(arrow_i2), FadeOut(arrow_i3),
            FadeOut(i_glow),
            run_time=TIME_NORMAL
        )
        self.wait(2.5)
