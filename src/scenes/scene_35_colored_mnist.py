"""
Scene 35: ColoredMNIST
Author: TV4 (Animation Lead)
Duration: ~75 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class ColoredMNISTScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Flashing pixel grid disintegrating to reveal title
        grid_size = 4
        square_side = 0.3
        spacing = 0.1
        pixels = VGroup()
        import random
        random.seed(35)
        
        for r in range(grid_size):
            for c in range(grid_size):
                color_idx = 0 if random.random() > 0.5 else 1
                color = THEME_EMERALD if color_idx == 0 else THEME_RED
                sq = Square(side_length=square_side, fill_color=color, fill_opacity=0.8, stroke_width=0)
                sq.move_to(RIGHT * (c - (grid_size-1)/2) * (square_side + spacing) + UP * (r - (grid_size-1)/2) * (square_side + spacing))
                sq.color_idx = color_idx
                pixels.add(sq)
                
        self.play(FadeIn(pixels), run_time=0.4)
        
        # Fast flashing (alternating red and emerald)
        flash_anims = []
        for sq in pixels:
            sq.color_idx = 1 - sq.color_idx
            new_color = THEME_RED if sq.color_idx == 1 else THEME_EMERALD
            flash_anims.append(sq.animate.set_fill(new_color))
        self.play(*flash_anims, run_time=0.25)
        
        flash_anims2 = []
        for sq in pixels:
            sq.color_idx = 1 - sq.color_idx
            new_color = THEME_RED if sq.color_idx == 1 else THEME_EMERALD
            flash_anims2.append(sq.animate.set_fill(new_color))
        self.play(*flash_anims2, run_time=0.2)
        
        # Disintegration: pixels move outward and fade out
        disintegrate_anims = []
        for i, sq in enumerate(pixels):
            angle = random.uniform(0, 2 * PI)
            dist = random.uniform(2.0, 3.5)
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            disintegrate_anims.append(
                sq.animate.move_to(sq.get_center() + direction * dist).set_opacity(0)
            )
            
        title_text = Text("Colored MNIST", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_EMERALD, THEME_RED)
        title_glow = create_3b1b_glow(title_text, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        
        subtitle_text = Text("Màu sắc hay hình dạng mới là đặc trưng bất biến?", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)
        
        self.play(
            *disintegrate_anims,
            FadeIn(title_group, scale=0.9),
            Write(subtitle_text),
            run_time=1.5
        )
        self.wait(3.5)
        
        self.play(
            FadeOut(title_group),
            FadeOut(subtitle_text),
            FadeOut(pixels),
            run_time=TIME_FAST
        )
        
        # Subtitle 1
        sub1 = create_bottom_caption("ColoredMNIST là benchmark kinh điển để kiểm chứng spurious correlation.")
        self.play(FadeIn(sub1))
        self.wait(6.0)
        
        # Draw Train Panel (Left - Shifted UP to UP * 0.8)
        train_box = RoundedRectangle(width=4.0, height=3.2, corner_radius=0.1, stroke_color=THEME_BLUE, stroke_width=2.5)
        train_title = Text("Train Environment\n(90% màu xanh cho số '5')", font_size=SIZE_SMALL - 4, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(train_box.get_top() + DOWN * 0.42)
        digit_train = Text("5", font_size=90, color=THEME_EMERALD, font="Segoe UI", weight=BOLD).move_to(train_box.get_center() + DOWN * 0.25)
        train_label = Text("Dự đoán: '5' (Đúng)", font_size=SIZE_SMALL - 4, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(train_box, DOWN, buff=0.25)
        train_group = VGroup(train_box, train_title, digit_train, train_label).shift(LEFT * 3.5 + UP * 0.8)
        
        self.play(FadeIn(train_group, shift=RIGHT * 0.25), run_time=TIME_NORMAL)
        self.wait(5.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Trong tập train, màu xanh lá giúp dự đoán '5' dễ dàng, tạo ra shortcut.")
        self.play(Transform(sub1, sub2))
        self.wait(6.5)
        
        # Draw Test Panel (Right - Shifted UP to UP * 0.8)
        test_box = RoundedRectangle(width=4.0, height=3.2, corner_radius=0.1, stroke_color=THEME_RED, stroke_width=2.5)
        test_title = Text("Test Environment\n(Đảo ngược: màu đỏ cho số '5')", font_size=SIZE_SMALL - 4, color=THEME_RED, font=FONT_PRIMARY, weight=BOLD).move_to(test_box.get_top() + DOWN * 0.42)
        digit_test = Text("5", font_size=90, color=THEME_RED, font="Segoe UI", weight=BOLD).move_to(test_box.get_center() + DOWN * 0.25)
        test_label = Text("Dự đoán: '3' (Sai!)", font_size=SIZE_SMALL - 4, color=THEME_RED, font=FONT_PRIMARY).next_to(test_box, DOWN, buff=0.25)
        test_cross = Cross(test_label, stroke_color=THEME_RED, stroke_width=3).scale(0.8)
        test_group = VGroup(test_box, test_title, digit_test, test_label, test_cross).shift(RIGHT * 3.5 + UP * 0.8)
        
        self.play(FadeIn(test_group[:-1], shift=LEFT * 0.25), run_time=TIME_NORMAL)
        self.wait(5.0)
        
        # Subtitle 3
        sub3 = create_bottom_caption("Ở tập test, tương quan màu sắc bị đảo, mô hình dựa vào màu sắc thất bại.")
        self.play(Transform(sub1, sub3))
        self.play(Create(test_cross), run_time=TIME_NORMAL)
        self.wait(7.5)
        
        # Subtitle 4
        sub4 = create_bottom_caption("Chỉ khi học được đặc trưng hình dạng (shape) bất biến, model mới robust.")
        self.play(Transform(sub1, sub4))
        self.wait(5.5)
        
        # Shape outline highlight (draw a white outline glow around both digits to represent shape learning)
        shape_glow_l = create_3b1b_glow(digit_train, color=THEME_BLUE, n_layers=4, opacity=0.2)
        shape_glow_r = create_3b1b_glow(digit_test, color=THEME_BLUE, n_layers=4, opacity=0.2)
        
        self.play(
            FadeIn(shape_glow_l), FadeIn(shape_glow_r),
            digit_train.animate.set_color(TEXT_PRIMARY),
            digit_test.animate.set_color(TEXT_PRIMARY),
            run_time=TIME_SLOW
        )
        self.wait(8.0)
        
        # Takeaway (Shifted slightly down to prevent overlap with train_label/test_label)
        insight = create_insight_box(
            "Màu sắc spurious sẽ thất bại khi environment thay đổi.",
            color=THEME_RED,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.5)
        
        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(13.0)
        
        # Outro
        self.play(
            FadeOut(train_group), FadeOut(test_group), FadeOut(shape_glow_l), FadeOut(shape_glow_r), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
