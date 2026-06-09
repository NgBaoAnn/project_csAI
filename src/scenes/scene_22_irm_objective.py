"""
Scene 22: IRM Objective
Author: TV3 (Animation Lead)
Duration: ~80 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


class IRMObjectiveScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: 3B1B-Style Unified Boundary Merge
        # Left and Right axes representing two different environments
        ax_l = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=2.5, y_length=2.5, axis_config={"color": TEXT_MUTED, "stroke_width": 1.5}).shift(LEFT * 3.0 + DOWN * 0.8)
        ax_r = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=2.5, y_length=2.5, axis_config={"color": TEXT_MUTED, "stroke_width": 1.5}).shift(RIGHT * 3.0 + DOWN * 0.8)
        
        # Left boundary line w_1 (blue, tilted positive)
        w1_line = Line(ax_l.c2p(-1.2, -0.8, 0), ax_l.c2p(1.2, 0.8, 0), color=THEME_BLUE, stroke_width=3)
        w1_label = MathTex(r"w_1", font_size=SIZE_SMALL, color=THEME_BLUE).next_to(w1_line, UP, buff=0.1).shift(RIGHT * 0.5)
        
        # Right boundary line w_2 (amber, tilted negative)
        w2_line = Line(ax_r.c2p(-1.2, 0.8, 0), ax_r.c2p(1.2, -0.8, 0), color=THEME_AMBER, stroke_width=3)
        w2_label = MathTex(r"w_2", font_size=SIZE_SMALL, color=THEME_AMBER).next_to(w2_line, UP, buff=0.1).shift(RIGHT * 0.5)
        
        # Center target axis
        ax_c = Axes(x_range=[-1.5, 1.5], y_range=[-1.5, 1.5], x_length=3.0, y_length=3.0, axis_config={"color": TEXT_MUTED, "stroke_width": 2}).shift(DOWN * 0.8)
        
        # Merged boundary w (purple, horizontal)
        target_line = Line(ax_c.c2p(-1.4, 0, 0), ax_c.c2p(1.4, 0, 0), color=THEME_PURPLE, stroke_width=4.5)
        w_label = MathTex(r"w", font_size=SIZE_BODY, color=THEME_PURPLE).move_to(ax_c.c2p(0.25, 0.4, 0))
        
        title_text = Text("IRM Objective", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD)
        subtitle_text = Text("Cùng một classifier w cho mọi environment", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        intro_group = VGroup(title_text, subtitle_text).arrange(DOWN, buff=0.35).move_to(UP * 1.5)
        
        # Animate left and right setups entering
        self.play(
            Create(ax_l), Create(ax_r),
            run_time=0.8
        )
        self.play(
            Create(w1_line), FadeIn(w1_label),
            Create(w2_line), FadeIn(w2_label),
            run_time=0.8
        )
        self.wait(0.4)
        
        # Morph/merge them into the center axis and single purple boundary w
        glow_w = create_3b1b_glow(target_line, color=THEME_PURPLE, n_layers=4, opacity=0.15)
        self.play(
            ReplacementTransform(ax_l, ax_c),
            ReplacementTransform(ax_r, ax_c),
            Transform(w1_line, target_line),
            Transform(w2_line, target_line),
            Transform(w1_label, w_label),
            Transform(w2_label, w_label),
            FadeIn(glow_w),
            Write(title_text),
            FadeIn(subtitle_text, shift=UP * 0.1),
            run_time=1.8
        )
        
        # Audio seg 0 (Intro)
        play_voiceover_and_wait(self, 22, 0)
        
        # Clean up
        self.play(
            FadeOut(ax_c),
            FadeOut(w1_line), FadeOut(w2_line),
            FadeOut(w1_label), FadeOut(w2_label),
            FadeOut(glow_w),
            FadeOut(intro_group),
            run_time=TIME_FAST
        )
        self.wait(1.0)
        
        # Subtitle 1
        sub1 = create_bottom_caption("IRM học representation Phi(X) để cùng một classifier w dùng được ở mọi environment.")
        self.play(FadeIn(sub1))
        
        # Audio seg 1 & 2
        play_voiceover_and_wait(self, 22, 1)
        play_voiceover_and_wait(self, 22, 2)
        
        # 2. Draw Spaces
        # Left space: Raw Space X
        axes_left = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4.0,
            y_length=3.8,
            axis_config={"color": TEXT_MUTED, "stroke_width": 2}
        ).shift(LEFT * 3.15 + UP * 0.55)
        
        raw_title = Text("Raw Space X", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY).next_to(axes_left, UP, buff=0.25)
        
        # E1 points in raw space (e.g. separated by y = x)
        e1_class0 = VGroup(*[Dot(axes_left.c2p(x, y, 0), color=THEME_BLUE, radius=0.05) for x, y in [(-1.5, -0.5), (-2, -1.5), (-0.8, -1.8), (-1.2, -1.2)]])
        e1_class1 = VGroup(*[Dot(axes_left.c2p(x, y, 0), color=THEME_BLUE, radius=0.05) for x, y in [(1.5, 0.5), (2, 1.5), (0.8, 1.8), (1.2, 1.2)]])
        e1_points = VGroup(e1_class0, e1_class1)
        e1_boundary = Line(axes_left.c2p(-2.5, -2.5, 0), axes_left.c2p(2.5, 2.5, 0), color=THEME_BLUE, stroke_width=2, stroke_opacity=0.6)
        
        # E2 points in raw space (e.g. separated by y = -0.5x)
        e2_class0 = VGroup(*[Dot(axes_left.c2p(x, y, 0), color=THEME_AMBER, radius=0.05) for x, y in [(-2, 1.5), (-1.5, 2.0), (-1.0, 1.2), (-0.8, 1.6)]])
        e2_class1 = VGroup(*[Dot(axes_left.c2p(x, y, 0), color=THEME_AMBER, radius=0.05) for x, y in [(2, -1.5), (1.5, -2.0), (1.0, -1.2), (0.8, -1.6)]])
        e2_points = VGroup(e2_class0, e2_class1)
        e2_boundary = Line(axes_left.c2p(-2.5, 1.25, 0), axes_left.c2p(2.5, -1.25, 0), color=THEME_AMBER, stroke_width=2, stroke_opacity=0.6)
        
        self.play(FadeIn(axes_left), Write(raw_title))
        self.play(FadeIn(e1_points), Create(e1_boundary))
        self.play(FadeIn(e2_points), Create(e2_boundary))
        
        # Mismatch highlight: flash boundaries red to show discrepancy (+4.0s total)
        self.play(
            e1_boundary.animate.set_color(THEME_RED),
            e2_boundary.animate.set_color(THEME_RED),
            run_time=TIME_NORMAL
        )
        self.play(
            e1_boundary.animate.set_color(THEME_BLUE),
            e2_boundary.animate.set_color(THEME_AMBER),
            run_time=TIME_NORMAL
        )
        
        # Audio seg 3: Trong raw space X...
        play_voiceover_and_wait(self, 22, 3)
        
        # Mapping Arrow
        mapping_arrow = Arrow(LEFT * 0.65, RIGHT * 0.65, color=THEME_PURPLE, stroke_width=4).shift(UP * 0.55)
        mapping_label = MathTex(r"\Phi(X)", font_size=SIZE_BODY, color=THEME_PURPLE).next_to(mapping_arrow, UP, buff=0.1)
        
        self.play(GrowArrow(mapping_arrow), Write(mapping_label))
        
        # Right space: Rep space Phi(X)
        axes_right = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=4.0,
            y_length=3.8,
            axis_config={"color": TEXT_MUTED, "stroke_width": 2}
        ).shift(RIGHT * 3.15 + UP * 0.55)
        
        rep_title = Text("Representation Space", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY).next_to(axes_right, UP, buff=0.25)
        
        # In representation space, both environments align (e.g. separated by vertical line x=0)
        e1_rep_class0 = VGroup(*[Dot(axes_right.c2p(x, y, 0), color=THEME_BLUE, radius=0.05) for x, y in [(-1.5, 1.0), (-2.0, -0.5), (-1.2, -1.5), (-0.8, 0.2)]])
        e1_rep_class1 = VGroup(*[Dot(axes_right.c2p(x, y, 0), color=THEME_BLUE, radius=0.05) for x, y in [(1.5, 1.0), (2.0, -0.5), (1.2, -1.5), (0.8, 0.2)]])
        
        e2_rep_class0 = VGroup(*[Dot(axes_right.c2p(x, y, 0), color=THEME_AMBER, radius=0.05) for x, y in [(-1.8, 1.5), (-2.2, -1.0), (-1.0, -0.8), (-1.4, 0.8)]])
        e2_rep_class1 = VGroup(*[Dot(axes_right.c2p(x, y, 0), color=THEME_AMBER, radius=0.05) for x, y in [(1.8, 1.5), (2.2, -1.0), (1.0, -0.8), (1.4, 0.8)]])
        rep_points = VGroup(e1_rep_class0, e1_rep_class1, e2_rep_class0, e2_rep_class1)
        
        shared_boundary = Line(axes_right.c2p(0, -2.5, 0), axes_right.c2p(0, 2.5, 0), color=THEME_PURPLE, stroke_width=4)
        boundary_label = MathTex(r"w", font_size=SIZE_BODY, color=THEME_PURPLE).next_to(shared_boundary, UP, buff=0.1)
        
        self.play(FadeIn(axes_right), Write(rep_title))
        self.play(
            TransformFromCopy(e1_points, VGroup(e1_rep_class0, e1_rep_class1)),
            TransformFromCopy(e2_points, VGroup(e2_rep_class0, e2_rep_class1)),
            run_time=3.0
        )
        self.play(Create(shared_boundary), Write(boundary_label))
        
        # Audio seg 4: Qua ánh xạ Phi...
        play_voiceover_and_wait(self, 22, 4)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Nếu w phải dùng được ở mọi nơi, representation không nên giữ feature chỉ hữu ích cục bộ.")
        self.play(Transform(sub1, sub2))
        
        # Clear some items to display formula
        self.play(
            FadeOut(axes_left), FadeOut(raw_title), FadeOut(e1_points), FadeOut(e2_points), FadeOut(e1_boundary), FadeOut(e2_boundary),
            FadeOut(axes_right), FadeOut(rep_title), FadeOut(shared_boundary), FadeOut(boundary_label),
            FadeOut(rep_points),
            FadeOut(mapping_arrow), FadeOut(mapping_label),
            run_time=TIME_NORMAL
        )
        
        # 3. Formula Display
        # We group each formula term with its corresponding label to stack them vertically.
        # This aligns the blue formula directly above the blue label, and the yellow formula directly above the yellow label.
        term_erm = VGroup(
            MathTex(
                r"\min_{\Phi}\quad \sum_{e \in \mathcal{E}_{train}} R^e(\Phi)",
                font_size=SIZE_FORMULA,
                color=THEME_BLUE,
            ),
            create_label("Rủi ro huấn luyện trung bình (average training risk)", color=THEME_BLUE, font_size=SIZE_SMALL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        term_inv = VGroup(
            MathTex(
                r"+\lambda \sum_{e \in \mathcal{E}_{train}} \left\| \nabla_{w \mid w=1} R^e(w \circ \Phi) \right\|^2",
                font_size=SIZE_FORMULA,
                color=THEME_AMBER,
            ),
            create_label("Hình phạt classifier đồng nhất (same classifier penalty)", color=THEME_AMBER, font_size=SIZE_SMALL)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        
        formula_group = VGroup(term_erm, term_inv).arrange(DOWN, aligned_edge=LEFT, buff=0.48)
        fit_to_width(formula_group, max_width=10.6)
        formula_group.move_to(UP * 0.55)
        
        self.play(Write(term_erm[0]))
        self.play(FadeIn(term_erm[1], shift=UP * 0.1))
        
        # Audio seg 5: Hàm mục tiêu IRM gồm hai phần...
        play_voiceover_and_wait(self, 22, 5)
        
        self.play(Write(term_inv[0]))
        self.play(FadeIn(term_inv[1], shift=UP * 0.1))
        
        # Audio seg 6: Phần hai hình phạt...
        play_voiceover_and_wait(self, 22, 6)
        
        # Takeaway
        insight = create_insight_box(
            "IRM yêu cầu một classifier tối ưu duy nhất trên mọi environment.",
            color=THEME_PURPLE,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        
        # Audio seg 7: IRM yêu cầu một classifier...
        play_voiceover_and_wait(self, 22, 7)
        
        # Outro
        self.play(
            FadeOut(formula_group), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(0.5)
