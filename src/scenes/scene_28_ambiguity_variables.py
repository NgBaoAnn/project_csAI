"""
Scene 28: Ambiguity Set Theo Biến
Author: TV3 (Animation Lead)
Duration: ~70 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


class AmbiguityVariablesScene(Scene):
    def make_switch(self, label, active=False):
        box = RoundedRectangle(width=2.5, height=0.6, corner_radius=0.05, stroke_color=THEME_EMERALD if active else TEXT_MUTED, stroke_width=1.5)
        text = Text(label, font_size=SIZE_CAPTION, color=THEME_EMERALD if active else TEXT_SECONDARY, font=FONT_PRIMARY)
        indicator = Circle(radius=0.08, color=THEME_EMERALD if active else TEXT_MUTED, fill_color=THEME_EMERALD if active else TEXT_MUTED, fill_opacity=1.0).next_to(text, LEFT, buff=0.15)
        switch = VGroup(box, text, indicator)
        return switch

    def construct(self):
        setup_dark_scene(self)

        # 1. Creative Intro: Variable-bound Ellipse
        set_ellipse = Ellipse(width=3.2, height=1.6, color=THEME_BLUE, stroke_width=3, fill_color=THEME_BLUE, fill_opacity=0.15).move_to(UP * 0.5)

        # Text variables scattered outside
        var_age = Text("Age", font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY).move_to(LEFT * 4.0 + UP * 1.5)
        var_edu = Text("Education", font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY).move_to(RIGHT * 3.5 + UP * 1.0)
        var_occ = Text("Occupation", font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY).move_to(DOWN * 1.5 + LEFT * 2.0)

        title_text = Text("Ambiguity Set Theo Biến", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(UP * 2.2)
        subtitle_text = Text("Ràng buộc độ robust vào thực tế", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(title_text, DOWN, buff=0.25)

        # Animate
        self.play(Create(set_ellipse), run_time=1.0)
        self.play(FadeIn(var_age), FadeIn(var_edu), FadeIn(var_occ), run_time=0.8)
        self.wait(0.2)

        # Snap variables to the border of the ellipse, changing its color to emerald with a glow
        glow_ellipse = create_3b1b_glow(set_ellipse, color=THEME_EMERALD, n_layers=4, opacity=0.15)
        self.play(
            var_age.animate.move_to(set_ellipse.get_center() + LEFT * 2.2 + UP * 0.5).set_color(THEME_EMERALD),
            var_edu.animate.move_to(set_ellipse.get_center() + RIGHT * 2.5 + UP * 0.2).set_color(THEME_EMERALD),
            var_occ.animate.move_to(set_ellipse.get_center() + DOWN * 1.25 + RIGHT * 0.2).set_color(THEME_EMERALD),
            set_ellipse.animate.set_color(THEME_EMERALD),
            FadeIn(glow_ellipse),
            Write(title_text),
            FadeIn(subtitle_text, shift=UP * 0.1),
            run_time=1.8
        )

        # seg 0: Title introduction
        play_voiceover_and_wait(self, 28, 0)

        # Clean up
        self.play(
            FadeOut(var_age), FadeOut(var_edu), FadeOut(var_occ),
            FadeOut(set_ellipse), FadeOut(glow_ellipse),
            FadeOut(title_text), FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        self.wait(0.5)

        # Subtitle 1
        sub1 = create_subtitle("Thay vì chọn ambiguity set trừu tượng, ta có thể chọn theo các biến có subgroup differences lớn.")
        self.play(FadeIn(sub1))
        # seg 1: "DRO nên robust trên biến nào..."
        play_voiceover_and_wait(self, 28, 1)

        # 2. Draw Feature Selector Dashboard (Left)
        dash_box = RoundedRectangle(width=3.6, height=3.6, corner_radius=0.1, stroke_color=TEXT_MUTED, stroke_width=1.5)
        dash_title = Text("Biến số (Variables)", font_size=SIZE_CAPTION, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=BOLD).move_to(dash_box.get_top() + DOWN * 0.35)

        s_age = self.make_switch("Age", active=False).move_to(dash_box.get_center() + UP * 0.6)
        s_edu = self.make_switch("Education", active=False).move_to(dash_box.get_center() + UP * 0.0)
        s_occ = self.make_switch("Occupation", active=False).move_to(dash_box.get_center() + DOWN * 0.6)

        dashboard = VGroup(dash_box, dash_title, s_age, s_edu, s_occ).shift(LEFT * 3.5 + UP * 0.8)
        self.play(FadeIn(dashboard, shift=RIGHT * 0.2))

        # 3. Draw Ambiguity Set (Right)
        # Represents the mathematical set U
        set_title = Text("Ambiguity Set U", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).shift(RIGHT * 3.5 + UP * 2.3)
        axes = Axes(x_range=[-2, 2, 1], y_range=[-2, 2, 1], x_length=3.0, y_length=3.0, axis_config={"color": TEXT_MUTED}).shift(RIGHT * 3.5 + UP * 0.5)

        ambiguity_set = Circle(radius=0.6, color=THEME_BLUE, stroke_width=2, fill_color=THEME_BLUE, fill_opacity=0.2).move_to(axes.c2p(0, 0, 0))
        set_group = VGroup(set_title, axes, ambiguity_set)

        self.play(FadeIn(set_group, shift=LEFT * 0.2))
        # seg 2: "Dashboard liệt kê biến... ambiguity set ban đầu hình tròn..."
        play_voiceover_and_wait(self, 28, 2)

        # Animate Toggling "Age" on
        s_age_active = self.make_switch("Age", active=True).move_to(s_age)

        # Ambiguity set changes shape (becomes elongated ellipse, representing focused constraint)
        focused_set = Ellipse(width=1.8, height=0.6, color=THEME_EMERALD, stroke_width=3, fill_color=THEME_EMERALD, fill_opacity=0.3).move_to(axes.c2p(0, 0, 0))

        self.play(
            Transform(s_age, s_age_active),
            Transform(ambiguity_set, focused_set),
            run_time=TIME_NORMAL
        )
        # seg 3: "Khi bật biến Age, ambiguity set thành ellipse nằm ngang..."
        play_voiceover_and_wait(self, 28, 3)

        # Subtitle 2
        sub2 = create_subtitle("Ràng buộc độ robust vào đúng các biến dịch chuyển giúp tối ưu hóa worst-group performance.")
        self.play(Transform(sub1, sub2))
        # seg 4: "Ràng buộc robustness vào đúng biến dịch chuyển..."
        play_voiceover_and_wait(self, 28, 4)

        # 4. Draw Performance Bar Chart (Bottom)
        # Show comparison: Without constraint vs With constraint
        top_group = VGroup(dashboard, set_group)
        self.play(top_group.animate.scale(0.78).to_edge(UP, buff=0.85), run_time=TIME_NORMAL)

        chart = BarChart(
            values=[55, 82],
            bar_names=["Trừu tượng", "Ràng buộc theo biến"],
            bar_colors=[THEME_BLUE, THEME_EMERALD],
            y_range=[0, 100, 25],
            y_length=1.8,
            x_length=4.8,
            y_axis_config={"font_size": 16},
            x_axis_config={"font_size": 16, "label_constructor": Text}
        ).shift(DOWN * 1.15)

        chart_label = Text("Worst-Group Accuracy", font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(chart, UP, buff=0.15)

        self.play(FadeIn(chart, shift=UP * 0.2), Write(chart_label), run_time=TIME_NORMAL)
        # seg 5: "Bar chart so sánh 55 phần trăm vs 82 phần trăm..."
        play_voiceover_and_wait(self, 28, 5)

        # Takeaway
        insight = create_insight_box(
            "Robustness phải được gắn với các biến số dịch chuyển.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.7)

        self.play(
            FadeOut(sub1),
            FadeOut(chart),
            FadeOut(chart_label),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL,
        )
        # seg 6: "Robustness phải được gắn với biến số dịch chuyển..."
        play_voiceover_and_wait(self, 28, 6)

        # Outro
        self.play(
            FadeOut(insight), FadeOut(dashboard),
            FadeOut(set_group),
            run_time=TIME_NORMAL
        )
        self.wait(1.0)
