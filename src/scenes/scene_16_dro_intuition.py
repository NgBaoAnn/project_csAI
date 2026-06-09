"""Scene 16: DRO Intuition.
Author: TV2  |  Duration: ~70 giây
Câu hỏi: Nếu average không đủ, ta tối ưu worst-case được không?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 70


class DROIntuitionScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Trực giác DRO",
                           "Từ trung bình sang worst-case")

        # ── STAGE 1: ERM formula ─────────────────────────────────────────
        erm_label = Text("ERM", font_size=SIZE_CAPTION, color=TEXT_MUTED, font=FONT_PRIMARY
                         ).to_edge(UP, buff=0.75)
        erm = MathTex(
            r"\min_{\theta}",
            r"\mathbb{E}_{P_{\mathrm{train}}}",
            r"\left[\mathcal{L}(\theta)\right]",
            font_size=SIZE_FORMULA, color=TEXT_PRIMARY,
        ).shift(UP * 0.5)
        erm[1].set_color(THEME_BLUE)

        self.play(Write(erm_label), run_time=0.6)
        self.play(
            LaggedStart(Write(erm[0]), Write(erm[1]), Write(erm[2]), lag_ratio=0.5),
            run_time=2.0,
        )
        self.play(Indicate(erm[1], color=THEME_BLUE, scale_factor=1.15), run_time=0.8)
        self.wait(7.0)

        erm_limit = Text(
            "ERM chỉ tối ưu trên P_train; chưa xét shift có thể xảy ra",
            font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=1.15)
        self.play(Write(erm_limit), run_time=1.2)
        self.wait(6.0)

        # ── STAGE 2: ERM → DRO transform ─────────────────────────────────
        dro_label = Text("DRO", font_size=SIZE_CAPTION, color=THEME_AMBER,
                         font=FONT_PRIMARY, weight=BOLD).to_edge(UP, buff=0.75)
        dro = MathTex(
            r"\min_{\theta}",
            r"\sup_{Q \in \mathcal{U}}",
            r"\mathbb{E}_{Q}",
            r"\left[\mathcal{L}(\theta)\right]",
            font_size=SIZE_FORMULA, color=TEXT_PRIMARY,
        ).shift(UP * 0.5)
        dro[1].set_color(THEME_RED)
        dro[2].set_color(THEME_RED)

        transform_note = Text("↓  worst-case: shift xấu nhất",
                              font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY
                              ).next_to(erm, DOWN, buff=0.35)
        self.play(FadeOut(erm_limit), Write(transform_note), run_time=0.8)
        self.wait(1.2)
        self.play(
            Transform(erm_label, dro_label),
            TransformMatchingShapes(erm, dro),
            FadeOut(transform_note),
            run_time=2.2,
            rate_func=smooth,
        )
        self.wait(6.5)

        # Highlight sup_Q
        sup_box = SurroundingRectangle(dro[1], color=THEME_RED, buff=0.15,
                                       corner_radius=0.06, stroke_width=2.0)
        sup_annot = Text("adversary: chọn Q xấu nhất trong tập U",
                         font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY
                         ).next_to(sup_box, UP, buff=0.25)
        self.play(Create(sup_box), FadeIn(sup_annot, shift=DOWN * 0.1), run_time=0.9)
        # ShowPassingFlash là hiệu ứng chính
        self.play(
            ShowPassingFlash(dro.copy().set_stroke(THEME_AMBER_LIGHT, width=6), time_width=0.35),
            run_time=0.9,
        )
        self.wait(6.0)

        # ── STAGE 3: Two-player game ──────────────────────────────────────
        self.play(FadeOut(sup_box), FadeOut(sup_annot), run_time=0.5)
        self.play(dro.animate.scale(0.72).to_edge(UP, buff=1.05), run_time=0.8)

        theta_circle = Circle(radius=0.72, color=THEME_BLUE, fill_opacity=0.20
                              ).shift(LEFT * 2.7 + DOWN * 0.55)
        theta_label = Text("θ", font_size=SIZE_SECTION, color=THEME_BLUE, font=FONT_PRIMARY
                           ).move_to(theta_circle)
        theta_annot = Text("model\n(bên giảm loss)", font_size=SIZE_SMALL, color=THEME_BLUE,
                           font=FONT_PRIMARY, line_spacing=0.9).next_to(theta_circle, DOWN, buff=0.22)
        theta_glow = create_3b1b_glow(theta_circle, color=THEME_BLUE, n_layers=4, opacity=0.18)

        q_circle = Circle(radius=0.72, color=THEME_RED, fill_opacity=0.20
                          ).shift(RIGHT * 2.7 + DOWN * 0.55)
        q_label = Text("Q", font_size=SIZE_SECTION, color=THEME_RED, font=FONT_PRIMARY
                       ).move_to(q_circle)
        q_annot = Text("phân phối\n(bên làm khó)", font_size=SIZE_SMALL, color=THEME_RED,
                       font=FONT_PRIMARY, line_spacing=0.9).next_to(q_circle, DOWN, buff=0.22)
        q_glow = create_3b1b_glow(q_circle, color=THEME_RED, n_layers=4, opacity=0.18)

        self.play(
            GrowFromCenter(theta_glow), GrowFromCenter(theta_circle),
            Write(theta_label), FadeIn(theta_annot),
            GrowFromCenter(q_glow), GrowFromCenter(q_circle),
            Write(q_label), FadeIn(q_annot),
            run_time=1.2,
        )

        arrow_min = Arrow(theta_circle.get_right(), q_circle.get_left(),
                          color=THEME_BLUE, buff=0.12, stroke_width=2.8)
        arrow_max = Arrow(q_circle.get_left() + DOWN * 0.22, theta_circle.get_right() + DOWN * 0.22,
                          color=THEME_RED, buff=0.12, stroke_width=2.8)
        min_lbl = Text("min: giảm loss", font_size=SIZE_SMALL, color=THEME_BLUE, font=FONT_PRIMARY
                       ).next_to(arrow_min, UP, buff=0.08)
        max_lbl = Text("max/sup: tăng loss", font_size=SIZE_SMALL, color=THEME_RED, font=FONT_PRIMARY
                       ).next_to(arrow_max, DOWN, buff=0.08)

        self.play(GrowArrow(arrow_min), FadeIn(min_lbl), run_time=0.8)
        self.play(GrowArrow(arrow_max), FadeIn(max_lbl), run_time=0.8)
        # Một lần flash mỗi hướng để thể hiện game loop
        self.play(
            ShowPassingFlash(arrow_min.copy().set_stroke(THEME_BLUE_LIGHT, width=7), time_width=0.5),
            run_time=0.6,
        )
        self.play(
            ShowPassingFlash(arrow_max.copy().set_stroke(THEME_RED_LIGHT, width=7), time_width=0.5),
            run_time=0.6,
        )
        self.play(
            theta_circle.animate.scale(1.12),
            theta_label.animate.scale(1.12),
            q_circle.animate.scale(0.88),
            q_label.animate.scale(0.88),
            run_time=0.7,
            rate_func=there_and_back,
        )
        self.play(
            q_circle.animate.scale(1.12),
            q_label.animate.scale(1.12),
            theta_circle.animate.scale(0.88),
            theta_label.animate.scale(0.88),
            run_time=0.7,
            rate_func=there_and_back,
        )
        self.wait(2.8)
        self.play(
            ShowPassingFlash(VGroup(arrow_min, arrow_max).copy().set_stroke(THEME_AMBER_LIGHT, width=6), time_width=0.45),
            run_time=0.9,
        )
        self.wait(2.4)

        # ── STAGE 4: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "DRO chuẩn bị cho một họ shift xấu đã chọn.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(8.0)
        self.play(Circumscribe(insight, color=THEME_AMBER, time_width=0.5), run_time=0.8)
        self.wait(8.2)
        fade_out_all(self)
