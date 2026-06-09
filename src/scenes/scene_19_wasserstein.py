"""Scene 19: Wasserstein Distance.
Author: TV2  |  Duration: ~80 giây
Câu hỏi: Khi support thay đổi, ta đo khoảng cách phân phối như thế nào?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 80


class WassersteinScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Wasserstein",
                           "Shift có geometry: cần tính chi phí vận chuyển")

        # ── STAGE 1: So sánh f-div vs Wasserstein ─────────────────────────
        compare_title = Text("f-divergence vs Wasserstein",
                             font_size=SIZE_BODY, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=MEDIUM
                             ).to_edge(UP, buff=0.72)

        fd_box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.1,
                                  stroke_color=THEME_BLUE, fill_color=THEME_BLUE, fill_opacity=0.08,
                                  stroke_width=2.0).shift(LEFT * 3.2 + UP * 0.5)
        fd_text = Text('"Trọng số khác\nbao nhiêu?"',
                       font_size=SIZE_SMALL, color=THEME_BLUE, font=FONT_PRIMARY, line_spacing=1.1
                       ).move_to(fd_box)
        vs_text = Text("so với", font_size=SIZE_BODY, color=TEXT_MUTED, font=FONT_PRIMARY).shift(UP * 0.5)
        wass_box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.1,
                                    stroke_color=THEME_AMBER, fill_color=THEME_AMBER, fill_opacity=0.08,
                                    stroke_width=2.0).shift(RIGHT * 3.2 + UP * 0.5)
        wass_text = Text('"Khối lượng phải\ndi chuyển xa\nbao nhiêu?"',
                         font_size=SIZE_SMALL, color=THEME_AMBER, font=FONT_PRIMARY, line_spacing=1.1
                         ).move_to(wass_box)

        self.play(Write(compare_title), run_time=0.8)
        self.play(
            DrawBorderThenFill(fd_box), FadeIn(fd_text, shift=RIGHT * 0.15),
            Write(vs_text),
            DrawBorderThenFill(wass_box), FadeIn(wass_text, shift=LEFT * 0.15),
            run_time=1.5,
        )
        self.play(Indicate(wass_box, color=THEME_AMBER, scale_factor=1.05), run_time=0.9)
        self.wait(7.0)
        self.play(FadeOut(compare_title), FadeOut(fd_box), FadeOut(fd_text), FadeOut(vs_text),
                  FadeOut(wass_box), FadeOut(wass_text), run_time=0.7)

        # ── STAGE 2: Transport diagram ────────────────────────────────────
        axes = Axes(
            x_range=[0, 7, 1], y_range=[-0.5, 3.5, 1],
            x_length=7.5, y_length=3.8, tips=False,
            axis_config={"color": GRID_COLOR, "stroke_width": 1.2},
        ).shift(UP * 0.1)
        x_lbl = Text("không gian feature", font_size=SIZE_SMALL, color=TEXT_MUTED, font=FONT_PRIMARY
                     ).next_to(axes, DOWN, buff=0.15).align_to(axes, RIGHT).shift(LEFT * 0.2)
        self.play(Create(axes), FadeIn(x_lbl), run_time=0.9)

        np.random.seed(7)
        p_centers = [(1.2, 2.1), (1.8, 1.5), (1.0, 0.8), (2.2, 2.5), (1.5, 0.4)]
        q_centers = [(4.5, 2.4), (5.1, 1.7), (4.8, 0.9), (5.5, 2.8), (4.2, 0.5)]

        p_dots = VGroup(*[Dot(axes.c2p(x, y), radius=0.115, color=THEME_BLUE)
                          for x, y in p_centers])
        q_dots = VGroup(*[Dot(axes.c2p(x, y), radius=0.115, color=THEME_AMBER)
                          for x, y in q_centers])
        p_label = Text("P", font_size=SIZE_BODY, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD
                       ).next_to(p_dots, UP, buff=0.28)
        q_label = Text("Q", font_size=SIZE_BODY, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD
                       ).next_to(q_dots, UP, buff=0.28)

        self.play(
            LaggedStart(*[FadeIn(d, scale=0.3) for d in p_dots], lag_ratio=0.15),
            Write(p_label), run_time=1.3,
        )
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.3) for d in q_dots], lag_ratio=0.15),
            Write(q_label), run_time=1.3,
        )
        self.wait(9.0)

        # ── STAGE 3: Transport arrows ─────────────────────────────────────
        transport_arrows = VGroup()
        cost_labels = VGroup()
        total_cost = 0.0
        for (px, py), (qx, qy) in zip(p_centers, q_centers):
            ps = axes.c2p(px, py); qs = axes.c2p(qx, qy)
            dist = np.sqrt((qx - px)**2 + (qy - py)**2)
            total_cost += dist
            arr  = Arrow(ps, qs, color=THEME_PURPLE, buff=0.13, stroke_width=2.2,
                         tip_length=0.14, max_tip_length_to_length_ratio=0.35)
            cost = Text(f"{dist:.1f}", font_size=16, color=TEXT_MUTED, font=FONT_PRIMARY
                        ).move_to((np.array(ps) + np.array(qs)) / 2 + UP * 0.2)
            transport_arrows.add(arr); cost_labels.add(cost)

        transport_lbl = Text("Chi phí vận chuyển khối lượng P → Q",
                             font_size=SIZE_CAPTION, color=THEME_PURPLE, font=FONT_PRIMARY
                             ).to_edge(DOWN, buff=1.2)
        self.play(Write(transport_lbl), run_time=0.7)
        self.play(
            LaggedStart(*[GrowArrow(a) for a in transport_arrows], lag_ratio=0.18),
            run_time=2.0,
        )
        self.play(
            LaggedStart(*[FadeIn(c, shift=DOWN * 0.1) for c in cost_labels], lag_ratio=0.18),
            run_time=1.2,
        )
        # ShowPassingFlash trên arrow đầu tiên — signature effect
        self.play(
            ShowPassingFlash(transport_arrows[0].copy().set_stroke(THEME_PURPLE_LIGHT, width=7),
                             time_width=0.5),
            run_time=0.8,
        )
        flow_dots = VGroup(*[
            Dot(arrow.get_start(), radius=0.045, color=THEME_PURPLE_LIGHT)
            for arrow in transport_arrows
        ])
        flow_paths = [
            Line(arrow.get_start(), arrow.get_end())
            for arrow in transport_arrows
        ]
        self.play(FadeIn(flow_dots, scale=0.4), run_time=0.2)
        self.play(
            LaggedStart(*[
                MoveAlongPath(flow_dots[i], flow_paths[i])
                for i in range(len(flow_dots))
            ], lag_ratio=0.12),
            run_time=1.2,
            rate_func=smooth,
        )
        self.play(FadeOut(flow_dots), run_time=0.2)
        self.wait(5.4)

        # Tổng chi phí
        cost_num = DecimalNumber(0.0, num_decimal_places=1, font_size=SIZE_BODY, color=THEME_PURPLE
                                 ).to_edge(RIGHT, buff=1.0).shift(UP * 0.4)
        cost_title = Text("Tổng W", font_size=SIZE_SMALL, color=TEXT_MUTED, font=FONT_PRIMARY
                          ).next_to(cost_num, UP, buff=0.15)
        self.play(FadeIn(cost_title), FadeIn(cost_num), run_time=0.5)
        self.play(ChangeDecimalToValue(cost_num, total_cost, run_time=1.5, rate_func=smooth))
        self.wait(5.5)

        # ── STAGE 4: Formula ──────────────────────────────────────────────
        wass_formula = MathTex(
            r"W_p(P, Q) = \min_{\gamma \in \Gamma(P,Q)}",
            r"\mathbb{E}_{(x,y)\sim\gamma}",
            r"\left[\|x - y\|^p\right]^{1/p}",
            font_size=SIZE_CAPTION + 2, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=1.05)
        wass_formula[0].set_color(THEME_AMBER)
        self.play(Write(wass_formula), run_time=1.5)
        self.wait(8.0)

        # ── STAGE 5: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "Wasserstein nhìn geometry qua chi phí vận chuyển.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeOut(transport_lbl), FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(24.0)
        fade_out_all(self)
