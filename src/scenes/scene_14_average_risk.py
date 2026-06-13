"""Scene 14: Average Risk Hides Worst Groups.
Author: TV2  |  Duration: ~70 giây
Câu hỏi: Accuracy trung bình có thể che giấu thất bại nào?
Note: Custom bars (không dùng BarChart/LaTeX).
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait

TARGET_DURATION_SECONDS = 70


class AverageRiskScene(Scene):

    def _make_bar(self, val, color, bar_w=1.65, bar_h_max=3.5):
        h = bar_h_max * (val / 100.0)
        bar = Rectangle(
            width=bar_w, height=h,
            fill_color=color, fill_opacity=0.85,
            stroke_color=color, stroke_width=1.8,
        )
        return bar

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Risk trung bình",
                           '"Trung bình" có thể che giấu nhóm yếu')

        # ── STAGE 1: Số to 95% với counting animation ─────────────────────
        count_num = Integer(0, font_size=144, color=THEME_EMERALD)
        pct_sign = Text("%", font_size=90, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD
                        ).next_to(count_num, RIGHT, buff=0.12).shift(DOWN * 0.15)
        # Add a dynamic updater to keep % next to the growing count_num
        pct_sign.add_updater(lambda m: m.next_to(count_num, RIGHT, buff=0.12).shift(DOWN * 0.15))
        counter_group = VGroup(count_num, pct_sign).shift(UP * 0.25)
        glow = create_3b1b_glow(counter_group, color=THEME_EMERALD, n_layers=5, opacity=0.20)
        avg_caption = Text("Accuracy trung bình: model có vẻ rất tốt",
                           font_size=SIZE_BODY, color=TEXT_SECONDARY, font=FONT_PRIMARY
                           ).next_to(counter_group, DOWN, buff=0.5)

        self.add(glow)
        self.play(
            ChangeDecimalToValue(count_num, 95, run_time=2.2, rate_func=rush_from),
            GrowFromCenter(pct_sign, run_time=1.2),
        )
        self.play(FadeIn(avg_caption, shift=UP * 0.1), run_time=0.7)
        play_voiceover_and_wait(self, 14, 0)
        self.wait(7.5)

        # ── STAGE 2: Vỡ ra thành bar chart theo nhóm ─────────────────────
        BAR_DATA = [
            (99, THEME_BLUE,   "Nhóm lớn (85%)", "99%"),
            (87, THEME_AMBER,  "Nhóm nhỏ A (10%)", "87%"),
            (43, THEME_RED,    "Nhóm nhỏ B (5%)",  "43%"),
        ]
        GAP = 0.55
        chart_bottom = DOWN * 1.4
        bars, labels, pcts = VGroup(), VGroup(), VGroup()
        for i, (val, color, lbl_str, pct_str) in enumerate(BAR_DATA):
            bar = self._make_bar(val, color)
            bar.align_to(chart_bottom, DOWN).shift(RIGHT * (i - 1) * (1.65 + GAP))
            lbl = Text(lbl_str, font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY
                       ).next_to(bar, DOWN, buff=0.18)
            pct = Text(pct_str, font_size=SIZE_BODY, color=color, font=FONT_PRIMARY, weight=BOLD
                       ).next_to(bar, UP, buff=0.14)
            bars.add(bar); labels.add(lbl); pcts.add(pct)

        chart_title = Text("Accuracy theo nhóm", font_size=SIZE_CAPTION,
                           color=TEXT_SECONDARY, font=FONT_PRIMARY).to_edge(UP, buff=1.0)

        # Counter nhỏ lại, bars xuất hiện
        pct_sign.clear_updaters()
        self.play(
            counter_group.animate.scale(0.45).to_edge(UP, buff=0.55).set_color(TEXT_MUTED),
            FadeOut(glow), FadeOut(avg_caption),
            run_time=1.2,
        )
        self.play(Write(chart_title), run_time=0.5)
        self.play(
            LaggedStart(*[GrowFromEdge(b, DOWN) for b in bars], lag_ratio=0.25),
            run_time=1.8,
            rate_func=smooth,
        )
        self.play(
            LaggedStart(*[FadeIn(l, shift=UP * 0.1) for l in labels], lag_ratio=0.2),
            LaggedStart(*[FadeIn(p, shift=DOWN * 0.1) for p in pcts], lag_ratio=0.2),
            run_time=1.0,
        )
        self.wait(7.0)

        # Đường avg
        avg_y = chart_bottom[1] + 3.5 * 0.95
        avg_line = DashedLine(LEFT * 3.8 + UP * avg_y, RIGHT * 3.8 + UP * avg_y,
                              color=TEXT_MUTED, stroke_width=2.2, dash_length=0.14)
        avg_lbl = Text("TB 95%", font_size=SIZE_SMALL, color=TEXT_MUTED, font=FONT_PRIMARY
                       ).next_to(avg_line, RIGHT, buff=0.12)
        self.play(Create(avg_line), FadeIn(avg_lbl), run_time=0.9)
        self.play(
            ShowPassingFlash(avg_line.copy().set_stroke(WHITE, width=6), time_width=0.5),
            run_time=0.7,
        )
        self.play(
            Indicate(bars[0], color=THEME_BLUE, scale_factor=1.04),
            Indicate(avg_lbl, color=TEXT_PRIMARY, scale_factor=1.12),
            run_time=0.8,
        )
        self.wait(2.5)
        self.play(
            ShowPassingFlash(bars[2].copy().set_stroke(THEME_RED_LIGHT, width=6), time_width=0.45),
            run_time=0.7,
        )
        self.wait(1.5)

        # ── STAGE 3: Highlight nhóm tệ nhất ──────────────────────────────
        worst_bar = bars[2]
        worst_glow = create_3b1b_glow(worst_bar, color=THEME_RED, n_layers=4, opacity=0.30)
        worst_brace = Brace(worst_bar, RIGHT, color=THEME_RED, buff=0.15)
        worst_txt = Text("Nhóm yếu nhất: 43%", font_size=SIZE_CAPTION,
                         color=THEME_RED, font=FONT_PRIMARY, weight=BOLD
                         ).next_to(worst_brace, RIGHT, buff=0.15)

        self.play(
            worst_bar.animate.set_fill(THEME_RED, opacity=1.0).set_stroke(THEME_RED, width=3),
            FadeIn(worst_glow),
            GrowFromCenter(worst_brace),
            FadeIn(worst_txt, shift=UP * 0.1),
            run_time=1.2,
        )
        self.play(Flash(worst_bar, color=THEME_RED, flash_radius=0.8, line_length=0.25), run_time=0.5)
        play_voiceover_and_wait(self, 14, 1)
        self.wait(7.0)

        # Context
        context = Text(
            "Trong y tế, tín dụng, tuyển dụng — nhóm nhỏ có thể là nhóm quan trọng nhất.",
            font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=1.0)
        self.play(Write(context), run_time=1.5)
        self.wait(7.5)

        # ── STAGE 4: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "Hiệu năng trung bình có thể che giấu lỗi cục bộ.",
            color=THEME_RED, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeOut(context), FadeIn(insight, shift=UP * 0.2), run_time=0.9)
        self.wait(8.0)
        self.play(Circumscribe(insight, color=THEME_RED, time_width=0.5), run_time=0.8)
        play_voiceover_and_wait(self, 14, 2)
        self.wait(9.2)
        fade_out_all(self)
