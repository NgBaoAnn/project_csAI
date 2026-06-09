"""
Scene 31: Crop Yield
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


class CropYieldScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: Sweeping field scanner (no overlaps)
        field_box = RoundedRectangle(
            width=7.5, height=2.8, corner_radius=0.12,
            stroke_color=TEXT_MUTED, stroke_width=1.5,
            fill_color=BG_PANEL, fill_opacity=0.4
        )
        field_box.move_to(DOWN * 0.8)

        # Grid of dots inside: 3 rows, 8 columns
        dots = VGroup()
        target_colors = []
        for col_idx in range(8):
            cx = -3.0 + col_idx * 0.85
            for row_idx in range(3):
                cy = -0.8 + (1 - row_idx) * 0.75
                dot = Circle(radius=0.14, stroke_color=TEXT_MUTED, fill_color=TEXT_MUTED,
                             fill_opacity=0.4, stroke_width=1.5)
                dot.move_to([cx, cy, 0])
                dots.add(dot)
                if col_idx + row_idx < 5:
                    target_colors.append(THEME_BLUE)
                else:
                    target_colors.append(THEME_AMBER)

        self.play(FadeIn(field_box), FadeIn(dots), run_time=1.0)
        self.wait(0.3)

        sweeping_line = Line(start=[-3.7, 0.5, 0], end=[-3.7, -2.1, 0], color=THEME_PURPLE, stroke_width=3.5)
        sweeping_line_glow = create_3b1b_glow(sweeping_line, color=THEME_PURPLE, n_layers=3, opacity=0.12)
        sweeping_group = VGroup(sweeping_line_glow, sweeping_line)

        self.play(FadeIn(sweeping_group), run_time=0.5)

        title_text = Text("Crop Yield", font_size=SIZE_TITLE - 4, font=FONT_PRIMARY, weight=BOLD)
        title_text.set_color_by_gradient(THEME_BLUE, THEME_BLUE_LIGHT)
        title_glow = create_3b1b_glow(title_text, color=THEME_BLUE, n_layers=4, opacity=0.15)
        title_group = VGroup(title_glow, title_text)
        title_group.move_to(UP * 1.8)

        subtitle_text = Text("Biến crop type ẩn lộ ra qua prediction", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_group, DOWN, buff=0.25)

        self.play(
            sweeping_group.animate.move_to([3.7, -0.8, 0]),
            LaggedStart(
                *[dot.animate.set_stroke(color=tc, width=2.5).set_fill(color=tc, opacity=0.8)
                  for dot, tc in zip(dots, target_colors)],
                lag_ratio=0.08, run_time=3.2
            ),
            FadeIn(title_group, shift=UP * 0.2),
            Write(subtitle_text),
            run_time=3.5
        )

        self.play(FadeOut(sweeping_group), run_time=0.5)
        # seg 0: Title introduction
        play_voiceover_and_wait(self, 31, 0)

        # Transition out
        self.play(FadeOut(field_box), FadeOut(dots), FadeOut(title_group), FadeOut(subtitle_text), run_time=1.0)
        self.wait(0.5)

        # Subtitle 1
        sub1 = create_bottom_caption("Trong bài toán crop yield, climate features dự đoán năng suất.")
        self.play(FadeIn(sub1))
        # seg 1: "climate features dự đoán năng suất..."
        play_voiceover_and_wait(self, 31, 1)

        # Draw maps
        map_size = 4
        spacing = 0.5

        def create_map(center, colors):
            grid = VGroup()
            for r in range(map_size):
                for c in range(map_size):
                    idx = r * map_size + c
                    color = colors[idx]
                    dot = Circle(radius=0.18, stroke_color=color, fill_color=color, fill_opacity=0.6, stroke_width=2)
                    dot.move_to(center + RIGHT * (c - (map_size-1)/2) * spacing + DOWN * (r - (map_size-1)/2) * spacing)
                    grid.add(dot)
            return grid

        true_colors = []
        for r in range(map_size):
            for c in range(map_size):
                if r + c < map_size:
                    true_colors.append(THEME_BLUE)
                else:
                    true_colors.append(THEME_AMBER)

        left_center = LEFT * 3.5 + UP * 0.4
        left_map = create_map(left_center, true_colors)
        left_label = Text("Bản đồ loại cây trồng thực tế\n(Ground Truth)", font_size=SIZE_SMALL - 2, color=TEXT_PRIMARY, font=FONT_PRIMARY).next_to(left_map, UP, buff=0.4)
        left_group = VGroup(left_map, left_label)

        hidden_colors = [TEXT_MUTED] * (map_size * map_size)
        right_center = RIGHT * 3.5 + UP * 0.4
        right_map = create_map(right_center, hidden_colors)
        right_label = Text("Bản đồ phân tách học được\n(Không có nhãn Crop)", font_size=SIZE_SMALL - 2, color=TEXT_PRIMARY, font=FONT_PRIMARY).next_to(right_map, UP, buff=0.4)
        right_group = VGroup(right_map, right_label)

        self.play(FadeIn(left_group, shift=RIGHT * 0.2), run_time=TIME_NORMAL)
        # seg 2: "bản đồ loại cây trồng thực tế: xanh là ngô, vàng là đậu nành..."
        play_voiceover_and_wait(self, 31, 2)

        # Subtitle 2
        sub2 = create_bottom_caption("Nhưng cơ chế năng suất thay đổi mạnh tùy theo loại cây trồng (crop type).")
        self.play(Transform(sub1, sub2))
        # seg 3: "cơ chế năng suất thay đổi theo crop type, ban đầu không có nhãn..."
        play_voiceover_and_wait(self, 31, 3)

        self.play(FadeIn(right_group, shift=LEFT * 0.2), run_time=TIME_NORMAL)
        self.wait(0.5)

        # Subtitle 3
        sub3 = create_bottom_caption("Predictive heterogeneity có thể học được subpopulation ẩn này qua dự đoán.")
        self.play(Transform(sub1, sub3))
        # seg 4: "predictive heterogeneity học subpopulation ẩn qua dự đoán..."
        play_voiceover_and_wait(self, 31, 4)

        # Arrow showing learning process
        learning_arrow = Arrow(left_map.get_right(), right_map.get_left(), color=THEME_PURPLE, stroke_width=4, buff=0.25)
        arrow_label = Text("PH Split", font_size=SIZE_SMALL - 4, color=THEME_PURPLE, font=FONT_PRIMARY).next_to(learning_arrow, UP, buff=0.1)

        self.play(GrowArrow(learning_arrow), Write(arrow_label), run_time=TIME_NORMAL)
        self.wait(0.5)

        # Right map updates to match left map colors
        right_colors_target = VGroup(*[
            Circle(radius=0.18, stroke_color=color, fill_color=color, fill_opacity=0.6, stroke_width=2).move_to(right_map[i].get_center())
            for i, color in enumerate(true_colors)
        ])
        glow_right = VGroup(*[create_3b1b_glow(dot, color=dot.stroke_color, n_layers=3, opacity=0.12) for dot in right_colors_target])

        self.play(
            *[ReplacementTransform(right_map[i], right_colors_target[i]) for i in range(len(right_map))],
            FadeIn(glow_right),
            run_time=TIME_SLOW
        )
        self.wait(0.5)

        alignment_text = Text("Khớp hoàn hảo! (Độ chính xác: 96%)", font_size=SIZE_SMALL - 2, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).next_to(learning_arrow, DOWN, buff=0.25)
        self.play(Write(alignment_text), run_time=TIME_NORMAL)
        # seg 5: "bản đồ học được khớp gần hoàn hảo với thực tế, dù biến bị ẩn..."
        play_voiceover_and_wait(self, 31, 5)

        # Insight Takeaway
        insight = create_insight_box(
            "Cơ chế ẩn có thể được phát hiện qua prediction.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.75)

        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        # seg 6: "cơ chế ẩn có thể phát hiện qua prediction..."
        play_voiceover_and_wait(self, 31, 6)

        # Outro
        self.play(
            FadeOut(left_map), FadeOut(left_label), FadeOut(right_label),
            FadeOut(right_colors_target), FadeOut(learning_arrow), FadeOut(arrow_label),
            FadeOut(glow_right), FadeOut(alignment_text), FadeOut(insight),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
