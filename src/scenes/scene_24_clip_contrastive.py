"""
Scene 24: CLIP Contrastive Learning
Author: TV3 (Animation Lead)
Duration: ~75 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from manim import *
from utils.theme import *
from utils.components import *
from utils.voice_sync import play_voiceover_and_wait


class CLIPContrastiveScene(Scene):
    def construct(self):
        setup_dark_scene(self)

        # ── 1. Intro: Collision of Image & Text ──────────────────────────────
        lbl_image = Text("Hình ảnh (Image)", font_size=SIZE_TITLE - 8,
                         color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD)
        lbl_image.shift(LEFT * 6 + UP * 0.5)
        lbl_text = Text("Văn bản (Text)", font_size=SIZE_TITLE - 8,
                        color=THEME_ORANGE, font=FONT_PRIMARY, weight=BOLD)
        lbl_text.shift(RIGHT * 6 + UP * 0.5)

        self.add(lbl_image, lbl_text)
        self.play(
            lbl_image.animate.move_to(LEFT * 0.9 + UP * 0.5),
            lbl_text.animate.move_to(RIGHT * 0.9 + UP * 0.5),
            run_time=1.0,
            rate_func=lambda t: t**3,
        )

        ripple = Circle(radius=0.1, color=THEME_PURPLE, stroke_width=4)
        ripple.move_to(UP * 0.5)
        self.add(ripple)

        title_text = Text("CLIP Contrastive Learning", font_size=SIZE_TITLE - 8,
                          color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD)
        title_text.move_to(UP * 0.5)
        subtitle_text = Text("Khai thác sức mạnh của mô hình lớn", font_size=SIZE_BODY - 4,
                             color=TEXT_SECONDARY, font=FONT_PRIMARY)
        subtitle_text.next_to(title_text, DOWN, buff=0.3)

        self.play(
            FadeOut(lbl_image),
            FadeOut(lbl_text),
            ripple.animate.scale(35).set_stroke(width=1, opacity=0),
            Write(title_text),
            FadeIn(subtitle_text, shift=UP * 0.1),
            run_time=1.5,
        )

        # seg 0: Title introduction
        play_voiceover_and_wait(self, 24, 0)

        self.play(
            FadeOut(title_text),
            FadeOut(subtitle_text),
            FadeOut(ripple),
            run_time=TIME_FAST,
        )
        self.wait(0.5)

        # ── 2. Subtitle 1 + Encoders ─────────────────────────────────────────
        sub1 = create_bottom_caption(
            "CLIP học từ các cặp ảnh và văn bản bằng phương pháp contrastive learning."
        )
        self.play(FadeIn(sub1))

        # seg 1: "CLIP học từ các cặp ảnh và văn bản..."
        play_voiceover_and_wait(self, 24, 2)

        # Image Encoder
        img_box = RoundedRectangle(width=3.2, height=2.2, corner_radius=0.08,
                                   stroke_color=THEME_BLUE, stroke_width=2)
        img_box.shift(LEFT * 4.5 + UP * 1.2)
        img_title = Text("Image Encoder", font_size=SIZE_CAPTION,
                        color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD)
        img_title.next_to(img_box, UP, buff=0.2)

        img_content = VGroup(
            Triangle(color=TEXT_MUTED).scale(0.35).move_to(img_box.get_center() + DOWN * 0.2 + LEFT * 0.3),
            Circle(radius=0.18, color=THEME_AMBER, fill_color=THEME_AMBER, fill_opacity=0.6)
            .move_to(img_box.get_center() + UP * 0.3 + RIGHT * 0.4)
        )
        image_encoder = VGroup(img_box, img_title, img_content)

        # Text Encoder
        txt_box = RoundedRectangle(width=3.2, height=2.2, corner_radius=0.08,
                                   stroke_color=THEME_ORANGE, stroke_width=2)
        txt_box.shift(RIGHT * 4.5 + UP * 1.2)
        txt_title = Text("Text Encoder", font_size=SIZE_CAPTION,
                        color=THEME_ORANGE, font=FONT_PRIMARY, weight=BOLD)
        txt_title.next_to(txt_box, UP, buff=0.2)
        txt_content = Text('"ảnh của một con chim"', font_size=SIZE_SMALL,
                           color=TEXT_PRIMARY, font=FONT_PRIMARY, slant=ITALIC)
        txt_content.move_to(txt_box.get_center())
        text_encoder = VGroup(txt_box, txt_title, txt_content)

        self.play(FadeIn(image_encoder), FadeIn(text_encoder), run_time=TIME_NORMAL)

        # seg 2: "Image encoder và text encoder độc lập..."
        play_voiceover_and_wait(self, 24, 3)

        # ── 3. Shared Embedding Space ────────────────────────────────────────
        space = Circle(radius=1.8, color=THEME_PURPLE, stroke_width=3,
                       fill_color=BG_PANEL, fill_opacity=0.45)
        space.shift(UP * 0.8)
        space_label = Text("Shared Embedding Space", font_size=SIZE_CAPTION,
                          color=THEME_PURPLE, font=FONT_PRIMARY, weight=BOLD)
        space_label.next_to(space, UP, buff=0.25)

        arrow_left = Arrow(img_box.get_right(), space.get_left(),
                          color=THEME_BLUE, stroke_width=3, buff=0.15)
        arrow_right = Arrow(txt_box.get_left(), space.get_right(),
                           color=THEME_ORANGE, stroke_width=3, buff=0.15)

        self.play(
            FadeIn(space), Write(space_label),
            Create(arrow_left), Create(arrow_right),
            run_time=TIME_NORMAL,
        )

        # seg 3: "Cả hai encoder cùng chiếu vào..."
        play_voiceover_and_wait(self, 24, 4)

        # ── 4. Subtitle 2 + Vectors ──────────────────────────────────────────
        sub2 = create_bottom_caption(
            "Cặp tương ứng kéo lại gần, cặp không khớp bị đẩy ra xa."
        )
        self.play(Transform(sub1, sub2))

        # Vectors inside embedding space
        vi = Dot(space.get_center() + LEFT * 0.8 + DOWN * 0.2,
                color=THEME_BLUE, radius=0.08)
        vt_correct = Dot(space.get_center() + LEFT * 0.3 + DOWN * 0.3,
                        color=THEME_ORANGE, radius=0.08)
        vi_label = MathTex(r"v_i", font_size=SIZE_SMALL, color=THEME_BLUE)
        vi_label.next_to(vi, UP, buff=0.15)
        vt_c_label = MathTex(r"v_t", font_size=SIZE_SMALL, color=THEME_ORANGE)
        vt_c_label.next_to(vt_correct, DOWN, buff=0.1)

        vt_incorrect = Dot(space.get_center() + RIGHT * 1.1 + UP * 0.6,
                          color=THEME_ORANGE, radius=0.08)
        vt_i_label = MathTex(r"v_{t'}", font_size=SIZE_SMALL, color=THEME_ORANGE)
        vt_i_label.next_to(vt_incorrect, DOWN, buff=0.15)

        self.play(
            FadeIn(vi), FadeIn(vt_correct), FadeIn(vi_label), FadeIn(vt_c_label),
            FadeIn(vt_incorrect), FadeIn(vt_i_label),
            run_time=TIME_NORMAL,
        )

        # seg 4: "Cặp ảnh-văn bản tương ứng..."
        play_voiceover_and_wait(self, 24, 5)

        # ── 5. Forces: Attract & Repel ───────────────────────────────────────
        attract = DoubleArrow(vi.get_center(), vt_correct.get_center(),
                             color=THEME_EMERALD, stroke_width=3, buff=0.15)
        repel1 = Arrow(vi.get_center(), space.get_center() + LEFT * 1.5 + DOWN * 0.1,
                      color=THEME_RED, stroke_width=2, buff=0.15)
        repel2 = Arrow(vt_incorrect.get_center(), space.get_center() + RIGHT * 1.6 + UP * 0.9,
                      color=THEME_RED, stroke_width=2, buff=0.15)

        self.play(Create(attract), run_time=TIME_NORMAL)
        self.play(Create(repel1), Create(repel2), run_time=TIME_NORMAL)

        # seg 5: "Mũi tên xanh lá kéo cặp đúng..."
        play_voiceover_and_wait(self, 24, 6)

        # ── 6. Formula: Cosine Similarity ────────────────────────────────────
        cosine_sim = MathTex(r"\text{Maximize } \cos(v_i, v_t)",
                            font_size=SIZE_FORMULA, color=THEME_EMERALD)
        cosine_sim.next_to(space, DOWN, buff=0.25)
        fit_to_width(cosine_sim, max_width=7.2)
        self.play(Write(cosine_sim), run_time=TIME_NORMAL)

        # seg 6: "Mục tiêu toán học: maximize cosine similarity..."
        play_voiceover_and_wait(self, 24, 7)

        # ── 7. Insight ───────────────────────────────────────────────────────
        insight = create_insight_box(
            "Pretraining trên dữ liệu lớn giúp học representations tổng quát.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION,
        ).to_edge(DOWN, buff=0.75)

        self.play(
            FadeOut(sub1),
            FadeIn(insight, shift=UP * 0.2),
            run_time=TIME_NORMAL,
        )

        # seg 7: "Pretraining trên dữ liệu đa dạng..."
        play_voiceover_and_wait(self, 24, 7)

        # ── Outro ────────────────────────────────────────────────────────────
        self.play(
            FadeOut(insight), FadeOut(image_encoder), FadeOut(text_encoder),
            FadeOut(space), FadeOut(space_label), FadeOut(arrow_left), FadeOut(arrow_right),
            FadeOut(vi), FadeOut(vt_correct), FadeOut(vi_label), FadeOut(vt_c_label),
            FadeOut(vt_incorrect), FadeOut(vt_i_label), FadeOut(attract),
            FadeOut(repel1), FadeOut(repel2), FadeOut(cosine_sim),
            run_time=TIME_NORMAL,
        )
        self.wait(1.0)
