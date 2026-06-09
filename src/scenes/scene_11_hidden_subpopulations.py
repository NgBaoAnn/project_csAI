"""Scene 11: Hidden Subpopulations.
Author: TV2  |  Duration: ~80 giây
Câu hỏi: Khi nào một model tốt lại che giấu sự thật?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 80


class HiddenSubpopulationsScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Subpopulations ẩn",
                           "Khi một model trung bình che giấu nhiều cơ chế")

        # ── Axes ─────────────────────────────────────────────────────────
        np.random.seed(42)
        xa = np.random.uniform(-2.2, 0.1, 18)
        ya = 1.1 * xa + np.random.normal(0, 0.25, 18) - 0.3
        xb = np.random.uniform(-0.1, 2.2, 18)
        yb = -0.9 * xb + np.random.normal(0, 0.25, 18) + 0.5

        axes = Axes(
            x_range=[-3, 3, 1], y_range=[-3, 3, 1],
            x_length=6.5, y_length=5.0, tips=False,
            axis_config={"color": GRID_COLOR, "stroke_width": 1.5},
        ).shift(LEFT * 0.4 + DOWN * 0.2)
        x_label = Text("X (đặc trưng)", font_size=SIZE_SMALL, color=TEXT_MUTED, font=FONT_PRIMARY
                       ).next_to(axes, DOWN, buff=0.25)
        y_label = Text("Y", font_size=SIZE_SMALL, color=TEXT_MUTED, font=FONT_PRIMARY
                       ).next_to(axes, LEFT, buff=0.12)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=1.2)
        self.wait(5.0)

        # ── STAGE 1: Gray pooled dots ─────────────────────────────────────
        gray_a = VGroup(*[Dot(axes.c2p(xa[i], ya[i]), radius=0.065, color=TEXT_MUTED, fill_opacity=0.75)
                          for i in range(len(xa))])
        gray_b = VGroup(*[Dot(axes.c2p(xb[i], yb[i]), radius=0.065, color=TEXT_MUTED, fill_opacity=0.75)
                          for i in range(len(xb))])

        pooled_label = Text("Dataset gộp: mọi mẫu đều màu xám",
                      font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY
                      ).to_edge(UP, buff=0.65)
        self.play(Write(pooled_label), run_time=0.8)
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.4) for d in VGroup(*gray_a, *gray_b)], lag_ratio=0.04),
            run_time=2.0,
        )
        self.wait(8.0)

        # ── STAGE 2: Average line ─────────────────────────────────────────
        avg_line = axes.plot(lambda x: 0.08 * x + 0.08, x_range=[-2.8, 2.8],
                             color=TEXT_MUTED, stroke_width=3.5)
        avg_label = Text("đường trung bình", font_size=SIZE_CAPTION, color=TEXT_MUTED, font=FONT_PRIMARY
                         ).next_to(avg_line.get_end(), RIGHT, buff=0.15)
        bad_note = Text("Đường trung bình không mô tả đúng bất kỳ nhóm nào.",
                        font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY
                        ).to_edge(DOWN, buff=1.0)

        self.play(Create(avg_line), Write(avg_label), run_time=1.2)
        self.play(avg_line.animate.set_stroke(color=THEME_RED, opacity=0.65),
                  Write(bad_note), run_time=1.0)
        self.play(
            ShowPassingFlash(avg_line.copy().set_stroke(THEME_RED_LIGHT, width=7), time_width=0.45),
            run_time=0.7,
        )
        residual_points = [
            (xa[2], ya[2]), (xa[8], ya[8]), (xa[14], ya[14]),
            (xb[3], yb[3]), (xb[9], yb[9]), (xb[15], yb[15]),
        ]
        residuals = VGroup(*[
            DashedLine(
                axes.c2p(x, y),
                axes.c2p(x, 0.08 * x + 0.08),
                color=THEME_RED,
                stroke_width=2.2,
                dash_length=0.08,
            )
            for x, y in residual_points
        ])
        self.play(
            LaggedStart(*[Create(r) for r in residuals], lag_ratio=0.18),
            run_time=1.1,
        )
        self.play(Flash(residuals, color=THEME_RED_LIGHT, flash_radius=0.18, line_length=0.08), run_time=0.5)
        self.wait(6.7)

        # ── STAGE 3: Color reveal ─────────────────────────────────────────
        col_a = VGroup(*[Dot(axes.c2p(xa[i], ya[i]), radius=0.075, color=THEME_BLUE)
                         for i in range(len(xa))])
        col_b = VGroup(*[Dot(axes.c2p(xb[i], yb[i]), radius=0.075, color=THEME_AMBER)
                         for i in range(len(xb))])
        legend_a = VGroup(Dot(radius=0.07, color=THEME_BLUE),
                          Text("Nhóm A", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY)
                          ).arrange(RIGHT, buff=0.15)
        legend_b = VGroup(Dot(radius=0.07, color=THEME_AMBER),
                          Text("Nhóm B", font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY)
                          ).arrange(RIGHT, buff=0.15)
        legend = VGroup(legend_a, legend_b).arrange(DOWN, aligned_edge=LEFT, buff=0.2
                        ).to_edge(RIGHT, buff=0.5).shift(UP * 0.5)

        self.play(
            FadeOut(pooled_label),
            FadeOut(bad_note),
            FadeOut(avg_label),
            FadeOut(residuals),
            run_time=0.5,
        )
        self.play(
            Transform(gray_a, col_a),
            Transform(gray_b, col_b),
            avg_line.animate.set_stroke(opacity=0.28),
            FadeIn(legend),
            run_time=1.8,
        )
        reveal_note = Text("Hai cơ chế Y|X khác nhau: độ dốc ngược chiều.",
                           font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY
                           ).to_edge(UP, buff=0.65)
        self.play(Write(reveal_note), run_time=0.9)
        mechanism_formula = MathTex(
            r"P_A(Y\mid X) \neq P_B(Y\mid X)",
            font_size=SIZE_SUBSECTION,
            color=TEXT_PRIMARY,
        ).to_edge(DOWN, buff=1.1)
        mechanism_formula[0][0:2].set_color(THEME_BLUE)
        mechanism_formula[0][9:11].set_color(THEME_AMBER)
        self.play(Write(mechanism_formula), run_time=1.0)
        self.play(Circumscribe(mechanism_formula, color=THEME_AMBER, time_width=0.6), run_time=0.8)
        self.wait(5.2)

        # ── STAGE 4: Two regression lines ────────────────────────────────
        line_a = axes.plot(lambda x: 1.1 * x - 0.3, x_range=[-2.5, 0.2],
                           color=THEME_BLUE, stroke_width=4.0)
        line_b = axes.plot(lambda x: -0.9 * x + 0.5, x_range=[-0.2, 2.5],
                           color=THEME_AMBER, stroke_width=4.0)
        self.play(Create(line_a), Create(line_b), run_time=1.2, rate_func=smooth)
        # Signature effect: ShowPassingFlash trên hai đường
        self.play(
            ShowPassingFlash(line_a.copy().set_stroke(THEME_BLUE_LIGHT, width=9), time_width=0.45),
            ShowPassingFlash(line_b.copy().set_stroke(THEME_AMBER_LIGHT, width=9), time_width=0.45),
            run_time=1.0,
        )
        self.wait(4.0)
        self.play(
            LaggedStart(
                ShowPassingFlash(line_a.copy().set_stroke(THEME_BLUE_LIGHT, width=8), time_width=0.4),
                ShowPassingFlash(line_b.copy().set_stroke(THEME_AMBER_LIGHT, width=8), time_width=0.4),
                lag_ratio=0.25,
            ),
            run_time=1.3,
        )
        self.wait(3.7)

        # ── STAGE 5: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "Một model trung bình có thể che giấu nhiều cơ chế.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeOut(mechanism_formula), FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(12.0)
        self.play(Circumscribe(insight, color=THEME_AMBER, time_width=0.5), run_time=0.9)
        self.wait(12.1)
        fade_out_all(self)
