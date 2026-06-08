"""Scene 15: Spurious Cow/Camel.
Author: TV2  |  Duration: ~80 giây
Câu hỏi: Model học con vật hay học background?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 80


class SpuriousCowCamelScene(Scene):

    def _panel(self, name, bg_color, shape_color, pos):
        """Tạo panel gồm nền + hình animal đơn giản + nhãn."""
        panel = RoundedRectangle(
            width=2.7, height=2.5, corner_radius=0.1,
            stroke_color=TEXT_MUTED, fill_color=BG_DARK,
            fill_opacity=0.0, stroke_width=1.8,
        ).move_to(pos)
        bg = RoundedRectangle(
            width=2.55, height=2.35, corner_radius=0.08,
            fill_color=bg_color, fill_opacity=0.22, stroke_width=0,
        ).move_to(pos)
        body = Ellipse(width=1.05, height=0.58,
                       color=shape_color, fill_opacity=0.88, fill_color=shape_color)
        head = Circle(radius=0.23, color=shape_color,
                      fill_opacity=0.88, fill_color=shape_color
                      ).next_to(body, RIGHT, buff=-0.06).shift(UP * 0.12)
        shape = VGroup(body, head).move_to(pos + DOWN * 0.12)
        label = Text(name, font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY
                     ).next_to(panel, DOWN, buff=0.22)
        return VGroup(panel, bg, shape, label), bg, shape

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Spurious correlation",
                           "Tương quan giả: model học con vật hay background?")

        # ── STAGE 1: Hai panels slide vào ────────────────────────────────
        cow_grp,   cow_bg,   cow_shape   = self._panel("Bò — trên cỏ",       THEME_EMERALD, THEME_BLUE,   LEFT * 2.9 + UP * 0.3)
        camel_grp, camel_bg, camel_shape = self._panel("Lạc đà — sa mạc",    THEME_AMBER,   THEME_ORANGE, RIGHT * 2.9 + UP * 0.3)

        cow_grp.shift(LEFT * 5)
        camel_grp.shift(RIGHT * 5)

        train_label = Text("Dữ liệu train",
                           font_size=SIZE_BODY, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=MEDIUM
                           ).to_edge(UP, buff=0.65)
        self.play(Write(train_label), run_time=0.7)
        self.play(
            cow_grp.animate.shift(RIGHT * 5),
            camel_grp.animate.shift(LEFT * 5),
            run_time=1.2, rate_func=smooth,
        )
        self.wait(9.0)

        # ── STAGE 2: Highlight background (spurious) ──────────────────────
        bg_note = Text("ERM học background: feature giả",
                       font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY
                       ).to_edge(DOWN, buff=1.35)
        bg_underline = create_chalk_underline(bg_note, color=THEME_RED)

        box_cow   = SurroundingRectangle(cow_bg,   color=THEME_RED, buff=0.05, corner_radius=0.06, stroke_width=2.5)
        box_camel = SurroundingRectangle(camel_bg, color=THEME_RED, buff=0.05, corner_radius=0.06, stroke_width=2.5)
        glow_cow   = create_3b1b_glow(cow_bg,   color=THEME_RED, n_layers=3, opacity=0.22)
        glow_camel = create_3b1b_glow(camel_bg, color=THEME_RED, n_layers=3, opacity=0.22)

        self.play(
            cow_bg.animate.set_fill(opacity=0.50),
            camel_bg.animate.set_fill(opacity=0.50),
            FadeIn(glow_cow), FadeIn(glow_camel),
            Create(box_cow), Create(box_camel),
            Write(bg_note), Create(bg_underline),
            run_time=1.4,
        )
        self.wait(8.0)

        # ── STAGE 3: Highlight shape (causal) ────────────────────────────
        self.play(
            FadeOut(bg_note), FadeOut(bg_underline),
            FadeOut(box_cow), FadeOut(box_camel),
            FadeOut(glow_cow), FadeOut(glow_camel),
            run_time=0.6,
        )
        shape_note = Text("Shape là tín hiệu thật: cơ chế nhân quả",
                          font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY
                          ).to_edge(DOWN, buff=1.35)
        glow_cow_s   = create_3b1b_glow(cow_shape,   color=THEME_EMERALD, n_layers=3, opacity=0.25)
        glow_camel_s = create_3b1b_glow(camel_shape, color=THEME_EMERALD, n_layers=3, opacity=0.25)

        self.play(
            FadeIn(glow_cow_s), FadeIn(glow_camel_s),
            Indicate(cow_shape,   color=THEME_EMERALD, scale_factor=1.2),
            Indicate(camel_shape, color=THEME_EMERALD, scale_factor=1.2),
            Write(shape_note),
            run_time=1.4,
        )
        self.wait(8.0)

        # ── STAGE 4: Test time — bò ở bãi biển ───────────────────────────
        self.play(
            FadeOut(camel_grp), FadeOut(glow_camel_s),
            FadeOut(glow_cow_s), FadeOut(shape_note),
            run_time=0.9,
        )
        test_label = Text("Test time: bò ở bãi biển (môi trường mới)",
                          font_size=SIZE_BODY, color=THEME_AMBER, font=FONT_PRIMARY, weight=MEDIUM
                          ).to_edge(UP, buff=0.65)
        self.play(
            cow_grp.animate.move_to(ORIGIN + UP * 0.2).scale(1.18),
            Transform(train_label, test_label),
            run_time=1.2,
        )
        # Background đổi màu sang vàng (bãi biển)
        self.play(cow_bg.animate.set_fill(THEME_AMBER, opacity=0.35), run_time=0.8)
        self.wait(5.5)

        # ── STAGE 5: Dự đoán sai ─────────────────────────────────────────
        wrong_pred = Text(
            "Model dự đoán:\nlạc đà?  ✗",
            font_size=SIZE_SUBSECTION,
            color=THEME_RED,
            font=FONT_PRIMARY,
            weight=BOLD,
            line_spacing=0.9,
        ).move_to(RIGHT * 3.55 + UP * 0.15)
        wrong_glow = create_3b1b_glow(wrong_pred, color=THEME_RED, n_layers=3, opacity=0.20)

        self.play(
            Flash(cow_bg, color=THEME_RED, flash_radius=1.2, line_length=0.3, num_lines=12),
            run_time=0.6,
        )
        self.play(FadeIn(wrong_glow), Write(wrong_pred), run_time=1.2)
        bg_signal = Dot(cow_bg.get_center(), radius=0.07, color=THEME_RED_LIGHT)
        bg_path = Line(bg_signal.get_center(), wrong_pred.get_left() + LEFT * 0.15)
        self.play(FadeIn(bg_signal, scale=0.4), run_time=0.3)
        self.play(MoveAlongPath(bg_signal, bg_path), run_time=0.9, rate_func=smooth)
        self.play(FadeOut(bg_signal), run_time=0.3)
        self.wait(6.0)

        explain = Text(
            "Background đổi → model fail.\nShape chưa được học như tín hiệu ổn định.",
            font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY, line_spacing=1.3,
        ).to_edge(DOWN, buff=1.0)
        self.play(Write(explain), run_time=1.5)
        self.wait(6.5)

        # ── STAGE 6: Insight ─────────────────────────────────────────────
        insight = create_insight_box(
            "Spurious correlation: đúng trong train, sai khi môi trường đổi.",
            color=THEME_RED, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeOut(explain), FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(20.0)
        fade_out_all(self)
