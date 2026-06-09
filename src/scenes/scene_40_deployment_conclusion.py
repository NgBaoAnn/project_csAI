"""
Scene 40: Deployment Conclusion
Author: TV4 (Animation Lead)
Duration: ~100 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class DeploymentConclusionScene(Scene):
    def make_recap_card(self, title_text, desc_text, color, position):
        box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.08, stroke_color=color, stroke_width=2, fill_color=BG_PANEL, fill_opacity=0.6)
        title = Text(title_text, font_size=SIZE_SMALL - 2, color=color, font=FONT_PRIMARY, weight=BOLD).move_to(box.get_top() + DOWN * 0.42)
        desc = Text(desc_text, font_size=SIZE_SMALL - 8, color=TEXT_SECONDARY, font=FONT_PRIMARY, line_spacing=0.8).move_to(box.get_center() + DOWN * 0.3)
        return VGroup(box, title, desc).move_to(position)

    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Network graph convergence to central glow dot
        np.random.seed(40)
        nodes = VGroup(*[
            Dot(point=[np.random.uniform(-2.5, 2.5), np.random.uniform(-1.8, 1.8), 0], color=THEME_EMERALD, radius=0.08)
            for _ in range(8)
        ])
        
        edges = VGroup()
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                if np.random.rand() > 0.65:
                    edges.add(Line(nodes[i].get_center(), nodes[j].get_center(), color=TEXT_MUTED, stroke_opacity=0.35, stroke_width=1.5))
                    
        self.play(FadeIn(nodes), Create(edges), run_time=TIME_NORMAL)
        self.wait(0.5)
        
        self.play(
            nodes.animate.move_to(ORIGIN),
            edges.animate.scale(0.01).move_to(ORIGIN),
            run_time=TIME_NORMAL,
            rate_func=smooth
        )
        
        center_glow_dot = Dot(ORIGIN, color=THEME_EMERALD, radius=0.15)
        center_glow = create_3b1b_glow(center_glow_dot, color=THEME_EMERALD, n_layers=5, opacity=0.35)
        
        self.remove(nodes, edges)
        self.play(FadeIn(center_glow_dot), FadeIn(center_glow), run_time=TIME_FAST)
        self.wait(0.2)
        
        title_text = Text("OOD Generalization", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_EMERALD, THEME_BLUE_LIGHT)
        title_glow = create_3b1b_glow(title_text, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        
        subtitle_text = Text("Quy trình OOD Generalization", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)
        
        self.play(
            ReplacementTransform(VGroup(center_glow_dot, center_glow), title_group),
            FadeIn(subtitle_text, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(4.5)
        
        self.play(
            FadeOut(title_group),
            FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        
        # Subtitle 1
        sub1 = create_bottom_caption("Sau deployment, ta phân tách sụt giảm do sampling shift và mechanism shift.")
        self.play(FadeIn(sub1))
        self.wait(8.0)
        
        # Draw Shared Distribution transition: P -> S -> Q
        p_circle = Circle(radius=0.7, color=THEME_BLUE, stroke_width=2.5, fill_color=THEME_BLUE, fill_opacity=0.15).shift(LEFT * 3.5 + UP * 0.8)
        p_label = Text("P (Nguồn / Source)", font_size=SIZE_SMALL - 6, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).next_to(p_circle, UP, buff=0.18)
        
        q_circle = Circle(radius=0.7, color=THEME_AMBER, stroke_width=2.5, fill_color=THEME_AMBER, fill_opacity=0.15).shift(RIGHT * 3.5 + UP * 0.8)
        q_label = Text("Q (Đích / Target)", font_size=SIZE_SMALL - 6, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).next_to(q_circle, UP, buff=0.18)
        
        # S (Intersection/Overlap)
        s_circle = Circle(radius=0.7, color=THEME_PURPLE, stroke_width=3, fill_color=THEME_PURPLE, fill_opacity=0.35).shift(UP * 0.8)
        s_label = Text("S (Phần chồng lấn chung)", font_size=SIZE_SMALL - 6, color=THEME_PURPLE, font=FONT_PRIMARY, weight=BOLD).next_to(s_circle, UP, buff=0.18)
        
        arrow_ps = Arrow(p_circle.get_right(), s_circle.get_left(), color=THEME_PURPLE, stroke_width=3)
        arrow_sq = Arrow(s_circle.get_right(), q_circle.get_left(), color=THEME_PURPLE, stroke_width=3)
        
        self.play(
            FadeIn(p_circle), FadeIn(p_label),
            FadeIn(q_circle), FadeIn(q_label),
            run_time=TIME_NORMAL
        )
        self.wait(6.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Bằng cách tập trung vào shared distribution S, ta phân tích nguyên nhân dịch chuyển.")
        self.play(Transform(sub1, sub2))
        self.play(
            FadeIn(s_circle), FadeIn(s_label),
            Create(arrow_ps), Create(arrow_sq),
            run_time=TIME_NORMAL
        )
        self.wait(11.0)
        
        # Clear shift transition elements
        self.play(
            FadeOut(p_circle), FadeOut(p_label), FadeOut(q_circle), FadeOut(q_label),
            FadeOut(s_circle), FadeOut(s_label), FadeOut(arrow_ps), FadeOut(arrow_sq),
            run_time=TIME_FAST
        )
        
        # Subtitle 3
        sub3 = create_bottom_caption("OOD generalization không phải là thuật toán đơn lẻ; đó là cả một workflow.")
        self.play(Transform(sub1, sub3))
        
        # Draw 2x2 Recap Cards representing the course
        card_erm = self.make_recap_card("ERM", "Tối thiểu hóa\nrủi ro trung bình", TEXT_MUTED, LEFT * 2.2 + UP * 1.5)
        card_dro = self.make_recap_card("DRO", "Tối ưu hóa\ntrường hợp xấu nhất", THEME_AMBER, RIGHT * 2.2 + UP * 1.5)
        card_irm = self.make_recap_card("IRM", "Biểu diễn bất biến\n(Invariant Representation)", THEME_ORANGE, LEFT * 2.2 + DOWN * 0.4)
        card_hrm = self.make_recap_card("HRM", "Tối thiểu hóa rủi ro\nkhông đồng nhất", THEME_EMERALD, RIGHT * 2.2 + DOWN * 0.4)
        
        self.play(
            FadeIn(card_erm, scale=0.95), FadeIn(card_dro, scale=0.95),
            FadeIn(card_irm, scale=0.95), FadeIn(card_hrm, scale=0.95),
            run_time=TIME_SLOW
        )
        self.wait(11.0)
        
        # Subtitle 4
        sub4 = create_bottom_caption("Hãy luôn thấu hiểu sự không đồng nhất của dữ liệu trước khi đối phó với shift.")
        self.play(Transform(sub1, sub4))
        
        # Highlight HRM Card (Co-evolution)
        hrm_glow = create_3b1b_glow(card_hrm[0], color=THEME_EMERALD, n_layers=4, opacity=0.18)
        self.play(
            FadeIn(hrm_glow),
            card_hrm[0].animate.set_stroke(color=THEME_EMERALD, width=3.5),
            run_time=TIME_NORMAL
        )
        self.wait(11.5)
        
        # Final Title: OOD Generalization Workflow
        self.play(
            FadeOut(card_erm), FadeOut(card_dro), FadeOut(card_irm), FadeOut(card_hrm), FadeOut(hrm_glow),
            run_time=TIME_FAST
        )
        
        final_title = Text("Quy trình OOD Generalization", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(UP * 0.5)
        final_subtitle = Text("Học máy lấy dữ liệu làm trung tâm & Nhận biết sự không đồng nhất", font_size=SIZE_BODY - 6, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(final_title, DOWN, buff=0.3)
        final_glow = create_3b1b_glow(final_title, color=THEME_EMERALD, n_layers=5, opacity=0.25)
        
        self.play(
            Write(final_title), FadeIn(final_subtitle), FadeIn(final_glow),
            run_time=TIME_NORMAL
        )
        self.wait(10.3)
        
        # Takeaway
        insight = create_insight_box(
            "Thấu hiểu sự không đồng nhất trước khi đối phó với dịch chuyển.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(14.5)
        
        # Outro
        self.play(
            FadeOut(final_title), FadeOut(final_subtitle), FadeOut(final_glow), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(5.5)
