"""
Scene 09: Stable Learning & Causal Inference
Phụ trách: TV4 (Production Lead)
Thời lượng: ~2.5 phút

Flow:
  1. Title Card + Mystery mở đầu
  2. Bridge: Nối từ IRM/DRO → giới thiệu Stable Learning
  3. Core Idea + Công thức Cov_weighted
  4. Causal Graph — giải thích chi tiết
  5. Reweighting Demo — vì sao nó hoạt động
  6. Triangle kết nối 3 phương pháp + Pipeline
"""

import sys
import os
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import (
    setup_dark_scene,
    animate_title_card,
    create_insight_box,
    create_label,
    fade_out_all,
)
from utils.math_helpers import (
    create_data_cloud,
    animate_data_cloud_in,
)

config.background_color = BG_DARK


# ─────────────────────────────────────────────
#  Helper nội bộ
# ─────────────────────────────────────────────

def make_node(label_text, color, position):
    """Tạo một node hình tròn có chữ bên trong."""
    circle = Circle(radius=0.45, color=color, fill_color=color,
                    fill_opacity=0.25, stroke_width=2.5)
    text = Text(label_text, font_size=SIZE_CAPTION,
                color=TEXT_PRIMARY, font=FONT_PRIMARY, weight=BOLD)
    node = VGroup(circle, text).move_to(position)
    return node


def make_arrow(start_pos, end_pos, color=TEXT_SECONDARY, stroke_width=2.5):
    """Tạo mũi tên giữa 2 vị trí."""
    return Arrow(
        start_pos, end_pos,
        buff=0.5, color=color,
        stroke_width=stroke_width, tip_length=0.2,
    )


def narration_text(text, font_size=SIZE_BODY, color=TEXT_PRIMARY):
    """Tạo text narration style 3B1B."""
    return Text(
        text, font_size=font_size, color=color,
        font=FONT_PRIMARY, line_spacing=1.4,
    )


# ─────────────────────────────────────────────
#  MAIN SCENE
# ─────────────────────────────────────────────

