"""
Scene 10: Tổng kết và Kết luận (Heterogeneity là thông tin)
Phụ trách: TV4 (Production Lead)
Thời lượng: ~2 phút

Flow:
  1. Rapid recap montage (Nhìn lại chặng đường)
  2. Final comparison table (So sánh 4 phương pháp)
  3. Open problems (Các bài toán mở)
  4. Final message & Credits
"""

import sys
import os
from manim import *

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from utils.theme import *
from utils.components import (
    setup_dark_scene,
    narration_text,
    create_label,
)

config.background_color = BG_DARK


class ConclusionScene(Scene):
    """
    Scene 10: Kết luận toàn bộ Video.
    Author: TV4
    """

    def construct(self):
        setup_dark_scene(self)

        self._block1_recap_montage()
        self._block2_comparison_table()
        self._block3_open_problems()
        self._block4_final_message_and_credits()

    # ═══════════════════════════════════════════
    # BLOCK 1: Rapid Recap Montage (~20s)
    # ═══════════════════════════════════════════
    def _block1_recap_montage(self):
        # Narration mở đầu
        intro = narration_text(
            "Hãy cùng nhìn lại chặng đường chúng ta vừa đi qua...",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).move_to(UP * 2.5)
        self.play(Write(intro), run_time=TIME_NORMAL)
        self.wait(0.5)

        # Các từ khóa cốt lõi
        keywords = [
            ("i.i.d. Assumption", THEME_BLUE),
            ("Distribution Shift", THEME_RED),
            ("Data Heterogeneity", THEME_AMBER),
            ("Spurious Correlations", THEME_ORANGE),
            ("ERM Fails", THEME_RED),
            ("IRM", THEME_BLUE),
            ("DRO", THEME_ORANGE),
            ("Stable Learning", THEME_EMERALD),
        ]

        texts = []
        for word, color in keywords:
            t = Text(word, font_size=SIZE_TITLE, color=color,
                     font=FONT_PRIMARY, weight=BOLD).move_to(ORIGIN)
            texts.append(t)

        # Rapid flash
        for i in range(len(texts)):
            if i == 0:
                self.play(FadeIn(texts[i], scale=1.2), run_time=0.6)
            else:
                self.play(
                    ReplacementTransform(texts[i-1], texts[i]),
                    run_time=0.6
                )
            self.wait(0.3)

        self.wait(TIME_PAUSE)
        self.play(FadeOut(texts[-1]), FadeOut(intro), run_time=TIME_FAST)

    # ═══════════════════════════════════════════
    # BLOCK 2: Bảng so sánh 4 phương pháp (~45s)
    # ═══════════════════════════════════════════
    def _block2_comparison_table(self):
        header = narration_text(
            "So sánh các phương pháp đối phó Distribution Shift",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.4)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        # --- Dữ liệu bảng ---
        columns = ["Phương pháp", "Cần dữ liệu gì?", "Mục tiêu tối ưu", "Điểm mạnh", "Điểm yếu"]
        
        row1 = ["ERM", "Dữ liệu gộp", "Trung bình (Average)", "Đơn giản, nhanh", "Dễ dính tương quan giả"]
        row2 = ["IRM", "Nhãn môi trường", "Đặc trưng bất biến", "Lý thuyết vững chắc", "Thực tế hiếm khi có nhãn"]
        row3 = ["Group DRO", "Nhãn nhóm", "Nhóm tệ nhất", "Hiệu quả thực tế cao", "Quá bảo thủ (Pesimistic)"]
        row4 = ["Stable Learning", "Kiến thức nhân quả", "Đặc trưng độc lập", "Dễ diễn giải", "Cần hiểu sâu về miền dữ liệu"]

        data = [columns, row1, row2, row3, row4]
        colors = [TEXT_MUTED, TEXT_PRIMARY, THEME_BLUE, THEME_ORANGE, THEME_EMERALD]

        # Xây dựng bảng (sử dụng VGroup dạng lưới)
        table_group = VGroup()
        for i, row in enumerate(data):
            row_group = VGroup()
            for j, text in enumerate(row):
                # Cột đầu tiên (tên PP) in đậm và to hơn chút
                if j == 0 and i > 0:
                    item = Text(text, font_size=20, color=colors[i], font=FONT_PRIMARY, weight=BOLD)
                elif i == 0: # Header
                    item = Text(text, font_size=18, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD)
                else:
                    item = Text(text, font_size=18, color=TEXT_SECONDARY, font=FONT_PRIMARY)
                
                # Căn chỉnh chiều rộng giả lập
                box = Rectangle(width=2.6, height=0.8, color=BG_DARK).set_opacity(0)
                item.move_to(box.get_center())
                cell = VGroup(box, item)
                row_group.add(cell)
            
            row_group.arrange(RIGHT, buff=0.1)
            table_group.add(row_group)

        table_group.arrange(DOWN, buff=0.2).move_to(DOWN * 0.3)

        # Lines ngang phân cách
        line_top = Line(table_group.get_left() + LEFT*0.2 + UP*2.0, table_group.get_right() + RIGHT*0.2 + UP*2.0, color=TEXT_MUTED, stroke_width=2)
        line_bot = Line(table_group.get_left() + LEFT*0.2 + DOWN*2.8, table_group.get_right() + RIGHT*0.2 + DOWN*2.8, color=TEXT_MUTED, stroke_width=2)

        # Animate Header
        self.play(FadeIn(table_group[0], shift=DOWN*0.1), Create(line_top))
        
        # Animate từng dòng
        for i in range(1, len(data)):
            self.play(FadeIn(table_group[i], shift=RIGHT*0.2), run_time=0.8)
            self.wait(0.3)
            
        self.play(Create(line_bot))
        self.wait(TIME_LONG_PAUSE)

        # Fade out bảng
        all_b2 = VGroup(header, table_group, line_top, line_bot)
        self.play(FadeOut(all_b2), run_time=TIME_NORMAL)

    # ═══════════════════════════════════════════
    # BLOCK 3: Open Problems (~30s)
    # ═══════════════════════════════════════════
    def _block3_open_problems(self):
        header = narration_text(
            "Tương lai & Các bài toán mở (Open Problems)",
            font_size=SIZE_SECTION, color=TEXT_PRIMARY,
        ).to_edge(UP, buff=0.5)
        self.play(FadeIn(header, shift=DOWN * 0.2))

        problems = [
            ("Self-aware models", "Mô hình biết khi nào mình không biết (OOD detection)"),
            ("Uncertainty quantification", "Định lượng độ bất định thay vì tự tin đoán sai"),
            ("Scalability", "Áp dụng kỹ thuật Robustness lên các mô hình hàng tỷ tham số"),
            ("Label-free Heterogeneity", "Học môi trường tự động mà không cần gán nhãn thủ công (HRM)"),
        ]

        prob_groups = VGroup()
        icons = ["🤔", "📊", "🏗️", "🤖"]

        for i, (title, desc) in enumerate(problems):
            icon = Text(icons[i], font_size=32).move_to(LEFT * 5)
            t_title = Text(title, font_size=24, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD)
            t_title.next_to(icon, RIGHT, buff=0.4)
            t_desc = Text(desc, font_size=20, color=TEXT_SECONDARY, font=FONT_PRIMARY)
            t_desc.next_to(t_title, DOWN, aligned_edge=LEFT, buff=0.15)
            
            grp = VGroup(icon, t_title, t_desc)
            prob_groups.add(grp)

        prob_groups.arrange(DOWN, buff=0.6, aligned_edge=LEFT).move_to(DOWN * 0.2)

        # Animate từng problem
        for grp in prob_groups:
            self.play(FadeIn(grp, shift=UP * 0.2), run_time=TIME_NORMAL)
            self.wait(0.6)

        self.wait(TIME_LONG_PAUSE)
        self.play(FadeOut(header), FadeOut(prob_groups))

    # ═══════════════════════════════════════════
    # BLOCK 4: Final Message & Credits (~30s)
    # ═══════════════════════════════════════════
    def _block4_final_message_and_credits(self):
        # --- Final Message ---
        msg1 = Text(
            "Data heterogeneity is not a bug in your dataset —",
            font_size=30, color=TEXT_PRIMARY, font=FONT_PRIMARY, slant=ITALIC
        ).move_to(UP * 0.8)
        
        msg2 = Text(
            "it is a feature of the real world.",
            font_size=36, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD
        ).next_to(msg1, DOWN, buff=0.4)
        
        msg3 = Text(
            "And learning to embrace it is how we build AI that actually works.",
            font_size=26, color=THEME_EMERALD, font=FONT_PRIMARY
        ).next_to(msg2, DOWN, buff=0.6)

        self.play(Write(msg1), run_time=TIME_NORMAL)
        self.wait(0.5)
        self.play(FadeIn(msg2, scale=1.1), run_time=TIME_SLOW)
        self.wait(0.5)
        self.play(Write(msg3), run_time=TIME_SLOW)
        
        self.wait(TIME_LONG_PAUSE * 1.5)
        self.play(FadeOut(msg1), FadeOut(msg2), FadeOut(msg3))

        # --- Credits ---
        credit_title = Text("THANK YOU FOR WATCHING", font_size=40, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD)
        credit_title.move_to(UP * 2.0)

        credit_team = Text("Thực hiện bởi: Nhóm csAI (TV1, TV2, TV3, TV4)", font_size=24, color=TEXT_PRIMARY, font=FONT_PRIMARY)
        credit_team.next_to(credit_title, DOWN, buff=0.8)

        credit_ref = Text("Dựa trên: CoLLAs 2024 Tutorial - Towards Heterogeneity-Aware ML", font_size=20, color=TEXT_SECONDARY, font=FONT_PRIMARY)
        credit_author = Text("By Peng Cui & Jiashuo Liu", font_size=20, color=TEXT_MUTED, font=FONT_PRIMARY)
        
        ref_group = VGroup(credit_ref, credit_author).arrange(DOWN, buff=0.2).next_to(credit_team, DOWN, buff=1.0)

        self.play(FadeIn(credit_title, shift=UP * 0.3))
        self.play(Write(credit_team))
        self.play(FadeIn(ref_group))
        
        self.wait(TIME_LONG_PAUSE * 2)
        self.play(FadeOut(Group(*self.mobjects)))
