"""
Scene 34: HRM Loop
Author: TV4 (Animation Lead)
Duration: ~75 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


class HRMLoopScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: Custom infinity circles morphing into title box
        left_circle = Circle(radius=1.0, color=THEME_AMBER, stroke_width=4).shift(LEFT * 0.9)
        right_circle = Circle(radius=1.0, color=THEME_BLUE, stroke_width=4).shift(RIGHT * 0.9)
        infinity = VGroup(left_circle, right_circle)

        self.play(FadeIn(infinity), run_time=TIME_NORMAL)
        self.play(Rotate(infinity, angle=PI, about_point=ORIGIN), run_time=TIME_NORMAL)

        title_box = RoundedRectangle(width=5.5, height=2.0, corner_radius=0.15, stroke_color=THEME_PURPLE, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6)
        self.play(ReplacementTransform(infinity, title_box), run_time=TIME_NORMAL)

        title_text = Text("HRM Loop", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_AMBER, THEME_BLUE)
        title_glow = create_3b1b_glow(title_text, color=THEME_BLUE, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(title_box.get_center())
        subtitle_text = Text("Đồng tiến hóa môi trường và mô hình dự đoán", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_box, DOWN, buff=0.3)

        self.play(FadeIn(title_group), Write(subtitle_text), run_time=TIME_NORMAL)
        # seg 0: Title introduction
        play_voiceover_and_wait(self, 34, 0)
        self.play(FadeOut(title_box), FadeOut(title_group), FadeOut(subtitle_text), run_time=TIME_FAST)

        # Subtitle 1
        sub1 = create_bottom_caption("HRM giải quyết vấn đề bằng chu trình co-evolution gồm hai module.")
        self.play(FadeIn(sub1))
        # seg 1: "HRM dùng chu trình đồng tiến hóa gồm hai module..."
        play_voiceover_and_wait(self, 34, 1)

        # Two blocks
        id_box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.08, stroke_color=THEME_AMBER, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6).shift(LEFT * 3.5 + UP * 1.1)
        id_title = Text("Heterogeneity\nIdentification", font_size=SIZE_SMALL - 4, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).move_to(id_box.get_center())
        id_block = VGroup(id_box, id_title)

        pred_box = RoundedRectangle(width=3.6, height=1.6, corner_radius=0.08, stroke_color=THEME_BLUE, stroke_width=2.5, fill_color=BG_PANEL, fill_opacity=0.6).shift(RIGHT * 3.5 + UP * 1.1)
        pred_title = Text("Invariant\nPrediction", font_size=SIZE_SMALL - 4, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(pred_box.get_center())
        pred_block = VGroup(pred_box, pred_title)

        self.play(FadeIn(id_block, shift=RIGHT * 0.25), FadeIn(pred_block, shift=LEFT * 0.25), run_time=TIME_NORMAL)
        # seg 2: "module 1 identification, module 2 invariant prediction..."
        play_voiceover_and_wait(self, 34, 2)

        # Subtitle 2
        sub2 = create_bottom_caption("Identification phân nhóm dữ liệu thành các môi trường nhân tạo.")
        self.play(Transform(sub1, sub2))
        # seg 3: "identification phân nhóm dữ liệu thành environment nhân tạo..."
        play_voiceover_and_wait(self, 34, 3)

        arrow_top = CurvedArrow(id_box.get_top() + RIGHT * 0.2, pred_box.get_top() + LEFT * 0.2, angle=-TAU/5, color=THEME_PURPLE, stroke_width=3)
        arrow_bottom = CurvedArrow(pred_box.get_bottom() + LEFT * 0.2, id_box.get_bottom() + RIGHT * 0.2, angle=-TAU/5, color=THEME_PURPLE, stroke_width=3)

        self.play(Create(arrow_top), run_time=TIME_NORMAL)
        self.wait(0.5)

        # Subtitle 3
        sub3 = create_bottom_caption("Invariant prediction học predictor ổn định từ các môi trường vừa tìm thấy.")
        self.play(Transform(sub1, sub3))
        # seg 4: "invariant prediction học predictor ổn định từ environment vừa tìm..."
        play_voiceover_and_wait(self, 34, 4)

        self.play(Create(arrow_bottom), run_time=TIME_NORMAL)
        self.wait(0.5)

        # Accuracy text
        center_lower = DOWN * 1.0
        acc_label = Text("Worst-Group Accuracy:", font_size=SIZE_SMALL - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).move_to(center_lower + LEFT * 2.0)
        acc_val = Text("55%", font_size=SIZE_BODY, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).next_to(acc_label, RIGHT, buff=0.25)
        acc_val_glow = create_3b1b_glow(acc_val, color=THEME_RED, n_layers=3, opacity=0.15)

        self.play(
            FadeIn(acc_label, shift=UP * 0.2),
            FadeIn(acc_val_glow, shift=UP * 0.2),
            FadeIn(acc_val, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        # seg 5: "ban đầu worst-group accuracy chỉ 55 phần trăm..."
        play_voiceover_and_wait(self, 34, 5)

        # Loop animation
        acc_val_mid = Text("72%", font_size=SIZE_BODY, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).move_to(acc_val.get_center())
        acc_val_final = Text("89%", font_size=SIZE_BODY, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(acc_val.get_center())
        acc_val_glow_final = create_3b1b_glow(acc_val_final, color=THEME_EMERALD, n_layers=3, opacity=0.15)

        self.play(
            ShowPassingFlash(arrow_top.copy().set_color(THEME_AMBER_LIGHT), time_width=0.4),
            Transform(acc_val, acc_val_mid),
            run_time=1.2
        )
        self.wait(0.8)
        self.play(
            ShowPassingFlash(arrow_bottom.copy().set_color(THEME_BLUE_LIGHT), time_width=0.4),
            Transform(acc_val, acc_val_final),
            Transform(acc_val_glow, acc_val_glow_final),
            run_time=1.2
        )
        # seg 6: "qua mỗi vòng lặp, accuracy tăng dần 72 rồi 89 phần trăm..."
        play_voiceover_and_wait(self, 34, 6)

        # Takeaway
        insight = create_insight_box(
            "Phát hiện environment và invariant learning có thể đồng tiến hóa.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.55)

        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 7: "phát hiện environment và invariant learning đồng tiến hóa..."
        play_voiceover_and_wait(self, 34, 7)

        # Outro
        self.play(
            FadeOut(id_block), FadeOut(pred_block), FadeOut(arrow_top), FadeOut(arrow_bottom),
            FadeOut(acc_label), FadeOut(acc_val), FadeOut(acc_val_glow), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
