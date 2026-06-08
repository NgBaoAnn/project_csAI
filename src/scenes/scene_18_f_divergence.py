"""Scene 18: f-divergence.
Author: TV2  |  Duration: ~75 giây
Câu hỏi: f-divergence mô hình hoá shift như thế nào?
Note: Custom bars (không dùng BarChart/LaTeX).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 75


def _bar(val, color, bar_w=1.1, bar_h_max=3.0):
    h = bar_h_max * (val / 100.0)
    return Rectangle(
        width=bar_w, height=h,
        fill_color=color, fill_opacity=0.85,
        stroke_color=color, stroke_width=1.5,
    )


class FDivergenceScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "f-divergence",
                           "Shift là đổi trọng số trên dữ liệu đã có")

        # ── STAGE 1: Formula ──────────────────────────────────────────────
        header = Text("f-divergence dùng density ratio để so sánh phân phối",
                      font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY
                      ).to_edge(UP, buff=0.7)
        formula = MathTex(
            r"D_f(Q \| P) = \mathbb{E}_P\!\left[f\!\left(\frac{dQ}{dP}\right)\right]",
            font_size=SIZE_FORMULA, color=TEXT_PRIMARY,
        ).shift(UP * 1.0)
        ratio_key = MathTex(r"\frac{dQ}{dP}", font_size=SIZE_SECTION, color=THEME_AMBER
                            ).next_to(formula, DOWN, buff=0.4)
        ratio_cap = Text("= density ratio: Q nặng hơn P bao nhiêu lần",
                         font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY
                         ).next_to(ratio_key, RIGHT, buff=0.22)

        self.play(Write(header), run_time=0.7)
        self.play(Write(formula), run_time=1.6)
        self.play(Indicate(formula, color=THEME_BLUE, scale_factor=1.04), run_time=0.7)
        self.play(FadeIn(ratio_key, shift=UP * 0.1), Write(ratio_cap), run_time=1.0)
        # Signature: ShowPassingFlash trên formula
        self.play(
            ShowPassingFlash(formula.copy().set_stroke(THEME_AMBER_LIGHT, width=5), time_width=0.4),
            run_time=0.9,
        )
        self.wait(8.0)

        # ── STAGE 2: Bar charts P_train vs Q_target ───────────────────────
        self.play(FadeOut(formula), FadeOut(ratio_key), FadeOut(ratio_cap), run_time=0.7)

        # P_train bars
        bp_old   = _bar(70, THEME_BLUE  ).shift(LEFT * 3.45).align_to(DOWN * 1.5, DOWN)
        bp_young = _bar(30, THEME_EMERALD).shift(LEFT * 2.2 ).align_to(DOWN * 1.5, DOWN)
        lp_old   = Text("Lớn tuổi", font_size=15, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(bp_old,   DOWN, buff=0.14)
        lp_young = Text("Trẻ tuổi", font_size=15, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(bp_young, DOWN, buff=0.14)
        pp_old   = Text("70%", font_size=SIZE_SMALL, color=THEME_BLUE,   font=FONT_PRIMARY, weight=BOLD).next_to(bp_old,   UP, buff=0.12)
        pp_young = Text("30%", font_size=SIZE_SMALL, color=THEME_EMERALD,font=FONT_PRIMARY, weight=BOLD).next_to(bp_young, UP, buff=0.12)
        train_title = Text("P_train", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY
                           ).next_to(VGroup(bp_old, bp_young), UP, buff=0.35)

        # Q_target bars
        bq_old   = _bar(40, THEME_BLUE  ).shift(RIGHT * 1.5 ).align_to(DOWN * 1.5, DOWN)
        bq_young = _bar(60, THEME_EMERALD).shift(RIGHT * 2.75).align_to(DOWN * 1.5, DOWN)
        lq_old   = Text("Lớn tuổi", font_size=15, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(bq_old,   DOWN, buff=0.14)
        lq_young = Text("Trẻ tuổi", font_size=15, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(bq_young, DOWN, buff=0.14)
        pq_old   = Text("40%", font_size=SIZE_SMALL, color=THEME_BLUE,   font=FONT_PRIMARY, weight=BOLD).next_to(bq_old,   UP, buff=0.12)
        pq_young = Text("60%", font_size=SIZE_SMALL, color=THEME_EMERALD,font=FONT_PRIMARY, weight=BOLD).next_to(bq_young, UP, buff=0.12)
        target_title = Text("Q_target", font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY
                            ).next_to(VGroup(bq_old, bq_young), UP, buff=0.35)

        self.play(
            Write(train_title),
            LaggedStart(GrowFromEdge(bp_old, DOWN), GrowFromEdge(bp_young, DOWN), lag_ratio=0.35),
            FadeIn(lp_old), FadeIn(lp_young), FadeIn(pp_old), FadeIn(pp_young),
            run_time=1.5,
        )
        self.wait(6.5)

        # Mũi tên reweight
        mid_arrow = Arrow(LEFT * 0.8, RIGHT * 0.8, color=THEME_AMBER, stroke_width=3.0, buff=0.1)
        rw_label  = Text("reweight\nsupport đã có",
                         font_size=SIZE_SMALL, color=THEME_AMBER, font=FONT_PRIMARY, line_spacing=0.9
                         ).next_to(mid_arrow, UP, buff=0.18)
        self.play(GrowArrow(mid_arrow), Write(rw_label), run_time=1.0)
        self.play(
            ShowPassingFlash(mid_arrow.copy().set_stroke(THEME_AMBER_LIGHT, width=7),
                             time_width=0.5, run_time=0.7),
        )

        self.play(
            Write(target_title),
            LaggedStart(
                TransformFromCopy(bp_old, bq_old),
                TransformFromCopy(bp_young, bq_young),
                lag_ratio=0.35,
            ),
            FadeIn(lq_old), FadeIn(lq_young), FadeIn(pq_old), FadeIn(pq_young),
            run_time=1.5,
        )
        self.wait(8.0)

        # Density ratio labels
        r_old   = MathTex(r"\frac{dQ}{dP} \approx 0.57", font_size=22, color=THEME_BLUE
                          ).next_to(bq_old,   RIGHT, buff=0.14).shift(UP * 0.3)
        r_young = MathTex(r"\frac{dQ}{dP} = 2.0",        font_size=22, color=THEME_EMERALD
                          ).next_to(bq_young, RIGHT, buff=0.14).shift(UP * 0.3)
        self.play(FadeIn(r_old, shift=LEFT * 0.15), FadeIn(r_young, shift=LEFT * 0.15), run_time=1.0)
        self.play(Indicate(r_young, color=THEME_EMERALD, scale_factor=1.18), run_time=0.9)
        self.wait(7.0)

        # ── STAGE 3: Key property ─────────────────────────────────────────
        key_prop = Text(
            "f-divergence chỉ reweight support đã có; không thêm vùng mới.",
            font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=1.05)
        self.play(Write(key_prop), run_time=1.2)
        self.wait(7.0)

        # ── STAGE 4: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "f-divergence mô phỏng shift bằng cách reweight dữ liệu đã có.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(Transform(key_prop, insight), run_time=0.9)
        self.wait(21.0)
        fade_out_all(self)
