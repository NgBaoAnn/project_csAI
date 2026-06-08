"""Scene 12: Pipeline View.
Author: TV2  |  Duration: ~70 giây
Câu hỏi: OOD generalization cần được tích hợp vào từng bước nào?
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from manim import *
from utils.theme import *
from utils.components import *

TARGET_DURATION_SECONDS = 70

STAGE_DATA = [
    ("Thu thập",    THEME_BLUE,   "Có nhóm ẩn\nkhông?"),
    ("Training",    THEME_EMERALD,"Học môi trường\nhay chỉ trung bình?"),
    ("Đánh giá",    THEME_AMBER,  "Đo ổn định\nvà nhóm lỗi"),
    ("Deployment",  THEME_RED,    "Shift nào làm\nhiệu năng giảm?"),
]


class PipelineViewScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        animate_title_card(self, "Pipeline OOD",
                           "OOD generalization là cả một quy trình")

        header = Text("Pipeline ML nhìn được heterogeneity",
                      font_size=SIZE_BODY, color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=MEDIUM
                      ).to_edge(UP, buff=0.65)
        self.play(Write(header), run_time=0.9)
        self.wait(6.0)

        # ── Build stage boxes ────────────────────────────────────────────
        boxes, labels, q_texts, glows = [], [], [], []
        for name, color, question in STAGE_DATA:
            box = RoundedRectangle(
                width=2.55, height=1.05, corner_radius=0.1,
                stroke_color=color, fill_color=BG_DARK, fill_opacity=0.0, stroke_width=2.2,
            )
            lbl = Text(name, font_size=SIZE_BODY, color=color, font=FONT_PRIMARY, weight=BOLD)
            q = Text(question, font_size=14, color=TEXT_SECONDARY, font=FONT_PRIMARY, line_spacing=0.85)
            glow = create_3b1b_glow(box, color=color, n_layers=3, opacity=0.12)
            boxes.append(box); labels.append(lbl); q_texts.append(q); glows.append(glow)

        stage_groups = VGroup(*[
            VGroup(boxes[i], labels[i]).arrange(ORIGIN) for i in range(4)
        ]).arrange(RIGHT, buff=1.1).shift(UP * 0.35)
        for i, sg in enumerate(stage_groups):
            labels[i].move_to(sg.get_center())
            q_texts[i].next_to(sg, DOWN, buff=0.35)

        # Arrows
        arrows = VGroup(*[
            Arrow(stage_groups[i].get_right() + RIGHT * 0.06,
                  stage_groups[i+1].get_left() + LEFT * 0.06,
                  color=TEXT_MUTED, buff=0.08, stroke_width=2.0,
                  tip_length=0.14, max_tip_length_to_length_ratio=0.4)
            for i in range(3)
        ])

        # Animate stages one by one
        for i in range(4):
            anims = [DrawBorderThenFill(boxes[i]), FadeIn(glows[i]), Write(labels[i])]
            if i > 0:
                anims.append(GrowArrow(arrows[i-1]))
            self.play(*anims, run_time=0.9)
            self.play(FadeIn(q_texts[i], shift=UP * 0.1), run_time=0.6)
            self.play(Circumscribe(stage_groups[i], color=STAGE_DATA[i][1], time_width=0.45), run_time=0.5)
            self.wait(6.0)

        self.wait(4.0)

        # ── Signature effect: particle đi qua pipeline ───────────────────
        particle = Dot(radius=0.10, color=THEME_BLUE_LIGHT)
        particle.move_to(stage_groups[0].get_center())
        self.play(FadeIn(particle, scale=0.3), run_time=0.4)
        for i in range(3):
            seg = Line(stage_groups[i].get_center(), stage_groups[i+1].get_center())
            self.play(
                MoveAlongPath(particle, seg),
                particle.animate.set_color(STAGE_DATA[i+1][1]),
                run_time=0.6, rate_func=smooth,
            )
        self.play(Flash(particle, color=THEME_AMBER, flash_radius=0.4, line_length=0.15), run_time=0.4)
        self.play(FadeOut(particle), run_time=0.3)

        # ShowPassingFlash trên toàn pipeline arrows
        self.play(
            LaggedStart(*[
                ShowPassingFlash(a.copy().set_stroke(THEME_BLUE_LIGHT, width=5), time_width=0.5)
                for a in arrows
            ], lag_ratio=0.3),
            run_time=1.5,
        )
        self.wait(5.0)

        # ── Insight ───────────────────────────────────────────────────────
        insight = create_insight_box(
            "OOD generalization là cả một quy trình, không chỉ là một thuật toán.",
            color=THEME_BLUE, font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.72)
        self.play(FadeIn(insight, shift=UP * 0.2), run_time=1.0)
        self.wait(13.0)
        fade_out_all(self)