class StableLearningScene(Scene):
    """
    Scene 9: Stable Learning — Nhìn từ góc nhân quả.
    Author: TV4
    Duration: ~2.5 phút
    """

    def construct(self):
        setup_dark_scene(self)

        self._block1_title_and_mystery()
        self._block2_bridge_and_intro()
        self._block3_core_formula()
        self._block4_causal_graph()
        self._block5_reweighting_demo()
        self._block6_triangle_and_pipeline()

    # ═══════════════════════════════════════════
    # BLOCK 1: Title Card + Mystery (~15 giây)
    # ═══════════════════════════════════════════
    def _block1_title_and_mystery(self):
        # --- Title card ---
        animate_title_card(self, "Stable Learning", "Nhìn từ góc nhân quả")

        # --- Mystery question ---
        mystery = narration_text(
            "Nếu ta biết được cấu trúc nhân quả\n"
            "— ta có thể loại bỏ spurious correlations\n"
            "trực tiếp không?",
            font_size=SIZE_SUBSECTION,
            color=THEME_AMBER,
        )
        mystery.move_to(ORIGIN)

        q_mark = Text("?", font_size=80, color=THEME_AMBER,
                       font=FONT_PRIMARY, weight=BOLD)
        q_mark.next_to(mystery, RIGHT, buff=0.3)

        self.play(Write(mystery), run_time=TIME_SLOW)
        self.play(FadeIn(q_mark, scale=1.5), run_time=TIME_FAST)
        self.wait(TIME_LONG_PAUSE)
        self.play(FadeOut(mystery), FadeOut(q_mark))

    # ═══════════════════════════════════════════
    # BLOCK 2: Bridge từ IRM/DRO + Giới thiệu (~30 giây)
    # ═══════════════════════════════════════════
    def _block2_bridge_and_intro(self):
        # --- Nhắc lại 2 phương pháp trước ---
        header = narration_text(
            "Hai phương pháp ta đã học:",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        # IRM box
        irm_title = Text("IRM", font_size=SIZE_SUBSECTION, color=THEME_BLUE,
                         font=FONT_PRIMARY, weight=BOLD)
        irm_desc = Text(
            "Tìm đặc trưng bất biến\nqua các môi trường",
            font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY,
        )
        irm_group = VGroup(irm_title, irm_desc).arrange(DOWN, buff=0.2)
        irm_box = SurroundingRectangle(irm_group, color=THEME_BLUE,
                                        buff=0.3, corner_radius=0.1)
        irm_all = VGroup(irm_box, irm_group).move_to(LEFT * 3 + DOWN * 0.3)

        # DRO box
        dro_title = Text("DRO", font_size=SIZE_SUBSECTION, color=THEME_ORANGE,
                         font=FONT_PRIMARY, weight=BOLD)
        dro_desc = Text(
            "Tối ưu cho trường hợp\nxấu nhất",
            font_size=SIZE_SMALL, color=TEXT_SECONDARY, font=FONT_PRIMARY,
        )
        dro_group = VGroup(dro_title, dro_desc).arrange(DOWN, buff=0.2)
        dro_box = SurroundingRectangle(dro_group, color=THEME_ORANGE,
                                        buff=0.3, corner_radius=0.1)
        dro_all = VGroup(dro_box, dro_group).move_to(RIGHT * 3 + DOWN * 0.3)

        self.play(FadeIn(irm_all, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.play(FadeIn(dro_all, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        # --- Nhược điểm thực tế ---
        common = narration_text(
            "Nhưng thực tế: ta thường KHÔNG có nhãn môi trường (cho IRM)\n"
            "và RẤT KHÓ đoán đúng sự dịch chuyển (cho DRO).",
            font_size=SIZE_CAPTION, color=THEME_RED,
        ).to_edge(DOWN, buff=1.0)
        self.play(Write(common), run_time=TIME_SLOW)
        self.wait(TIME_LONG_PAUSE)

        # --- Fade → giới thiệu cách thứ ba ---
        self.play(
            FadeOut(header), FadeOut(irm_all), FadeOut(dro_all),
            FadeOut(common),
        )

        # Giới thiệu Stable Learning
        intro1 = narration_text(
            "Nhưng còn một cách thứ ba:",
            font_size=SIZE_SUBSECTION, color=TEXT_PRIMARY,
        ).move_to(UP * 1.5)

        intro2 = narration_text(
            "Nhìn thẳng vào cấu trúc NHÂN QUẢ của dữ liệu",
            font_size=SIZE_SUBSECTION, color=THEME_EMERALD,
        ).move_to(UP * 0.3)

        intro3 = narration_text(
            "Nếu ta hiểu được cái gì gây ra cái gì,\n"
            "ta có thể loại bỏ các mối tương quan giả\n"
            "một cách trực tiếp.",
            font_size=SIZE_BODY, color=TEXT_SECONDARY,
        ).move_to(DOWN * 1.2)

        self.play(Write(intro1), run_time=TIME_NORMAL)
        self.wait(0.5)
        self.play(Write(intro2), run_time=TIME_SLOW)
        self.wait(0.5)
        self.play(FadeIn(intro3, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(TIME_LONG_PAUSE)

        # --- Tên phương pháp xuất hiện ---
        self.play(FadeOut(intro1), FadeOut(intro2), FadeOut(intro3))

        sl_title = Text(
            "STABLE LEARNING",
            font_size=SIZE_TITLE, color=THEME_AMBER,
            font=FONT_PRIMARY, weight=BOLD,
        ).move_to(UP * 0.8)

        sl_author = Text(
            "Kuang et al. (2018) — Peng Cui's Lab, Tsinghua University",
            font_size=SIZE_SMALL, color=TEXT_MUTED, font=FONT_PRIMARY,
        ).move_to(ORIGIN)

        sl_idea = narration_text(
            "Ý tưởng: Điều chỉnh trọng số từng mẫu dữ liệu\n"
            "để các đặc trưng trở nên KHÔNG PHỤ THUỘC nhau.\n"
            "(VD: Phạt nặng các mẫu 'Bò trên cỏ', tăng trọng số 'Bò trên biển'\n"
            "để phá vỡ sự liên kết giả giữa bò và bối cảnh).",
            font_size=SIZE_BODY, color=TEXT_PRIMARY,
        ).move_to(DOWN * 1.5)

        self.play(FadeIn(sl_title, scale=1.1), run_time=TIME_NORMAL)
        self.play(FadeIn(sl_author), run_time=TIME_FAST)
        self.wait(TIME_PAUSE)
        self.play(Write(sl_idea), run_time=TIME_SLOW)
        self.wait(TIME_LONG_PAUSE)

        self.play(
            FadeOut(sl_title), FadeOut(sl_author), FadeOut(sl_idea),
        )

    # ═══════════════════════════════════════════
    # BLOCK 3: Công thức cốt lõi (~20 giây)
    # ═══════════════════════════════════════════
    def _block3_core_formula(self):
        header = narration_text(
            "Công thức cốt lõi của Stable Learning:",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        # --- Giải thích bằng text trước ---
        explain1 = narration_text(
            "Tìm trọng số w cho mỗi mẫu dữ liệu sao cho:",
            font_size=SIZE_BODY, color=TEXT_SECONDARY,
        ).move_to(UP * 1.0)
        self.play(Write(explain1), run_time=TIME_NORMAL)
        self.wait(0.5)

        # --- Công thức (dùng MathTex nếu có LaTeX, fallback Text) ---
        try:
            formula = MathTex(
                r"\text{Cov}_{\text{weighted}}",
                r"(X_k, \, X_l)",
                r"\approx 0",
                r"\quad \forall \, k \neq l",
                font_size=SIZE_FORMULA,
                color=TEXT_PRIMARY,
            )
            # Tô màu từng phần
            formula[0].set_color(THEME_AMBER)    # Cov_weighted
            formula[2].set_color(THEME_EMERALD)  # ≈ 0
        except Exception:
            # Fallback nếu không có LaTeX
            formula = Text(
                "Cov_weighted(Xk, Xl) ≈ 0    ∀k ≠ l",
                font_size=SIZE_SUBSECTION, color=TEXT_PRIMARY,
                font=FONT_PRIMARY,
            )

        formula.move_to(ORIGIN)
        self.play(Write(formula), run_time=TIME_SLOW)
        self.wait(TIME_PAUSE)

        # --- Giải thích ý nghĩa ---
        meaning1 = narration_text(
            "= Trong bộ dữ liệu đã điều chỉnh trọng số,",
            font_size=SIZE_CAPTION, color=TEXT_SECONDARY,
        ).move_to(DOWN * 1.2)

        meaning2 = narration_text(
            "tất cả các cặp đặc trưng phải KHÔNG TƯƠNG QUAN nhau",
            font_size=SIZE_CAPTION, color=THEME_EMERALD,
        ).move_to(DOWN * 1.8)

        self.play(FadeIn(meaning1, shift=UP * 0.1), run_time=TIME_NORMAL)
        self.play(FadeIn(meaning2, shift=UP * 0.1), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        # --- Key insight ---
        insight = create_insight_box(
            "Khi features independent → model buộc phải\n"
            "đánh giá từng feature riêng lẻ\n"
            "→ dễ tìm ra causal features!",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        )
        insight.to_edge(DOWN, buff=0.3)
        self.play(FadeIn(insight, shift=UP * 0.2))
        self.wait(TIME_LONG_PAUSE)

        self.play(
            FadeOut(header), FadeOut(explain1), FadeOut(formula),
            FadeOut(meaning1), FadeOut(meaning2), FadeOut(insight),
        )

    # ═══════════════════════════════════════════
    # BLOCK 4: Causal Graph chi tiết (~35 giây)
    # ═══════════════════════════════════════════
    def _block4_causal_graph(self):
        header = narration_text(
            "Nhìn từ đồ thị nhân quả (Causal Graph):",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        # --- Tạo 4 node ---
        POS_Z  = UP * 2.3
        POS_XC = LEFT * 3.0 + UP * 0.3
        POS_XS = RIGHT * 3.0 + UP * 0.3
        POS_Y  = DOWN * 1.5

        node_Z  = make_node("Z",  THEME_AMBER,   POS_Z)
        node_Xc = make_node("Xc", THEME_EMERALD, POS_XC)
        node_Xs = make_node("Xs", THEME_RED,     POS_XS)
        node_Y  = make_node("Y",  THEME_BLUE,    POS_Y)

        # --- Labels giải thích ---
        lbl_Z = Text("Confounder\n(Mùa, Địa điểm...)",
                      font_size=SIZE_SMALL, color=THEME_AMBER, font=FONT_PRIMARY)
        lbl_Z.next_to(node_Z, RIGHT, buff=0.3)

        lbl_Xc = Text("Đặc trưng nhân quả\n(Hình dạng con bò)",
                       font_size=SIZE_SMALL, color=THEME_EMERALD, font=FONT_PRIMARY)
        lbl_Xc.next_to(node_Xc, LEFT, buff=0.3)

        lbl_Xs = Text("Đặc trưng giả\n(Nền cỏ / Nền biển)",
                       font_size=SIZE_SMALL, color=THEME_RED, font=FONT_PRIMARY)
        lbl_Xs.next_to(node_Xs, RIGHT, buff=0.3)

        lbl_Y = Text("Label (Bò / Lạc đà)",
                      font_size=SIZE_SMALL, color=THEME_BLUE, font=FONT_PRIMARY)
        lbl_Y.next_to(node_Y, DOWN, buff=0.3)

        # --- Mũi tên ---
        arrow_Z_Xc = make_arrow(POS_Z, POS_XC, color=TEXT_SECONDARY)
        arrow_Z_Xs = make_arrow(POS_Z, POS_XS, color=TEXT_SECONDARY)
        arrow_Xc_Y = make_arrow(POS_XC, POS_Y, color=THEME_EMERALD, stroke_width=3.5)
        arrow_Xs_Y = make_arrow(POS_XS, POS_Y, color=THEME_RED, stroke_width=3.5)

        # ── Step 1: Node Z xuất hiện ──
        self.play(FadeIn(node_Z, scale=0.7), run_time=TIME_NORMAL)
        self.play(Write(lbl_Z), run_time=TIME_FAST)
        self.wait(0.5)

        explain_Z = narration_text(
            "Z là 'thủ phạm ẩn' — nó ảnh hưởng đến\n"
            "cả đặc trưng thật lẫn đặc trưng giả",
            font_size=SIZE_CAPTION, color=TEXT_MUTED,
        ).to_edge(DOWN, buff=0.4)
        self.play(FadeIn(explain_Z), run_time=TIME_FAST)
        self.wait(TIME_PAUSE)

        # ── Step 2: Z → Xc (đặc trưng thật) ──
        self.play(GrowArrow(arrow_Z_Xc), run_time=TIME_NORMAL)
        self.play(FadeIn(node_Xc, scale=0.7), Write(lbl_Xc), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        # ── Step 3: Z → Xs (đặc trưng giả) ──
        self.play(GrowArrow(arrow_Z_Xs), run_time=TIME_NORMAL)
        self.play(FadeIn(node_Xs, scale=0.7), Write(lbl_Xs), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        # ── Step 4: Xc → Y (causal path) ──
        self.play(FadeOut(explain_Z))
        self.play(GrowArrow(arrow_Xc_Y), run_time=TIME_NORMAL)
        self.play(FadeIn(node_Y, scale=0.7), Write(lbl_Y), run_time=TIME_NORMAL)

        causal_tag = Text(
            "CAUSAL PATH  ✓  (ổn định qua mọi môi trường)",
            font_size=SIZE_SMALL, color=THEME_EMERALD,
            font=FONT_PRIMARY, weight=BOLD,
        ).next_to(arrow_Xc_Y, LEFT, buff=0.15)
        self.play(Write(causal_tag), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        # ── Step 5: Xs → Y (spurious path) + gạch bỏ ──
        self.play(GrowArrow(arrow_Xs_Y), run_time=TIME_NORMAL)

        spurious_tag = Text(
            "SPURIOUS PATH  ✗  (thay đổi theo môi trường!)",
            font_size=SIZE_SMALL, color=THEME_RED,
            font=FONT_PRIMARY, weight=BOLD,
        ).next_to(arrow_Xs_Y, RIGHT, buff=0.15)
        self.play(Write(spurious_tag), run_time=TIME_NORMAL)

        # Gạch chéo đường spurious
        cross = Cross(arrow_Xs_Y, stroke_color=THEME_RED, stroke_width=5)
        self.play(Create(cross), run_time=TIME_FAST)
        self.wait(TIME_PAUSE)

        # ── Insight: Tại sao Z gây vấn đề ──
        insight_text = narration_text(
            "Z (confounder) làm cho Xc và Xs tương quan nhau trong training data\n"
            "→ Model không phân biệt được đặc trưng thật và giả!",
            font_size=SIZE_CAPTION, color=THEME_AMBER,
        ).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(insight_text, shift=UP * 0.2))
        self.wait(TIME_LONG_PAUSE)

        # ── Fade out block 4 ──
        all_b4 = VGroup(
            header, node_Z, node_Xc, node_Xs, node_Y,
            lbl_Z, lbl_Xc, lbl_Xs, lbl_Y,
            arrow_Z_Xc, arrow_Z_Xs, arrow_Xc_Y, arrow_Xs_Y,
            cross, causal_tag, spurious_tag, insight_text,
        )
        self.play(FadeOut(all_b4), run_time=TIME_NORMAL)

    # ═══════════════════════════════════════════
    # BLOCK 5: Reweighting Demo (~30 giây)
    # ═══════════════════════════════════════════
    def _block5_reweighting_demo(self):
        header = narration_text(
            "Stable Learning hoạt động như thế nào?",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        # --- Giải thích bước 1: Vấn đề ---
        step1 = narration_text(
            "Vấn đề: Trong training data, bò luôn đi kèm cỏ xanh (90%)\n"
            "→ Model tưởng 'cỏ xanh = bò'",
            font_size=SIZE_CAPTION, color=TEXT_SECONDARY,
        ).move_to(UP * 1.8)
        self.play(Write(step1), run_time=TIME_NORMAL)

        # --- Data points ---
        dots_majority = create_data_cloud(
            center=(-2.5, 0.5), n_points=18, std=0.55,
            color=THEME_EMERALD, radius=0.10, seed=42,
        )
        dots_minority = create_data_cloud(
            center=(2.0, 0.5), n_points=3, std=0.35,
            color=THEME_BLUE, radius=0.10, seed=7,
        )

        lbl_maj = Text("Bò trên cỏ (90%)", font_size=SIZE_SMALL,
                        color=THEME_EMERALD, font=FONT_PRIMARY)
        lbl_maj.next_to(dots_majority, DOWN, buff=0.5)

        lbl_min = Text("Bò trên biển (10%)", font_size=SIZE_SMALL,
                        color=THEME_BLUE, font=FONT_PRIMARY)
        lbl_min.next_to(dots_minority, DOWN, buff=0.5)

        animate_data_cloud_in(self, dots_majority, run_time=1.2)
        animate_data_cloud_in(self, dots_minority, run_time=0.6)
        self.play(Write(lbl_maj), Write(lbl_min), run_time=TIME_FAST)
        self.wait(TIME_PAUSE)

        # --- Giải thích bước 2: Giải pháp ---
        self.play(FadeOut(step1))
        step2 = narration_text(
            "Giải pháp: Stable Learning điều chỉnh trọng số →\n"
            "Giảm ảnh hưởng nhóm đa số, tăng ảnh hưởng nhóm thiểu số",
            font_size=SIZE_CAPTION, color=THEME_AMBER,
        ).move_to(UP * 1.8)
        self.play(Write(step2), run_time=TIME_NORMAL)
        self.wait(0.5)

        # --- Animation reweight ---
        self.play(
            LaggedStart(
                *[dot.animate.scale(0.5).set_opacity(0.4)
                  for dot in dots_majority],
                lag_ratio=0.03,
            ),
            LaggedStart(
                *[dot.animate.scale(2.8).set_color(THEME_AMBER)
                  for dot in dots_minority],
                lag_ratio=0.1,
            ),
            run_time=TIME_SLOW,
        )

        # Cập nhật label
        new_lbl_maj = Text("Trọng số ↓ (giảm)", font_size=SIZE_SMALL,
                           color=TEXT_MUTED, font=FONT_PRIMARY)
        new_lbl_maj.move_to(lbl_maj.get_center())

        new_lbl_min = Text("Trọng số ↑ (tăng)", font_size=SIZE_SMALL,
                           color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD)
        new_lbl_min.move_to(lbl_min.get_center())

        self.play(
            Transform(lbl_maj, new_lbl_maj),
            Transform(lbl_min, new_lbl_min),
            run_time=TIME_FAST,
        )
        self.wait(TIME_PAUSE)

        # --- Giải thích TẠI SAO nó hoạt động ---
        self.play(FadeOut(step2))
        step3 = narration_text(
            "Sau khi điều chỉnh trọng số:",
            font_size=SIZE_BODY, color=TEXT_PRIMARY,
        ).move_to(UP * 1.8)
        self.play(Write(step3))

        why1 = narration_text(
            "• Xc (hình dạng) và Xs (nền cỏ) không còn tương quan",
            font_size=SIZE_CAPTION, color=THEME_EMERALD,
        ).move_to(DOWN * 1.5)

        why2 = narration_text(
            "• Model buộc phải dựa vào Xc (hình dạng) — đặc trưng thật!",
            font_size=SIZE_CAPTION, color=THEME_EMERALD,
        ).move_to(DOWN * 2.0)

        self.play(FadeIn(why1, shift=UP * 0.1), run_time=TIME_NORMAL)
        self.wait(0.5)
        self.play(FadeIn(why2, shift=UP * 0.1), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)

        # --- Insight box ---
        insight = create_insight_box(
            "Stable Learning 'vô hiệu hóa' confounder Z\n"
            "bằng cách phá vỡ tương quan giả giữa các features!",
            color=THEME_AMBER, font_size=SIZE_CAPTION,
        )
        insight.to_edge(DOWN, buff=0.2)
        self.play(FadeIn(insight, shift=UP * 0.2))
        self.wait(TIME_LONG_PAUSE)

        # --- Fade out ---
        all_b5 = VGroup(
            header, dots_majority, dots_minority,
            lbl_maj, lbl_min, step3,
            why1, why2, insight,
        )
        self.play(FadeOut(all_b5), run_time=TIME_NORMAL)

    # ═══════════════════════════════════════════
    # BLOCK 6: Triangle + Pipeline (~20 giây)
    # ═══════════════════════════════════════════
    def _block6_triangle_and_pipeline(self):

        # ══ 6a: Tam giác kết nối 3 phương pháp ══
        header = narration_text(
            "Ba con đường — một đích đến",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        # Giải thích: cả 3 đều muốn gì?
        goal = narration_text(
            "Mục tiêu chung: Model chỉ dùng CAUSAL FEATURES",
            font_size=SIZE_BODY, color=THEME_EMERALD,
        ).move_to(UP * 2.3)
        self.play(Write(goal), run_time=TIME_NORMAL)
        self.wait(0.5)

        # 3 đỉnh tam giác
        POS_TOP   = UP * 0.1
        POS_LEFT  = DOWN * 2.2 + LEFT * 3.5
        POS_RIGHT = DOWN * 2.2 + RIGHT * 3.5

        # 3 cạnh
        line_tl = Line(POS_TOP, POS_LEFT, color=TEXT_MUTED, stroke_width=2)
        line_tr = Line(POS_TOP, POS_RIGHT, color=TEXT_MUTED, stroke_width=2)
        line_lr = Line(POS_LEFT, POS_RIGHT, color=TEXT_MUTED, stroke_width=2)

        # Labels
        txt_c = VGroup(
            Text("Causality", font_size=SIZE_BODY, color=THEME_AMBER,
                 font=FONT_PRIMARY, weight=BOLD),
            Text("(Stable Learning)", font_size=SIZE_SMALL, color=THEME_AMBER,
                 font=FONT_PRIMARY),
            Text("Loại bỏ confounder", font_size=SIZE_SMALL,
                 color=TEXT_SECONDARY, font=FONT_PRIMARY),
        ).arrange(DOWN, buff=0.08).move_to(POS_TOP + UP * 0.8)

        txt_i = VGroup(
            Text("Invariance", font_size=SIZE_BODY, color=THEME_BLUE,
                 font=FONT_PRIMARY, weight=BOLD),
            Text("(IRM)", font_size=SIZE_SMALL, color=THEME_BLUE,
                 font=FONT_PRIMARY),
            Text("Tìm feature bất biến", font_size=SIZE_SMALL,
                 color=TEXT_SECONDARY, font=FONT_PRIMARY),
        ).arrange(DOWN, buff=0.08).move_to(POS_LEFT + DOWN * 0.7)

        txt_r = VGroup(
            Text("Robustness", font_size=SIZE_BODY, color=THEME_ORANGE,
                 font=FONT_PRIMARY, weight=BOLD),
            Text("(DRO)", font_size=SIZE_SMALL, color=THEME_ORANGE,
                 font=FONT_PRIMARY),
            Text("Tối ưu worst-case", font_size=SIZE_SMALL,
                 color=TEXT_SECONDARY, font=FONT_PRIMARY),
        ).arrange(DOWN, buff=0.08).move_to(POS_RIGHT + DOWN * 0.7)

        # Animate tam giác
        self.play(
            LaggedStart(Create(line_tl), Create(line_tr), Create(line_lr),
                        lag_ratio=0.3),
            run_time=TIME_SLOW,
        )
        self.play(
            LaggedStart(
                FadeIn(txt_c, shift=DOWN * 0.2),
                FadeIn(txt_i, shift=UP * 0.2),
                FadeIn(txt_r, shift=UP * 0.2),
                lag_ratio=0.3),
            run_time=TIME_SLOW,
        )
        self.wait(TIME_LONG_PAUSE)

        # Fade out tam giác
        tri_group = VGroup(
            header, goal,
            line_tl, line_tr, line_lr,
            txt_c, txt_i, txt_r,
        )
        self.play(FadeOut(tri_group), run_time=TIME_NORMAL)

        # ══ 6b: Pipeline tổng thể ══
        header2 = narration_text(
            "Heterogeneous Risk Minimization (HRM):",
            font_size=SIZE_SECTION, color=THEME_AMBER,
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(header2, shift=DOWN * 0.2))

        # 4 bước pipeline
        steps_data = [
            ("Data",                 THEME_BLUE,    "Thu thập từ\nnhiều nguồn"),
            ("Nhận diện\nHeterogeneity", THEME_AMBER, "Phát hiện\ncác environments"),
            ("Học đặc trưng\nổn định",   THEME_EMERALD,"IRM / DRO /\nStable Learning"),
            ("Đánh giá\nOOD accuracy",   THEME_PURPLE, "Worst-group acc\n+ OOD test"),
        ]

        step_groups = []
        for label, color, desc in steps_data:
            title = Text(label, font_size=16, color=color,
                         font=FONT_PRIMARY, weight=BOLD)
            description = Text(desc, font_size=14, color=TEXT_MUTED,
                               font=FONT_PRIMARY)
            content = VGroup(title, description).arrange(DOWN, buff=0.1)
            box = SurroundingRectangle(content, color=color, buff=0.15,
                                        corner_radius=0.1, stroke_width=2)
            grp = VGroup(box, content)
            step_groups.append(grp)

        pipeline_row = VGroup(*step_groups).arrange(RIGHT, buff=0.4)
        pipeline_row.move_to(UP * 0.2)

        # Mũi tên
        arrows = []
        for i in range(len(step_groups) - 1):
            arr = Arrow(
                step_groups[i].get_right(),
                step_groups[i + 1].get_left(),
                color=TEXT_MUTED, buff=0.05,
                stroke_width=2, tip_length=0.18,
            )
            arrows.append(arr)

        # Animate từng bước
        for i, grp in enumerate(step_groups):
            self.play(FadeIn(grp, shift=UP * 0.2), run_time=0.6)
            if i < len(arrows):
                self.play(GrowArrow(arrows[i]), run_time=0.3)

        self.wait(TIME_PAUSE)

        # ── Final message ──
        final = narration_text(
            "Heterogeneity không phải lỗi trong dữ liệu\n"
            "— đó là đặc trưng của thế giới thực.\n"
            "Và học cách tận dụng nó chính là cách\n"
            "xây dựng AI thực sự hoạt động.",
            font_size=SIZE_BODY, color=THEME_AMBER,
        ).to_edge(DOWN, buff=0.3)
        self.play(Write(final), run_time=TIME_LONG_PAUSE)
        self.wait(TIME_LONG_PAUSE)

        # Fade out
        all_b6 = VGroup(header2, *step_groups, *arrows, final)
        self.play(FadeOut(all_b6), run_time=TIME_NORMAL)
        self.wait(TIME_PAUSE)
