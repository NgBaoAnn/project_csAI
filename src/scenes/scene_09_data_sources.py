"""Scene 09: Data đến từ nhiều sources."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


TARGET_DURATION_SECONDS = 70


class DataSourcesScene(Scene):
    def source_box(self, name, color):
        box = RoundedRectangle(
            width=2.1,
            height=0.85,
            corner_radius=0.07,
            stroke_color=color,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        )
        label = Text(name, font_size=SIZE_CAPTION, color=color, font=FONT_PRIMARY)
        return VGroup(box, label)

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Nhiều nguồn dữ liệu", "Training data là một mixture")

        sources = VGroup(
            self.source_box("Nguồn A", THEME_BLUE),
            self.source_box("Nguồn B", THEME_AMBER),
            self.source_box("Nguồn C", THEME_EMERALD),
            self.source_box("Nguồn D", THEME_PURPLE),
        ).arrange(DOWN, buff=0.28).to_edge(LEFT, buff=0.9)

        training = RoundedRectangle(
            width=3.6,
            height=2.4,
            corner_radius=0.08,
            stroke_color=TEXT_PRIMARY,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        ).shift(RIGHT * 2.2)
        training_label = Text("Dữ liệu train", font_size=SIZE_BODY, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(training.get_top() + DOWN * 0.5)
        mixture_label = Text("hỗn hợp", font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY).move_to(training.get_bottom() + UP * 0.45)

        dots = VGroup()
        colors = [THEME_BLUE, THEME_AMBER, THEME_EMERALD, THEME_PURPLE]
        for row in range(4):
            for col in range(5):
                dots.add(Dot(
                    training.get_center() + LEFT * 1.1 + RIGHT * 0.55 * col + UP * 0.35 - DOWN * 0.25 * row,
                    radius=0.045,
                    color=colors[(row + col) % len(colors)],
                ))

        arrows = VGroup(*[
            Arrow(source.get_right(), training.get_left(), color=source[0].get_stroke_color(), buff=0.15, stroke_width=2.5)
            for source in sources
        ])
        flow_dots = VGroup(*[
            Dot(source.get_right(), radius=0.055, color=source[0].get_stroke_color())
            for source in sources
        ])
        flow_paths = [
            Line(source.get_right(), training.get_left() + UP * (0.45 - index * 0.3))
            for index, source in enumerate(sources)
        ]
        source_pulses = VGroup(*[
            SurroundingRectangle(source, color=source[0].get_stroke_color(), buff=0.08, corner_radius=0.05, stroke_width=2)
            for source in sources
        ])

        insight = create_insight_box(
            "Dataset thường là hỗn hợp nhiều nguồn sinh dữ liệu.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.7)

        self.play(LaggedStart(*[FadeIn(source, shift=RIGHT * 0.15) for source in sources], lag_ratio=0.15), run_time=TIME_NORMAL, rate_func=smooth)
        self.play(
            LaggedStart(*[ShowPassingFlash(pulse, time_width=0.55) for pulse in source_pulses], lag_ratio=0.1),
            run_time=1.2,
        )
        play_voiceover_and_wait(self, 9, 0)
        self.wait(12.0)
        self.play(FadeIn(training), Write(training_label), run_time=TIME_NORMAL)
        self.wait(10.0)
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.12), run_time=TIME_NORMAL)
        self.play(
            LaggedStart(
                *[MoveAlongPath(dot, path) for dot, path in zip(flow_dots, flow_paths)],
                lag_ratio=0.12,
            ),
            run_time=2.0,
            rate_func=smooth,
        )
        self.play(
            LaggedStart(*[TransformFromCopy(flow_dot, dots[index * 5]) for index, flow_dot in enumerate(flow_dots)], lag_ratio=0.12),
            run_time=1.0,
        )
        self.remove(flow_dots)
        play_voiceover_and_wait(self, 9, 1)
        self.wait(10.0)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.4) for dot in dots], lag_ratio=0.02), Write(mixture_label), run_time=TIME_NORMAL)
        self.wait(16.0)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 9, 2)
        self.wait(10.0)

        fade_out_all(self)
