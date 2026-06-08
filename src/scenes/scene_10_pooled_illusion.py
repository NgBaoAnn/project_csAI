"""Scene 10: Pooled dataset illusion."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class PooledIllusionScene(Scene):
    def cluster(self, center, color):
        offsets = [(-0.4, -0.1), (-0.22, 0.23), (0.05, -0.22), (0.25, 0.15), (0.42, -0.05), (-0.08, 0.42)]
        return VGroup(*[
            Dot([center[0] + x, center[1] + y, 0], radius=0.055, color=color)
            for x, y in offsets
        ])

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Pooled Dataset Illusion", "Một màu xám che giấu nhiều environments")

        gray_centers = [(-2.0, 0.35), (-1.35, -0.25), (-0.75, 0.25), (-0.15, -0.3), (0.45, 0.28), (1.05, -0.15), (1.65, 0.3)]
        pooled_points = VGroup(*[
            Dot([x, y, 0], radius=0.055, color=TEXT_MUTED)
            for x, y in gray_centers
            for _ in range(2)
        ])
        pooled_title = Text("pooled dataset", font_size=SIZE_SECTION, color=TEXT_PRIMARY, font=FONT_PRIMARY).to_edge(UP, buff=0.7)
        pooled_note = Text("mọi sample nhìn như cùng một khối", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(pooled_title, DOWN)

        lens = Circle(radius=1.25, color=THEME_AMBER, stroke_width=4).shift(RIGHT * 0.2 + DOWN * 0.05)
        handle = Line(lens.get_corner(DR), lens.get_corner(DR) + DOWN * 0.85 + RIGHT * 0.85, color=THEME_AMBER, stroke_width=5)

        cluster_a = self.cluster((-2.25, -0.15), THEME_BLUE)
        cluster_b = self.cluster((0.0, 0.45), THEME_EMERALD)
        cluster_c = self.cluster((2.2, -0.25), THEME_PURPLE)
        colored_clusters = VGroup(cluster_a, cluster_b, cluster_c)
        labels = VGroup(
            Text("Hospital A", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY).next_to(cluster_a, DOWN),
            Text("Hospital B", font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(cluster_b, DOWN),
            Text("Hospital C", font_size=SIZE_CAPTION, color=THEME_PURPLE, font=FONT_PRIMARY).next_to(cluster_c, DOWN),
        )

        insight = create_insight_box(
            "colored clusters reveal hidden environments",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.65)

        self.play(Write(pooled_title), FadeIn(pooled_note), run_time=TIME_NORMAL)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.4) for dot in pooled_points], lag_ratio=0.025), run_time=TIME_NORMAL)
        self.play(Create(lens), Create(handle), run_time=TIME_NORMAL)
        self.play(
            FadeOut(pooled_points),
            FadeOut(pooled_note),
            FadeIn(colored_clusters, scale=0.95),
            FadeIn(labels, shift=UP * 0.1),
            run_time=TIME_SLOW,
        )
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
