"""
Scene 32: COVID Mortality
Author: TV4 (Animation Lead)
Duration: ~75 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class COVIDMortalityScene(Scene):
    def make_feature_panel(self, title_text, values, bar_color, center_pos):
        # values: [Age, Underlying Disease, Symptoms]
        
        # 1. Title
        title = Text(title_text, font_size=SIZE_SMALL - 4, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=BOLD, line_spacing=0.85)
        
        # 2. Features list
        feature_names = ["Tuổi", "Bệnh nền", "Triệu chứng"]
        features_group = VGroup()
        for i, val in enumerate(values):
            label = Text(feature_names[i], font_size=SIZE_SMALL - 6, color=TEXT_SECONDARY, font=FONT_PRIMARY)
            bar_bg = Rectangle(width=1.6, height=0.18, color=GRID_COLOR, stroke_width=0, fill_color=GRID_COLOR, fill_opacity=1.0)
            
            # Row group using absolute left alignment to avoid vertical/horizontal offsets
            row = VGroup(label, bar_bg)
            label.move_to(LEFT * 1.5, aligned_edge=LEFT)
            bar_bg.move_to(LEFT * 0.1, aligned_edge=LEFT)
            
            # Foreground bar aligned exactly over bar_bg
            bar_fg = Rectangle(width=max(1.6 * val, 0.05), height=0.18, color=bar_color, stroke_width=0, fill_color=bar_color, fill_opacity=0.8)
            bar_fg.move_to(bar_bg.get_center())
            bar_fg.align_to(bar_bg, LEFT)
            
            row.add(bar_fg)
            features_group.add(row)
            
        features_group.arrange(DOWN, buff=0.25)
        
        content = VGroup(title, features_group).arrange(DOWN, buff=0.35)
        
        box = RoundedRectangle(
            width=max(content.get_width() + 0.8, 3.8),
            height=content.get_height() + 0.7,
            corner_radius=0.1,
            stroke_color=TEXT_MUTED,
            stroke_width=1.5,
            fill_color=BG_PANEL,
            fill_opacity=0.75
        )
        
        content.move_to(box.get_center())
        
        panel = VGroup(box, content).move_to(center_pos)
        return panel

    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Heartbeat ECG Pulse
        ecg_points = [
            LEFT * 5 + DOWN * 0.5,
            LEFT * 1 + DOWN * 0.5,
            LEFT * 0.7 + DOWN * 1.0,
            LEFT * 0.4 + UP * 1.8,
            LEFT * 0.1 + DOWN * 1.4,
            RIGHT * 0.2 + DOWN * 0.5,
            RIGHT * 5 + DOWN * 0.5
        ]
        ecg_path = VMobject(color=THEME_ORANGE, stroke_width=4)
        ecg_path.set_points_as_corners(ecg_points)
        
        self.play(Create(ecg_path), run_time=TIME_NORMAL)
        
        peak_pos = LEFT * 0.4 + UP * 1.8
        peak_dot = Dot(peak_pos, color=THEME_ORANGE, radius=0.12)
        peak_glow = create_3b1b_glow(peak_dot, color=THEME_ORANGE, n_layers=5, opacity=0.3)
        
        self.play(FadeIn(peak_dot), FadeIn(peak_glow), run_time=TIME_FAST)
        self.wait(0.2)
        
        # Pulse beat 1 (heartbeat effect)
        self.play(peak_dot.animate.scale(1.4), peak_glow.animate.scale(1.3), run_time=0.25)
        self.play(peak_dot.animate.scale(1.0/1.4), peak_glow.animate.scale(1.0/1.3), run_time=0.25)
        self.wait(0.15)
        # Pulse beat 2
        self.play(peak_dot.animate.scale(1.4), peak_glow.animate.scale(1.3), run_time=0.25)
        self.play(peak_dot.animate.scale(1.0/1.4), peak_glow.animate.scale(1.0/1.3), run_time=0.25)
        self.wait(0.5)
        
        title_text = Text("COVID Mortality", font_size=SIZE_TITLE, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_ORANGE, THEME_AMBER)
        title_glow = create_3b1b_glow(title_text, color=THEME_ORANGE, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text).move_to(UP * 0.5)
        
        subtitle_text = Text("Một dataset chứa nhiều cơ chế rủi ro", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.3)
        
        self.play(
            FadeOut(ecg_path),
            ReplacementTransform(VGroup(peak_dot, peak_glow), title_group),
            FadeIn(subtitle_text, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(4.5)
        self.play(
            FadeOut(title_group),
            FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        
        # Subtitle 1
        sub1 = create_bottom_caption("Mô hình ERM trung bình hiển thị các đặc trưng rủi ro chung của COVID.")
        self.play(FadeIn(sub1))
        self.wait(6.5)
        
        # Draw initial Average ERM Panel
        center_pos = UP * 0.5
        erm_panel = self.make_feature_panel("Mô hình ERM trung bình", [0.7, 0.5, 0.6], THEME_BLUE, center_pos)
        
        self.play(FadeIn(erm_panel, shift=UP * 0.25), run_time=TIME_NORMAL)
        self.wait(8.0)
        
        # Subtitle 2
        sub2 = create_bottom_caption("Nhưng khi phân tách subpopulations, hai cơ chế rủi ro khác biệt xuất hiện.")
        self.play(Transform(sub1, sub2))
        self.wait(7.5)
        
        # Split: shift ERM panel left and transform into Subpopulation 1
        left_pos = LEFT * 3.5 + UP * 0.5
        right_pos = RIGHT * 3.5 + UP * 0.5
        
        sub1_panel = self.make_feature_panel("Subpopulation 1\n(Người cao tuổi - Bệnh nền)", [0.95, 0.9, 0.25], THEME_ORANGE, left_pos)
        sub2_panel = self.make_feature_panel("Subpopulation 2\n(Cộng đồng - Triệu chứng)", [0.3, 0.2, 0.95], THEME_EMERALD, right_pos)
        
        split_label = Text("PH Split", font_size=SIZE_SMALL - 4, color=THEME_PURPLE, font=FONT_PRIMARY).move_to(UP * 0.5)
        split_arrow1 = Arrow(start=split_label.get_left(), end=sub1_panel[0].get_right(), color=THEME_PURPLE, stroke_width=3, buff=0.15)
        split_arrow2 = Arrow(start=split_label.get_right(), end=sub2_panel[0].get_left(), color=THEME_PURPLE, stroke_width=3, buff=0.15)
        
        self.play(
            ReplacementTransform(erm_panel, sub1_panel),
            FadeIn(sub2_panel, shift=LEFT * 0.2),
            Create(split_arrow1), Create(split_arrow2), Write(split_label),
            run_time=TIME_SLOW
        )
        self.wait(7.0)
        
        # Subtitle 3
        sub3 = create_bottom_caption("Nhóm lớn tuổi bị chi phối bởi bệnh nền; nhóm còn lại nhạy cảm với triệu chứng hô hấp.")
        self.play(Transform(sub1, sub3))
        
        # Glow the dominant features to emphasize
        glow_sub1 = VGroup(
            create_3b1b_glow(sub1_panel[1][1][0][2], color=THEME_ORANGE, n_layers=3, opacity=0.15),
            create_3b1b_glow(sub1_panel[1][1][1][2], color=THEME_ORANGE, n_layers=3, opacity=0.15)
        )
        glow_sub2 = create_3b1b_glow(sub2_panel[1][1][2][2], color=THEME_EMERALD, n_layers=3, opacity=0.15)
        
        self.play(
            FadeIn(glow_sub1), FadeIn(glow_sub2),
            run_time=TIME_NORMAL
        )
        self.wait(12.0)
        
        # Takeaway
        insight = create_insight_box(
            "Một dataset có thể chứa nhiều cơ chế rủi ro.",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)
        
        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL
        )
        self.wait(14.5)
        
        # Outro
        self.play(
            FadeOut(sub1_panel), FadeOut(sub2_panel), FadeOut(glow_sub1), FadeOut(glow_sub2),
            FadeOut(split_arrow1), FadeOut(split_arrow2), FadeOut(split_label), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
