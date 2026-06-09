"""Scene 20: DRO Limits.
Author: TV2  |  Duration: ~70 giây
Câu hỏi: Worst-case có thật sự là target thật không?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 70


class DROLimitsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Giới hạn của DRO",
                           "worst-case có giống target thật không?")

        # ── Setup axes ────────────────────────────────────────────────────
        header = Text("Giả định DRO có thể sai",
                      font_size=SIZE_BODY, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=MEDIUM
                      ).to_edge(UP, buff=0.72)
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 4, 1],
            x_length=6.2, y_length=4.2, tips=False,
            axis_config={"color": GRID_COLOR, "stroke_width": 1.2},
        ).shift(LEFT * 0.5 + DOWN * 0.15)
        space_label = Text("Không gian phân phối", font_size=SIZE_SMALL,
                           color=TEXT_MUTED, font=FONT_PRIMARY).next_to(axes, UP, buff=0.18)

        np.random.seed(5)
        bg_dots = VGroup(*[
            Dot(axes.c2p(np.random.uniform(0, 4), np.random.uniform(0, 3)),
                radius=0.04, color=TEXT_MUTED, fill_opacity=0.20)
            for _ in range(25)
        ])

        self.play(
            Write(header), Create(axes), FadeIn(space_label),
            LaggedStart(*[FadeIn(d, scale=0.3) for d in bg_dots], lag_ratio=0.04),
            run_time=1.5,
        )
        self.wait(5.5)

        # ── STAGE 2: P_train với ripple ───────────────────────────────────
        p_pos = axes.c2p(1.5, 1.5)
        p_dot = Dot(p_pos, radius=0.11, color=THEME_BLUE)
        p_glow = create_3b1b_glow(p_dot, color=THEME_BLUE, n_layers=4, opacity=0.22)
        p_label = MathTex(r"P_{\mathrm{train}}", font_size=SIZE_CAPTION, color=THEME_BLUE
                          ).next_to(p_dot, LEFT, buff=0.2)

        self.play(GrowFromCenter(p_glow), FadeIn(p_dot, scale=0.3), Write(p_label), run_time=0.9)
        ring = Circle(radius=0.11, color=THEME_BLUE, stroke_width=2.5, stroke_opacity=0.8
                      ).move_to(p_pos)
        self.add(ring)
        self.play(ring.animate.scale(9).set_stroke(opacity=0), run_time=1.0, rate_func=rush_from)
        self.remove(ring)

        # ── STAGE 3: Uncertainty ball ─────────────────────────────────────
        r_screen = axes.x_length / (axes.x_range[1] - axes.x_range[0]) * 1.35
        ball = Circle(radius=r_screen, color=THEME_AMBER, stroke_width=2.5,
                      fill_color=THEME_AMBER, fill_opacity=0.07).move_to(p_pos)
        ball_label = MathTex(r"\mathcal{U}", font_size=SIZE_CAPTION, color=THEME_AMBER
                             ).next_to(ball, UP, buff=0.12)
        self.play(Create(ball), Write(ball_label), run_time=0.9)
        self.wait(5.5)

        # ── STAGE 4: Q* bên trong ball ────────────────────────────────────
        q_star_pos = axes.c2p(2.4, 2.5)
        q_star = Dot(q_star_pos, radius=0.10, color=THEME_RED)
        q_star_glow = create_3b1b_glow(q_star, color=THEME_RED, n_layers=3, opacity=0.22)
        q_star_label = MathTex(r"Q^*", font_size=SIZE_CAPTION, color=THEME_RED
                               ).next_to(q_star_pos, UP, buff=0.15)
        q_star_annot = Text("(worst-case mà DRO chọn)", font_size=SIZE_SMALL,
                            color=THEME_RED, font=FONT_PRIMARY).next_to(q_star_label, RIGHT, buff=0.14)

        self.play(
            FadeIn(q_star_glow), FadeIn(q_star, scale=0.3),
            Write(q_star_label), FadeIn(q_star_annot),
            run_time=1.0,
        )
        self.wait(5.5)

        # ── STAGE 5: Q_real bên ngoài ball ───────────────────────────────
        q_real_pos = axes.c2p(4.0, 0.4)
        q_real = Dot(q_real_pos, radius=0.10, color=THEME_EMERALD)
        q_real_glow = create_3b1b_glow(q_real, color=THEME_EMERALD, n_layers=3, opacity=0.22)
        q_real_label = MathTex(r"Q_{\mathrm{real}}", font_size=SIZE_CAPTION, color=THEME_EMERALD
                               ).next_to(q_real_pos, DOWN, buff=0.17)
        q_real_annot = Text("(shift thật: ngoài U)", font_size=SIZE_SMALL,
                            color=THEME_EMERALD, font=FONT_PRIMARY).next_to(q_real_label, LEFT, buff=0.14)

        self.play(
            FadeIn(q_real_glow), FadeIn(q_real, scale=0.3),
            Write(q_real_label), FadeIn(q_real_annot),
            run_time=1.0,
        )
        self.play(Indicate(q_real, color=THEME_EMERALD, scale_factor=1.5), run_time=0.7)
        self.wait(5.5)

        # ── STAGE 6: Mismatch arrow ───────────────────────────────────────
        mismatch_arrow = Arrow(q_star_pos, q_real_pos, color=THEME_RED, stroke_width=3.2,
                               buff=0.13, tip_length=0.22)
        mismatch_text = Text("LỆCH GIẢ ĐỊNH", font_size=SIZE_SMALL, color=THEME_RED,
                             font=FONT_PRIMARY, weight=BOLD
                             ).next_to(mismatch_arrow.get_center(), RIGHT, buff=0.22)
        mismatch_glow = create_3b1b_glow(mismatch_text, color=THEME_RED, n_layers=3, opacity=0.20)

        self.play(GrowArrow(mismatch_arrow), run_time=0.9)
        # Signature: ShowPassingFlash trên mismatch arrow
        self.play(
            ShowPassingFlash(mismatch_arrow.copy().set_stroke(THEME_RED_LIGHT, width=8), time_width=0.5),
            run_time=0.7,
        )
        self.play(FadeIn(mismatch_glow), Write(mismatch_text), run_time=0.9)
        self.wait(6.0)

        # ── STAGE 7: Hai failure modes ────────────────────────────────────
        prob1 = Text("① Lệch shift:\nQ* ≠ Q_real → tối ưu nhầm",
                     font_size=18, color=THEME_RED, font=FONT_PRIMARY, line_spacing=0.9)
        prob2 = Text("② Quá bi quan:\nU quá lớn → bài toán cực đoan",
                     font_size=18, color=THEME_AMBER, font=FONT_PRIMARY, line_spacing=0.9)
        problems = VGroup(prob1, prob2).arrange(DOWN, aligned_edge=LEFT, buff=0.28
                         ).to_edge(RIGHT, buff=0.35).shift(DOWN * 0.55)

        self.play(
            LaggedStart(
                FadeIn(prob1, shift=LEFT * 0.2),
                FadeIn(prob2, shift=LEFT * 0.2),
                lag_ratio=0.5,
            ),
            FadeOut(q_star_annot),
            FadeOut(q_real_annot),
            FadeOut(mismatch_glow),
            FadeOut(mismatch_text),
            run_time=1.2,
        )
        self.play(Circumscribe(prob1, color=THEME_RED, time_width=0.45), run_time=0.6)
        self.play(Circumscribe(prob2, color=THEME_AMBER, time_width=0.45), run_time=0.6)
        self.wait(6.3)

        # ── STAGE 8: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "DRO tốt cần giả định shift sát thực tế.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(20.0)
        fade_out_all(self)
