"""Voiceover-ready Manim scene template.

Copy this file to create scenes 1-20 with synchronized voiceover.

Usage:
    1. Rename the file to e.g. scene_01_accuracy_fail.py.
    2. Update class name and scene title.
    3. Replace the placeholder animation blocks with your scene content.
    4. Add play_voiceover_and_wait(self, <scene_num>, <segment_idx>) at the audio cue points.

Voice sync pipeline:
    - The scene writes timings to output/audio/scene_XX/timings.txt
    - generate_voiceover.py reads timings.txt and aligns MP3 segments to the rendered video

Requirements:
    - Keep `output/audio/scene_XX/seg_YY_*.mp3` structure
    - Use segment indices starting from 0
    - Keep animation durations consistent with narration timing
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


TARGET_DURATION_SECONDS = 80


class Scene01AccuracyFail(Scene):
    """Scene 01: Accuracy cao nhưng fail ngoài đời."""

    def construct(self):
        setup_dark_scene(self)

        # --- Title / intro block ---
        eyebrow = Text(
            "OUT-OF-DISTRIBUTION GENERALIZATION",
            font_size=SIZE_SMALL,
            color=THEME_BLUE_LIGHT,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        ).to_edge(UP, buff=0.75)

        title = Text(
            "99.1%",
            font_size=128,
            color=TEXT_PRIMARY,
            font=FONT_PRIMARY,
            weight=BOLD,
        )
        title_glow = create_3b1b_glow(title, color=THEME_EMERALD, n_layers=5, opacity=0.22)
        underline = create_chalk_underline(title, color=THEME_AMBER, buff=0.04)
        metric = VGroup(title_glow, title, underline).move_to(UP * 0.38)

        label = Text(
            "Test accuracy",
            font_size=SIZE_BODY,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        ).next_to(metric, DOWN, buff=0.18)

        self.play(
            FadeIn(eyebrow, shift=DOWN * 0.15),
            FadeIn(title_glow, scale=1.05),
            Write(title),
            run_time=2.5,
        )
        self.play(Create(underline), FadeIn(label, shift=UP * 0.12), run_time=1.5)
        self.wait(0.5)

        # --- Voice segment 0: title intro ---
        play_voiceover_and_wait(self, 1, 0)

        # --- Main visual block ---
        dashboard = self.create_dashboard()
        dashboard.to_edge(LEFT, buff=0.7).shift(DOWN * 0.1)
        dashboard_arrow = Arrow(
            dashboard.get_right() + RIGHT * 0.25,
            RIGHT * 1.5,
            color=THEME_BLUE,
            stroke_width=4,
            buff=0.2,
        )

        self.play(FadeIn(dashboard, shift=RIGHT * 0.25), Create(dashboard_arrow), run_time=2.0)
        self.wait(0.5)

        # --- Voice segment 1: visual explanation ---
        play_voiceover_and_wait(self, 1, 1)

        # --- Finish block ---
        question = Text(
            "Nếu 99.1% là đúng, vậy nó đang đúng ở đâu?",
            font_size=SIZE_SECTION,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        ).move_to(ORIGIN)
        question_underline = create_chalk_underline(question, color=THEME_AMBER, buff=0.08)

        self.play(FadeOut(dashboard), FadeOut(dashboard_arrow), Write(question), Create(question_underline), run_time=2.5)
        self.wait(0.5)

        # --- Voice segment 2: closing question ---
        play_voiceover_and_wait(self, 1, 2)

        self.wait(1.5)

    def create_dashboard(self):
        """Example helper; replace with your own visual construction."""
        dashboard = VGroup(
            Rectangle(width=4.0, height=2.3, color=THEME_BLUE, fill_color=THEME_BLUE, fill_opacity=0.12, stroke_width=2),
            Text("Dashboard đẹp", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY)
        ).arrange(DOWN, buff=0.3)
        return dashboard
