"""Scene 13: ERM Formula.
Author: TV2  |  Duration: ~80 giây
Câu hỏi: ERM đang tối ưu thứ gì — và vì sao đó là vấn đề?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait

TARGET_DURATION_SECONDS = 80


class ERMFormulaScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "ERM",
                           "Tối thiểu hóa risk thực nghiệm")

        # ── STAGE 1: Build formula từng phần ─────────────────────────────
        theta_part = MathTex(r"\hat{\theta}", font_size=SIZE_FORMULA, color=THEME_BLUE)
        eq_part    = MathTex(r"=", font_size=SIZE_FORMULA, color=TEXT_MUTED)
        min_part   = MathTex(r"\arg\min_{\theta}", font_size=SIZE_FORMULA, color=TEXT_PRIMARY)
        avg_part   = MathTex(r"\frac{1}{n} \sum_{i=1}^{n}", font_size=SIZE_FORMULA, color=THEME_AMBER)
        loss_part  = MathTex(r"\mathcal{L}(f_\theta(x_i),\, y_i)", font_size=SIZE_FORMULA, color=TEXT_PRIMARY)

        formula = VGroup(theta_part, eq_part, min_part, avg_part, loss_part
                         ).arrange(RIGHT, buff=0.22).shift(UP * 0.8)

        # Ghi từng phần có stagger tự nhiên
        self.play(
            LaggedStart(
                Write(theta_part), Write(eq_part), Write(min_part),
                Write(avg_part), Write(loss_part),
                lag_ratio=0.45,
            ),
            run_time=3.0,
        )
        play_voiceover_and_wait(self, 13, 0)
        self.wait(7.0)

        # ── STAGE 2: Highlight phần "average" ────────────────────────────
        avg_box = SurroundingRectangle(avg_part, color=THEME_AMBER, buff=0.15,
                                       corner_radius=0.08, stroke_width=2.5)
        avg_caption = Text("trung bình trên toàn dữ liệu train",
                           font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY
                           ).next_to(formula, DOWN, buff=0.6)
        self.play(Create(avg_box), Write(avg_caption), run_time=1.0)
        self.play(Indicate(avg_part, color=THEME_AMBER, scale_factor=1.15), run_time=0.8)
        self.wait(3.8)
        self.play(
            ShowPassingFlash(avg_box.copy().set_stroke(THEME_AMBER_LIGHT, width=5), time_width=0.5),
            run_time=0.8,
        )
        self.wait(2.4)

        # ── STAGE 3: Minh hoạ 6 mẫu — bars tăng dần ─────────────────────
        self.play(
            FadeOut(avg_box),
            FadeOut(avg_caption),
            formula.animate.scale(0.85).to_edge(UP, buff=0.6),
            run_time=1.0,
        )
        self.wait(3.0)

        losses = [0.82, 0.34, 1.10, 0.55, 0.70, 0.90]
        chart_bottom = DOWN * 0.5
        bars = VGroup()
        bar_labels = VGroup()
        for i, loss in enumerate(losses):
            bar = Rectangle(
                width=0.38, height=loss * 1.3,
                fill_color=THEME_BLUE, fill_opacity=0.8,
                stroke_color=THEME_BLUE, stroke_width=1.0,
            ).align_to(chart_bottom, DOWN).shift(RIGHT * (-2.2 + i * 0.8))
            lbl = Text(f"L{i+1}", font_size=14, color=TEXT_MUTED, font=FONT_PRIMARY
                       ).next_to(bar, DOWN, buff=0.1)
            bars.add(bar); bar_labels.add(lbl)

        demo_title = Text("Ví dụ: n=6 mẫu và loss từng mẫu",
                          font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY
                          ).to_edge(DOWN, buff=1.8)
        self.play(Write(demo_title), run_time=0.7)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.18),
            LaggedStart(*[FadeIn(l) for l in bar_labels], lag_ratio=0.18),
            run_time=2.0,
        )
        weight_labels = VGroup(*[
            MathTex(r"1/n", font_size=20, color=THEME_AMBER).next_to(bar, UP, buff=0.12)
            for bar in bars
        ])
        self.play(
            LaggedStart(*[FadeIn(w, shift=DOWN * 0.08) for w in weight_labels], lag_ratio=0.08),
            run_time=0.9,
        )
        self.play(ApplyWave(weight_labels), run_time=0.8)

        # Đường avg — signature ShowPassingFlash
        avg_loss = sum(losses) / len(losses)
        avg_line = DashedLine(
            bars.get_left() + LEFT * 0.15 + UP * avg_loss * 1.3,
            bars.get_right() + RIGHT * 0.15 + UP * avg_loss * 1.3,
            color=THEME_AMBER, stroke_width=2.8, dash_length=0.15,
        )
        avg_line_lbl = Text(f"trung bình = {avg_loss:.2f}", font_size=SIZE_SMALL,
                            color=THEME_AMBER, font=FONT_PRIMARY).next_to(avg_line, RIGHT, buff=0.15)
        self.play(Create(avg_line), FadeIn(avg_line_lbl), run_time=0.9)
        self.play(
            ShowPassingFlash(avg_line.copy().set_stroke(THEME_AMBER_LIGHT, width=8), time_width=0.5),
            run_time=0.8,
        )
        play_voiceover_and_wait(self, 13, 1)
        self.wait(6.3)

        # ── STAGE 4: Limitation ───────────────────────────────────────────
        limit = Text("ERM cho mọi mẫu cùng trọng số; dễ bỏ qua nhóm ẩn.",
                     font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY
                     ).to_edge(DOWN, buff=1.05)
        self.play(Transform(demo_title, limit), run_time=1.0)
        self.wait(6.5)

        # ── STAGE 5: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "ERM tối ưu loss trung bình trên dữ liệu train.",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeOut(demo_title), FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(15.0)
        self.play(
            Circumscribe(insight, color=THEME_AMBER, time_width=0.55),
            ShowPassingFlash(avg_line.copy().set_stroke(THEME_AMBER_LIGHT, width=7), time_width=0.45),
            run_time=1.1,
        )
        play_voiceover_and_wait(self, 13, 2)
        self.wait(16.2)
        fade_out_all(self)
