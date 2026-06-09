"""Scene 01: Accuracy cao nhưng fail ngoài đời."""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from manim import *
from utils.theme import *
from utils.components import *


TARGET_DURATION_SECONDS = 80


class AccuracyFailScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        subtle_grid = self.create_subtle_grid()

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

        lab_mark = VGroup(
            Line(LEFT * 1.0, RIGHT * 1.0, color=THEME_EMERALD, stroke_width=3),
            Text(
                "KẾT QUẢ LAB",
                font_size=SIZE_SMALL,
                color=THEME_EMERALD,
                font=FONT_PRIMARY,
                weight=BOLD,
            ),
        ).arrange(DOWN, buff=0.12).move_to(label.get_center() + DOWN * 0.78)

        self.play(
            FadeIn(subtle_grid),
            FadeIn(eyebrow, shift=DOWN * 0.15),
            run_time=1.5,
        )
        self.play(FadeIn(title_glow, scale=1.05), Write(title), run_time=2.5, rate_func=smooth)
        self.play(
            Create(underline),
            FadeIn(label, shift=UP * 0.12),
            FadeIn(lab_mark, shift=UP * 0.12),
            run_time=1.5,
        )
        self.wait(6.0)

        dashboard = self.create_dashboard()
        dashboard.to_edge(LEFT, buff=0.7).shift(DOWN * 0.1)
        metric_target = metric.copy().scale(0.78).to_edge(RIGHT, buff=0.95).shift(UP * 0.55)
        label_target = label.copy().next_to(metric_target, DOWN, buff=0.1)
        lab_mark_target = lab_mark.copy().next_to(label_target, DOWN, buff=0.3)
        dashboard_arrow = Arrow(
            dashboard.get_right() + RIGHT * 0.25,
            metric_target.get_left() + LEFT * 0.2,
            color=THEME_BLUE,
            stroke_width=4,
            buff=0.2,
        )
        dashboard_note = Text(
            "Dashboard đẹp không có nghĩa là thế giới thật đứng yên.",
            font_size=SIZE_CAPTION,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=0.65)

        self.play(
            Transform(metric, metric_target),
            Transform(label, label_target),
            Transform(lab_mark, lab_mark_target),
            run_time=2.0,
            rate_func=smooth,
        )
        self.play(FadeIn(dashboard, shift=RIGHT * 0.25), Create(dashboard_arrow), run_time=2.0, rate_func=smooth)
        self.play(
            ShowPassingFlash(dashboard_arrow.copy().set_stroke(THEME_BLUE_LIGHT, width=7), time_width=0.45),
            run_time=0.8,
        )
        self.play(Write(dashboard_note), run_time=2.0)
        self.wait(6.7)

        question = Text(
            "Nếu 99.1% là đúng, vậy nó đang đúng ở đâu?",
            font_size=SIZE_SECTION,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        ).move_to(ORIGIN)
        question_underline = create_chalk_underline(question, color=THEME_AMBER, buff=0.08)

        self.play(
            FadeOut(dashboard),
            FadeOut(dashboard_arrow),
            FadeOut(dashboard_note),
            metric.animate.scale(0.72).to_edge(UP, buff=1.1),
            FadeOut(label),
            FadeOut(lab_mark),
            run_time=2.0,
        )
        self.play(Write(question), Create(question_underline), run_time=2.5, rate_func=smooth)
        self.wait(6.5)

        train_cloud = self.create_dot_cloud(LEFT * 3.2 + DOWN * 0.45, THEME_BLUE)
        test_cloud = self.create_dot_cloud(LEFT * 0.5 + DOWN * 0.45, THEME_EMERALD)
        deploy_cloud = self.create_dot_cloud(RIGHT * 3.1 + DOWN * 0.25, THEME_RED, stretched=True)
        cloud_labels = VGroup(
            Text("train", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY).next_to(train_cloud, DOWN),
            Text("test", font_size=SIZE_CAPTION, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(test_cloud, DOWN),
            Text("deploy", font_size=SIZE_CAPTION, color=THEME_RED, font=FONT_PRIMARY).next_to(deploy_cloud, DOWN),
        )
        assumption = MathTex(
            r"P_{\mathrm{train}}",
            r"\approx",
            r"P_{\mathrm{test}}",
            font_size=SIZE_SUBSECTION,
            color=TEXT_PRIMARY,
        ).to_edge(UP, buff=1.25)
        assumption[0].set_color(THEME_BLUE)
        assumption[2].set_color(THEME_EMERALD)
        broken_assumption = MathTex(
            r"P_{\mathrm{train}}",
            r"\neq",
            r"P_{\mathrm{deploy}}",
            font_size=SIZE_SUBSECTION,
            color=THEME_RED,
        ).move_to(assumption)
        broken_assumption[0].set_color(THEME_BLUE)
        broken_assumption[2].set_color(THEME_RED)
        assumption_caption = Text(
            "Validation chỉ kiểm tra một thế giới đã được giữ khá giống training.",
            font_size=SIZE_CAPTION,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=0.65)

        self.play(
            FadeOut(metric),
            FadeOut(question),
            FadeOut(question_underline),
            FadeIn(train_cloud),
            FadeIn(test_cloud),
            FadeIn(cloud_labels[:2]),
            Write(assumption),
            run_time=2.5,
        )
        self.play(Write(assumption_caption), run_time=2.0)
        self.wait(7.0)

        deploy_arrow = Arrow(
            test_cloud.get_right() + RIGHT * 0.25,
            deploy_cloud.get_left() + LEFT * 0.25,
            color=THEME_RED,
            stroke_width=4,
            buff=0.1,
        )
        deploy_caption = Text(
            "Ngoài đời: ánh sáng, camera, bệnh viện, người dùng, mùa vụ... đều có thể đổi.",
            font_size=SIZE_CAPTION,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
        ).to_edge(DOWN, buff=0.65)

        self.play(Create(deploy_arrow), FadeIn(deploy_cloud), FadeIn(cloud_labels[2]), run_time=2.0, rate_func=smooth)
        self.play(
            ShowPassingFlash(deploy_arrow.copy().set_stroke(THEME_RED_LIGHT, width=7), time_width=0.45),
            run_time=0.8,
        )
        self.play(
            Transform(assumption, broken_assumption),
            Transform(assumption_caption, deploy_caption),
            run_time=2.0,
        )
        self.wait(7.2)

        # A clean, natural zigzag crack that splits the number vertically
        crack_1 = Line(UP * 0.75 + LEFT * 0.1, UP * 0.2 + RIGHT * 0.05, color=THEME_RED, stroke_width=4.5)
        crack_2 = Line(UP * 0.2 + RIGHT * 0.05, DOWN * 0.25 + LEFT * 0.15, color=THEME_RED, stroke_width=4.5)
        crack_3 = Line(DOWN * 0.25 + LEFT * 0.15, DOWN * 0.75 + RIGHT * 0.1, color=THEME_RED, stroke_width=4.5)
        crack_4 = Line(UP * 0.1 + RIGHT * 0.02, UP * 0.45 + RIGHT * 0.35, color=THEME_RED, stroke_width=3.5)
        final_title = Text(
            "99.1%",
            font_size=128,
            color=TEXT_PRIMARY,
            font=FONT_PRIMARY,
            weight=BOLD,
        ).move_to(UP * 0.28)
        final_glow = create_3b1b_glow(final_title, color=THEME_EMERALD, n_layers=5, opacity=0.22)
        final_underline = create_chalk_underline(final_title, color=THEME_AMBER, buff=0.04)
        cracks = VGroup(crack_1, crack_2, crack_3, crack_4).move_to(final_title)
        hairline = Line(
            final_title.get_top() + DOWN * 0.15,
            final_title.get_bottom() + UP * 0.15,
            color=THEME_RED_LIGHT,
            stroke_width=2,
            stroke_opacity=0.55,
        ).move_to(final_title)

        target_mark = VGroup(
            Line(LEFT * 1.35, RIGHT * 1.35, color=THEME_RED, stroke_width=3),
            Text(
                "RỦI RO DEPLOYMENT",
                font_size=SIZE_SMALL,
                color=THEME_RED,
                font=FONT_PRIMARY,
                weight=BOLD,
            ),
        ).arrange(DOWN, buff=0.12).next_to(final_title, DOWN, buff=0.75)

        warning = create_insight_box(
            "Test accuracy cao chưa chắc đáng tin ngoài đời",
            color=THEME_RED,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.82)
        warning[0].set_stroke(opacity=0.85)
        warning[0].set_fill(BG_DARK, opacity=0.0)

        shift_line = Text(
            "Khi dữ liệu ngoài đời đổi, con số trong lab bắt đầu nứt.",
            font_size=SIZE_BODY,
            color=THEME_AMBER,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        ).next_to(final_title, UP, buff=0.45)

        self.play(
            FadeOut(train_cloud),
            FadeOut(test_cloud),
            FadeOut(deploy_cloud),
            FadeOut(cloud_labels),
            FadeOut(deploy_arrow),
            FadeOut(assumption),
            FadeOut(assumption_caption),
            FadeIn(final_glow),
            Write(final_title),
            Create(final_underline),
            run_time=2.5,
        )
        self.play(
            ShowPassingFlash(hairline, time_width=0.35),
            final_title.animate.scale(1.02),
            run_time=0.8,
            rate_func=there_and_back,
        )
        self.play(
            LaggedStart(*[Create(crack) for crack in cracks], lag_ratio=0.18),
            final_title.animate.set_color(THEME_RED),
            final_glow.animate.set_color(THEME_RED).set_opacity(0.22),
            final_underline.animate.set_color(THEME_RED),
            run_time=1.5,
            rate_func=rush_from,
        )
        self.play(Flash(final_title, color=THEME_RED_LIGHT, flash_radius=0.65, line_length=0.18), run_time=0.6)
        self.play(
            FadeIn(target_mark, shift=UP * 0.1),
            FadeIn(shift_line, shift=DOWN * 0.15),
            FadeIn(warning, shift=UP * 0.2),
            run_time=2.0,
        )
        self.wait(6.4)

        bridge = Text(
            "Vậy muốn tin model, ta phải hỏi dữ liệu đã khác nhau như thế nào.",
            font_size=SIZE_BODY,
            color=THEME_BLUE_LIGHT,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        ).to_edge(DOWN, buff=0.65)

        self.play(Transform(warning, bridge), FadeOut(target_mark), run_time=2.0)
        self.wait(4.0)

        fade_out_all(self)

    def create_subtle_grid(self):
        subtle_grid = VGroup()
        for x in [-6, -4, -2, 0, 2, 4, 6]:
            subtle_grid.add(
                Line(
                    [x, -3.6, 0],
                    [x, 3.6, 0],
                    color=GRID_COLOR,
                    stroke_opacity=0.1,
                    stroke_width=1,
                )
            )
        for y in [-3, -2, -1, 0, 1, 2, 3]:
            subtle_grid.add(
                Line(
                    [-7.0, y, 0],
                    [7.0, y, 0],
                    color=GRID_COLOR,
                    stroke_opacity=0.1,
                    stroke_width=1,
                )
            )
        return subtle_grid

    def create_dashboard(self):
        title = Text(
            "Dashboard đẹp",
            font_size=SIZE_BODY,
            color=TEXT_PRIMARY,
            font=FONT_PRIMARY,
            weight=BOLD,
        )
        rows = VGroup(
            self.create_dashboard_row("loss giảm đều", THEME_EMERALD),
            self.create_dashboard_row("validation ổn", THEME_EMERALD),
            self.create_dashboard_row("test accuracy cao", THEME_EMERALD),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        panel = VGroup(title, rows).arrange(DOWN, aligned_edge=LEFT, buff=0.35)
        box = SurroundingRectangle(
            panel,
            color=THEME_BLUE,
            buff=0.35,
            corner_radius=0.04,
            stroke_width=1.6,
        )
        return VGroup(box, panel)

    def create_dashboard_row(self, text, color):
        check = Text("✓", font_size=SIZE_CAPTION, color=color, font=FONT_PRIMARY, weight=BOLD)
        label = Text(text, font_size=SIZE_CAPTION, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        return VGroup(check, label).arrange(RIGHT, buff=0.18)

    def create_dot_cloud(self, center, color, stretched=False):
        offsets = [
            (-0.75, 0.12),
            (-0.45, 0.52),
            (-0.2, -0.28),
            (0.1, 0.18),
            (0.35, -0.46),
            (0.55, 0.42),
            (0.78, -0.02),
            (-0.05, 0.62),
            (-0.62, -0.42),
            (0.22, -0.02),
        ]
        dots = VGroup()
        for x, y in offsets:
            scale_x = 1.45 if stretched else 1.0
            scale_y = 0.75 if stretched else 1.0
            dots.add(Dot(center + RIGHT * x * scale_x + UP * y * scale_y, color=color, radius=0.07))
        ellipse = Ellipse(
            width=2.35 if stretched else 1.9,
            height=1.35,
            color=color,
            stroke_width=2,
            stroke_opacity=0.55,
        ).move_to(center)
        return VGroup(ellipse, dots)
