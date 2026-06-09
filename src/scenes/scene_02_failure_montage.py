"""Scene 02: Failure montage."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *


TARGET_DURATION_SECONDS = 70


class FailureMontageScene(Scene):
    def make_card(self, title, icon, color):
        frame = RoundedRectangle(
            width=2.8,
            height=2.0,
            corner_radius=0.08,
            stroke_color=color,
            fill_color=BG_DARK,
            fill_opacity=0.0,
        )
        heading = Text(title, font_size=SIZE_SMALL, color=TEXT_PRIMARY, font=FONT_PRIMARY)
        heading.next_to(frame.get_top(), DOWN, buff=0.22)
        icon.move_to(frame.get_center() + DOWN * 0.15)
        return VGroup(frame, heading, icon)

    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Montage lỗi", "Những lỗi khác nhau, cùng một dấu hiệu")

        robot = VGroup(
            Circle(radius=0.26, color=THEME_BLUE, fill_opacity=0.35),
            VGroup(*[Line(LEFT * 0.5 + UP * y, RIGHT * 0.5 + UP * y, color=TEXT_MUTED) for y in (-0.35, 0, 0.35)]),
            Text("robot", font_size=18, color=THEME_BLUE, font=FONT_PRIMARY).shift(DOWN * 0.6),
        )
        camera = VGroup(
            Rectangle(width=0.9, height=0.55, color=THEME_AMBER),
            Circle(radius=0.13, color=THEME_AMBER).shift(RIGHT * 0.15),
            Dot(LEFT * 0.35 + DOWN * 0.25, color=THEME_RED),
            Text("camera", font_size=18, color=THEME_AMBER, font=FONT_PRIMARY).shift(DOWN * 0.65),
        )
        hospital = VGroup(
            RoundedRectangle(width=0.9, height=0.75, corner_radius=0.04, color=THEME_EMERALD),
            Text("+", font_size=36, color=THEME_EMERALD, font=FONT_PRIMARY),
            Text("hospital", font_size=18, color=THEME_EMERALD, font=FONT_PRIMARY).shift(DOWN * 0.68),
        )
        car = VGroup(
            Rectangle(width=0.95, height=0.35, color=THEME_PURPLE),
            Circle(radius=0.1, color=THEME_PURPLE).shift(LEFT * 0.32 + DOWN * 0.24),
            Circle(radius=0.1, color=THEME_PURPLE).shift(RIGHT * 0.32 + DOWN * 0.24),
            Triangle(color=THEME_RED).scale(0.22).shift(RIGHT * 0.95),
            Text("car", font_size=18, color=THEME_PURPLE, font=FONT_PRIMARY).shift(DOWN * 0.68),
        )

        cards = VGroup(
            self.make_card("Robot mắc kẹt", robot, THEME_BLUE),
            self.make_card("Tracking sai", camera, THEME_AMBER),
            self.make_card("Shortcut y tế", hospital, THEME_EMERALD),
            self.make_card("Phanh nhầm", car, THEME_PURPLE),
        ).arrange_in_grid(rows=2, cols=2, buff=0.45)

        question = Text(
            "Điều gì đã đổi?",
            font_size=SIZE_SECTION,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
        ).move_to(DOWN * 1.25)
        answer = create_insight_box(
            "Dữ liệu deployment không còn giống dữ liệu train",
            color=THEME_AMBER,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.7)

        self.play(LaggedStart(*[FadeIn(card, scale=0.92) for card in cards], lag_ratio=0.18), run_time=TIME_SLOW)
        self.play(
            LaggedStart(
                *[Flash(card[2], color=card[0].get_stroke_color(), flash_radius=0.55) for card in cards],
                lag_ratio=0.22,
            ),
            run_time=2.0,
        )
        self.play(
            LaggedStart(*[Indicate(card[0], color=card[0].get_stroke_color()) for card in cards], lag_ratio=0.18),
            run_time=2.0,
        )
        self.wait(12.0)
        self.play(cards.animate.scale(0.78).to_edge(UP, buff=0.75), run_time=TIME_NORMAL)
        self.wait(12.0)
        self.play(Write(question), run_time=TIME_NORMAL)
        self.wait(18.0)
        self.play(FadeIn(answer, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(15.0)

        fade_out_all(self)
