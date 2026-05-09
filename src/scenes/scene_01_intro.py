"""
Scene 01: Intro — Hook & Giới thiệu vấn đề
Phụ trách: TV1 (Team Lead)
Thời lượng: ~1.5 phút

Nội dung:
- Title card dự án
- Hook: "Tại sao AI thất bại trong thực tế?"
- Lead vào nội dung chính
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


class IntroScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # === Title Card ===
        title = Text(
            "Data Heterogeneity",
            font_size=SIZE_TITLE,
            color=TEXT_PRIMARY,
            font=FONT_PRIMARY,
        )
        subtitle = Text(
            "& Out-of-Distribution Generalization",
            font_size=SIZE_SUBSECTION,
            color=THEME_BLUE,
            font=FONT_PRIMARY,
        )
        tagline = Text(
            "Tại sao AI thông minh nhưng vẫn sai?",
            font_size=SIZE_BODY,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
        )

        title_group = VGroup(title, subtitle, tagline).arrange(DOWN, buff=0.5)

        # Animate title
        self.play(FadeIn(title, shift=UP * 0.3), run_time=TIME_SLOW)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)
        self.play(FadeIn(tagline, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        # Fade out title
        self.play(FadeOut(title_group), run_time=TIME_NORMAL)
        self.wait(TIME_FAST)

        # === Hook: Question ===
        question = Text(
            "99% accuracy trong lab...\nnhưng thất bại ngoài thực tế?",
            font_size=SIZE_SUBSECTION,
            color=TEXT_PRIMARY,
            font=FONT_PRIMARY,
            line_spacing=1.5,
        )
        question_mark = Text(
            "?",
            font_size=120,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
        )
        question_mark.next_to(question, RIGHT, buff=0.5)

        self.play(Write(question), run_time=TIME_SLOW)
        self.play(
            FadeIn(question_mark, scale=0.5),
            Flash(question_mark, color=THEME_AMBER, flash_radius=1.5),
            run_time=TIME_NORMAL,
        )
        self.wait(TIME_LONG_PAUSE)

        # === Transition ===
        insight = create_insight_box(
            "Câu trả lời nằm ở DATA HETEROGENEITY",
            color=THEME_EMERALD,
        )
        self.play(
            FadeOut(question),
            FadeOut(question_mark),
            run_time=TIME_FAST,
        )
        self.play(FadeIn(insight, shift=UP * 0.3), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        fade_out_all(self)
