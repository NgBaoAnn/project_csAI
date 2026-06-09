"""
Scene 23: IRM Limits
Author: TV3 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


class IRMLimitsScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # ── 1. Intro: Warning Split Line ─────────────────────────────────────
        split_line = Line(LEFT * 6, RIGHT * 6, color=THEME_RED, stroke_width=3)
        title_text = Text("IRM Limits", font_size=SIZE_TITLE - 8,
                          color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD)
        subtitle_text = Text("Điều gì xảy ra nếu environments không đủ tốt?",
                             font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        title_text.next_to(split_line, UP, buff=0.2)
        subtitle_text.next_to(split_line, DOWN, buff=0.2)

        self.play(Create(split_line), run_time=0.8)
        glow_line = create_3b1b_glow(split_line, color=THEME_RED, n_layers=4, opacity=0.15)
        self.play(
            FadeIn(glow_line),
            Write(title_text),
            FadeIn(subtitle_text, shift=DOWN * 0.1),
            run_time=1.5,
        )
        self.play(split_line.animate.set_color(THEME_ORANGE), run_time=0.4)
        self.play(split_line.animate.set_color(THEME_RED),    run_time=0.4)

        # seg 0: Title introduction
        play_voiceover_and_wait(self, 23, 0)

        self.play(
            FadeOut(title_text), FadeOut(subtitle_text),
            FadeOut(split_line), FadeOut(glow_line),
            run_time=TIME_FAST,
        )
        self.wait(0.5)

        # ── 2. Subtitle 1 + 3 Training Environments ──────────────────────────
        sub1 = create_bottom_caption(
            "Nếu mọi training environment giữ cùng một shortcut, shortcut đó cũng trông invariant."
        )
        self.play(FadeIn(sub1))

        # seg 1: giải thích vấn đề — đọc trước khi env xuất hiện
        play_voiceover_and_wait(self, 23, 2)

        # Build 3 training environment panels
        panel_w, panel_h = 3.25, 2.3

        def make_train_env(label_text, label_color):
            box = RoundedRectangle(
                width=panel_w, height=panel_h,
                corner_radius=0.1,
                stroke_color=label_color, stroke_width=2,
            )
            lbl = Text(label_text, font_size=SIZE_CAPTION,
                       color=label_color, font=FONT_PRIMARY, weight=BOLD)
            lbl.move_to(box.get_top() + DOWN * 0.42)

            feat_grass = Text("Nền cỏ (90%)", font_size=SIZE_SMALL,
                              color=THEME_EMERALD, font=FONT_PRIMARY)
            feat_grass.move_to(box.get_center() + UP * 0.25)
            fit_to_width(feat_grass, max_width=panel_w * 0.82)

            feat_shape = Text("Hình dáng bò", font_size=SIZE_SMALL,
                              color=TEXT_PRIMARY, font=FONT_PRIMARY)
            feat_shape.move_to(box.get_center() + DOWN * 0.45)
            fit_to_width(feat_shape, max_width=panel_w * 0.82)

            return VGroup(box, lbl, feat_grass, feat_shape)

        env1 = make_train_env("Environment 1", THEME_BLUE)
        env2 = make_train_env("Environment 2", THEME_BLUE)
        env3 = make_train_env("Environment 3", THEME_BLUE)

        train_envs = VGroup(env1, env2, env3)
        train_envs.arrange(RIGHT, buff=0.45)
        fit_to_frame(train_envs, max_width=11.2, max_height=2.8)
        train_envs.move_to(UP * 1.2)

        self.play(FadeIn(train_envs, shift=DOWN * 0.2), run_time=TIME_SLOW)

        # seg 3: "Ba training environments ở đây đều giống nhau..."
        play_voiceover_and_wait(self, 23, 3)

        # ── 3. Highlight grass background as "invariant" ─────────────────────
        # Collect the feat_grass objects from each env (index 2 in each VGroup)
        grass_group = VGroup(env1[2], env2[2], env3[2])
        inv_frame = SurroundingRectangle(grass_group, color=THEME_EMERALD, buff=0.12)
        inv_text = Text("Có vẻ invariant khi train", font_size=SIZE_CAPTION,
                        color=THEME_EMERALD, font=FONT_PRIMARY)
        inv_text.next_to(train_envs, DOWN, buff=0.22)

        self.play(Create(inv_frame), Write(inv_text), run_time=TIME_NORMAL)

        # seg 4: "Đường viền xanh bao quanh feature nền cỏ..."
        play_voiceover_and_wait(self, 23, 4)

        # ── 4. Subtitle 2: cần env đa dạng ───────────────────────────────────
        sub2 = create_bottom_caption(
            "IRM cần environments đủ đa dạng để lộ ra feature không ổn định."
        )
        self.play(Transform(sub1, sub2))

        # seg 5: "IRM cần environments đủ đa dạng..."
        play_voiceover_and_wait(self, 23, 5)

        # ── 5. Test environment (beach) xuất hiện ────────────────────────────
        test_box = RoundedRectangle(
            width=panel_w, height=panel_h,
            corner_radius=0.1,
            stroke_color=THEME_RED, stroke_width=3,
        )
        test_label = Text("Test Environment", font_size=SIZE_CAPTION,
                          color=THEME_RED, font=FONT_PRIMARY, weight=BOLD)
        test_label.move_to(test_box.get_top() + DOWN * 0.42)

        test_feat1 = Text("Nền bãi biển (100%)", font_size=SIZE_SMALL,
                          color=THEME_RED, font=FONT_PRIMARY)
        test_feat1.move_to(test_box.get_center() + UP * 0.25)
        fit_to_width(test_feat1, max_width=panel_w * 0.82)

        test_feat2 = Text("Hình dáng bò", font_size=SIZE_SMALL,
                          color=THEME_EMERALD, font=FONT_PRIMARY)
        test_feat2.move_to(test_box.get_center() + DOWN * 0.45)
        fit_to_width(test_feat2, max_width=panel_w * 0.82)

        env_test = VGroup(test_box, test_label, test_feat1, test_feat2)
        env_test.move_to(DOWN * 0.9)

        self.play(
            train_envs.animate.scale(0.82).shift(UP * 0.5),
            inv_frame.animate.scale(0.82).shift(UP * 0.5),
            FadeOut(inv_text),
            FadeIn(env_test, shift=UP * 0.2),
            run_time=TIME_NORMAL,
        )

        # seg 6: "Test environment có nền bãi biển 100 phần trăm..."
        play_voiceover_and_wait(self, 23, 6)

        # ── 6. Failure indicator ──────────────────────────────────────────────
        cross = Cross(test_feat1, stroke_color=THEME_RED, stroke_width=5)
        fail_text = Text("Shortcut bị phá vỡ!", font_size=SIZE_CAPTION,
                         color=THEME_RED, font=FONT_PRIMARY, weight=BOLD)
        fail_text.next_to(test_box, RIGHT, buff=0.4)

        self.play(Create(cross), Write(fail_text), run_time=TIME_NORMAL)
        self.wait(1.0)

        # ── 7. Insight ────────────────────────────────────────────────────────
        insight = create_insight_box(
            "Environments xấu tạo ra invariance kém.",
            color=THEME_RED,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.75)

        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL,
        )

        # seg 7: "Environments xấu tạo ra invariance kém..."
        play_voiceover_and_wait(self, 23, 7)

        # ── Outro ─────────────────────────────────────────────────────────────
        self.play(
            FadeOut(insight), FadeOut(train_envs),
            FadeOut(inv_frame), FadeOut(env_test),
            FadeOut(cross), FadeOut(fail_text),
            run_time=TIME_NORMAL,
        )
        self.wait(1.0)
