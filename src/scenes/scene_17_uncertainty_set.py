"""Scene 17: Uncertainty Set.
Author: TV2  |  Duration: ~75 giây
Câu hỏi: Worst-case được chọn trong vùng nào?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait

TARGET_DURATION_SECONDS = 75


class UncertaintySetScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Uncertainty set",
                           "Vùng shift được phép cho worst-case")

        # ── Setup: Distribution space ─────────────────────────────────────
        axes = Axes(
            x_range=[-1, 5, 1], y_range=[-1, 4, 1],
            x_length=6.0, y_length=4.5, tips=False,
            axis_config={"color": GRID_COLOR, "stroke_width": 1.2},
        ).shift(LEFT * 0.5 + DOWN * 0.1)

        np.random.seed(99)
        bg_dots = VGroup(*[
            Dot(axes.c2p(np.random.uniform(0, 4), np.random.uniform(0, 3)),
                radius=0.04, color=TEXT_MUTED, fill_opacity=0.20)
            for _ in range(30)
        ])
        space_label = Text("Không gian phân phối", font_size=SIZE_CAPTION,
                           color=TEXT_MUTED, font=FONT_PRIMARY).next_to(axes, UP, buff=0.2)

        self.play(
            Create(axes, lag_ratio=0.05),
            LaggedStart(*[FadeIn(d, scale=0.3) for d in bg_dots], lag_ratio=0.03),
            FadeIn(space_label),
            run_time=1.5,
        )
        play_voiceover_and_wait(self, 17, 0)
        self.wait(5.5)

        # ── STAGE 2: P_train với ripple ───────────────────────────────────
        p_pos = axes.c2p(2.0, 1.8)
        p_dot = Dot(p_pos, radius=0.12, color=THEME_BLUE)
        p_glow = create_3b1b_glow(p_dot, color=THEME_BLUE, n_layers=5, opacity=0.25)
        p_label = MathTex(r"P_{\mathrm{train}}", font_size=SIZE_BODY, color=THEME_BLUE
                          ).next_to(p_dot, DOWN, buff=0.22)

        self.play(GrowFromCenter(p_glow), FadeIn(p_dot, scale=0.3), Write(p_label), run_time=1.0)
        # Một ripple ring duy nhất — sạch và đẹp
        ring = Circle(radius=0.12, color=THEME_BLUE, stroke_width=2.5, stroke_opacity=0.8
                      ).move_to(p_pos)
        self.add(ring)
        self.play(ring.animate.scale(9).set_stroke(opacity=0), run_time=1.2, rate_func=rush_from)
        self.remove(ring)
        self.wait(5.0)

        # ── STAGE 3: Uncertainty ball với ρ tracker ───────────────────────
        rho_tracker = ValueTracker(1.2)
        r_scale = axes.x_length / (axes.x_range[1] - axes.x_range[0])

        ball = always_redraw(lambda: Circle(
            radius=rho_tracker.get_value() * r_scale,
            color=THEME_AMBER, stroke_width=2.8,
            fill_color=THEME_AMBER, fill_opacity=0.07,
        ).move_to(p_pos))

        rho_lbl = MathTex(r"\rho", font_size=SIZE_SECTION, color=THEME_AMBER
                          ).to_edge(RIGHT, buff=1.8).shift(UP * 0.8)
        rho_eq  = MathTex(r"=", font_size=SIZE_BODY, color=TEXT_SECONDARY
                          ).next_to(rho_lbl, RIGHT, buff=0.1)
        rho_val = DecimalNumber(rho_tracker.get_value(), num_decimal_places=1,
                                font_size=SIZE_BODY, color=THEME_AMBER
                                ).next_to(rho_eq, RIGHT, buff=0.12)
        rho_val.add_updater(lambda m: m.set_value(rho_tracker.get_value()))
        rho_cap = Text("ρ là bán kính\ncủa vùng worst-case",
                       font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY, line_spacing=0.9
                       ).next_to(rho_lbl, DOWN, buff=0.35)
        u_label = always_redraw(lambda: MathTex(
            r"\mathcal{U}(P_{\mathrm{train}},\, \rho)",
            font_size=SIZE_CAPTION, color=THEME_AMBER,
        ).next_to(ball, UP, buff=0.18))

        self.play(Create(ball), Write(rho_lbl), Write(rho_eq),
                  Write(rho_val), FadeIn(rho_cap), run_time=1.2)
        self.play(FadeIn(u_label), run_time=0.7)
        self.wait(5.0)

        # Animate ρ tăng / giảm / về normal
        self.play(rho_tracker.animate.set_value(2.0), run_time=1.8, rate_func=smooth)
        self.wait(2.7)
        self.play(ShowPassingFlash(ball.copy().set_stroke(THEME_AMBER_LIGHT, width=6), time_width=0.45), run_time=0.8)
        self.play(rho_tracker.animate.set_value(0.55), run_time=1.8, rate_func=smooth)
        self.wait(2.7)
        self.play(ShowPassingFlash(ball.copy().set_stroke(THEME_RED_LIGHT, width=6), time_width=0.45), run_time=0.8)
        self.play(rho_tracker.animate.set_value(1.2), run_time=1.2, rate_func=smooth)
        self.wait(3.0)

        # ── STAGE 4: Q* xuất hiện bên trong ball ─────────────────────────
        q_star_pos = axes.c2p(2.8, 2.6)
        q_star = Dot(q_star_pos, radius=0.10, color=THEME_RED)
        q_star_glow = create_3b1b_glow(q_star, color=THEME_RED, n_layers=3, opacity=0.22)
        q_star_label = MathTex(r"Q^*", font_size=SIZE_BODY, color=THEME_RED
                               ).next_to(q_star_pos, UP, buff=0.15)
        q_annot = Text("worst-case trong U",
                       font_size=SIZE_SMALL, color=THEME_RED, font=FONT_PRIMARY
                       ).next_to(q_star_label, RIGHT, buff=0.15)

        self.play(FadeIn(q_star_glow), FadeIn(q_star, scale=0.3),
                  Write(q_star_label), FadeIn(q_annot), run_time=1.0)
        self.play(Flash(q_star, color=THEME_RED, flash_radius=0.45, line_length=0.15), run_time=0.5)
        play_voiceover_and_wait(self, 17, 1)
        self.wait(6.0)

        # ── STAGE 5: Cảnh báo ρ nhỏ / lớn ───────────────────────────────
        warn_small = Text(
            "ρ quá nhỏ → shift thật ở ngoài → DRO hụt",
            font_size=SIZE_SMALL, color=THEME_RED, font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=1.1)
        warn_large = Text(
            "ρ quá lớn → worst-case xa thực tế → model quá bi quan",
            font_size=SIZE_SMALL, color=THEME_AMBER, font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=1.1)
        q_real_hint = Dot(axes.c2p(3.55, 0.65), radius=0.08, color=THEME_EMERALD)
        q_real_hint_label = MathTex(r"Q_{\mathrm{real}}", font_size=SIZE_SMALL, color=THEME_EMERALD
                                    ).next_to(q_real_hint, DOWN, buff=0.12)
        outside_arrow = Arrow(
            p_pos + RIGHT * 0.55 * r_scale,
            q_real_hint.get_left(),
            color=THEME_EMERALD,
            stroke_width=2.2,
            buff=0.1,
            tip_length=0.16,
        )

        self.play(rho_tracker.animate.set_value(0.4), Write(warn_small), run_time=1.5, rate_func=smooth)
        self.play(FadeIn(q_real_hint, scale=0.35), Write(q_real_hint_label), GrowArrow(outside_arrow), run_time=0.8, rate_func=smooth)
        self.wait(4.2)
        self.play(
            rho_tracker.animate.set_value(2.45),
            Transform(warn_small, warn_large),
            FadeOut(q_real_hint),
            FadeOut(q_real_hint_label),
            FadeOut(outside_arrow),
            run_time=1.5,
            rate_func=smooth,
        )
        self.wait(5.0)
        self.play(rho_tracker.animate.set_value(1.2), FadeOut(warn_small), run_time=1.0)
        self.wait(4.0)

        # ── STAGE 6: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "Uncertainty set là giả định cốt lõi của DRO.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(3.1)
        self.play(Circumscribe(insight, color=THEME_AMBER, time_width=0.5), run_time=0.8)
        play_voiceover_and_wait(self, 17, 2)
        self.wait(4.6)
        fade_out_all(self)
