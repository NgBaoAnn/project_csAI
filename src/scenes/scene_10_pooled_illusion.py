"""Scene 10: Pooled dataset illusion."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


TARGET_DURATION_SECONDS = 75


class PooledIllusionScene(Scene):
    def cluster(self, center, color):
        offsets = [(-0.4, -0.1), (-0.22, 0.23), (0.05, -0.22), (0.25, 0.15), (0.42, -0.05), (-0.08, 0.42)]
        return VGroup(*[
            Dot([center[0] + x, center[1] + y, 0], radius=0.055, color=color)
            for x, y in offsets
        ])

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Ảo giác dataset gộp", "Một màu xám che giấu nhiều environments")

        gray_centers = [(-2.0, 0.35), (-1.35, -0.25), (-0.75, 0.25), (-0.15, -0.3), (0.45, 0.28), (1.05, -0.15), (1.65, 0.3)]
        pooled_points = VGroup(*[
            Dot([x, y, 0], radius=0.055, color=TEXT_MUTED)
            for x, y in gray_centers
            for _ in range(2)
        ])
        pooled_title = Text("dataset gộp", font_size=SIZE_SECTION, color=TEXT_PRIMARY, font=FONT_PRIMARY).to_edge(UP, buff=0.7)
        pooled_note = Text("mọi sample nhìn như cùng một khối", font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(pooled_title, DOWN)

        lens = Circle(radius=1.25, color=THEME_AMBER, stroke_width=4).shift(RIGHT * 0.2 + DOWN * 0.05)
        handle = Line(lens.get_corner(DR), lens.get_corner(DR) + DOWN * 0.85 + RIGHT * 0.85, color=THEME_AMBER, stroke_width=5)
        lens_group = VGroup(lens, handle)
        scan_path = Line(LEFT * 2.2 + DOWN * 0.05, RIGHT * 1.2 + DOWN * 0.05)
        reveal_wedge = AnnularSector(
            inner_radius=1.08,
            outer_radius=1.25,
            angle=TAU * 0.72,
            start_angle=PI * 0.08,
            color=THEME_AMBER,
            fill_opacity=0.12,
            stroke_opacity=0,
        ).move_to(lens)

        cluster_a = self.cluster((-2.25, -0.15), THEME_BLUE)
        cluster_b = self.cluster((0.0, 0.45), THEME_EMERALD)
        cluster_c = self.cluster((2.2, -0.25), THEME_PURPLE)
        colored_clusters = VGroup(cluster_a, cluster_b, cluster_c)
        labels = VGroup(
            Text("Bệnh viện A", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY).next_to(cluster_a, DOWN),
            Text("Bệnh viện B", font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(cluster_b, DOWN),
            Text("Bệnh viện C", font_size=SIZE_CAPTION, color=THEME_PURPLE, font=FONT_PRIMARY).next_to(cluster_c, DOWN),
        )

        insight = create_insight_box(
            "Các cụm màu làm lộ environment ẩn.",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.65)

        self.play(Write(pooled_title), FadeIn(pooled_note), run_time=TIME_NORMAL, rate_func=smooth)
        play_voiceover_and_wait(self, 10, 0)
        self.wait(11.0)
        self.play(LaggedStart(*[FadeIn(dot, scale=0.4) for dot in pooled_points], lag_ratio=0.025), run_time=TIME_NORMAL)
        self.wait(14.0)
        self.play(Create(lens), Create(handle), FadeIn(reveal_wedge, scale=0.9), run_time=TIME_NORMAL)
        self.play(MoveAlongPath(lens_group, scan_path), MoveAlongPath(reveal_wedge, scan_path), run_time=3.0, rate_func=smooth)
        play_voiceover_and_wait(self, 10, 1)
        self.wait(9.0)
        self.play(
            Transform(pooled_points, colored_clusters.copy()),
            FadeOut(pooled_note),
            FadeOut(reveal_wedge),
            FadeIn(colored_clusters, scale=0.95),
            FadeIn(labels, shift=UP * 0.1),
            run_time=TIME_SLOW,
            rate_func=smooth,
        )
        self.wait(18.0)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        play_voiceover_and_wait(self, 10, 2)
        self.wait(10.0)

        fade_out_all(self)
