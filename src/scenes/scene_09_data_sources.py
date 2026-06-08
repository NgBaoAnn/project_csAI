"""Scene 09: Data đến từ nhiều sources."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class DataSourcesScene(Scene):
    def source_box(self, name, color):
        box = RoundedRectangle(
            width=2.1,
            height=0.85,
            corner_radius=0.07,
            stroke_color=color,
            fill_color=BG_DARKER,
            fill_opacity=0.86,
        )
        label = Text(name, font_size=SIZE_CAPTION, color=color, font=FONT_PRIMARY)
        return VGroup(box, label)

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Multiple Sources", "Training data là một mixture")

        sources = VGroup(
            self.source_box("Source A", THEME_BLUE),
            self.source_box("Source B", THEME_AMBER),
            self.source_box("Source C", THEME_EMERALD),
            self.source_box("Source D", THEME_PURPLE),
        ).arrange(DOWN, buff=0.28).to_edge(LEFT, buff=0.9)

        training = RoundedRectangle(
            width=3.6,
            height=2.4,
            corner_radius=0.08,
            stroke_color=TEXT_PRIMARY,
            fill_color=BG_DARKER,
            fill_opacity=0.9,
        ).shift(RIGHT * 2.2)
        training_label = Text("Training data", font_size=SIZE_BODY, color=TEXT_PRIMARY, font=FONT_PRIMARY).move_to(training.get_top() + DOWN * 0.5)
        mixture_label = Text("mixture", font_size=SIZE_CAPTION, color=THEME_AMBER, font=FONT_PRIMARY).move_to(training.get_bottom() + UP * 0.45)

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

        insight = create_insight_box(
            "A dataset is often a mixture of data-generating sources",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.7)

        self.play(LaggedStart(*[FadeIn(source, shift=RIGHT * 0.15) for source in sources], lag_ratio=0.15), run_time=TIME_NORMAL)
        self.play(FadeIn(training), Write(training_label), run_time=TIME_NORMAL)
        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in arrows], lag_ratio=0.12), run_time=TIME_NORMAL)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.4) for dot in dots], lag_ratio=0.02), Write(mixture_label), run_time=TIME_NORMAL)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
