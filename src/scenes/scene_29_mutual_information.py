"""
Scene 29: Mutual Information
Author: TV3 (Animation Lead)
Duration: ~85 seconds
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from manim import *
from utils.theme import *
from utils.components import *
class MutualInformationScene(Scene):
    def construct(self):
        setup_dark_scene(self)
        
        # 1. Creative Intro: Entropy Venn Diagram
        circle_x = Circle(radius=1.2, color=THEME_BLUE, stroke_width=3, fill_color=THEME_BLUE, fill_opacity=0.15).shift(LEFT * 1.5 + DOWN * 0.2)
        circle_y = Circle(radius=1.2, color=THEME_AMBER, stroke_width=3, fill_color=THEME_AMBER, fill_opacity=0.15).shift(RIGHT * 1.5 + DOWN * 0.2)
        
        lbl_x = Text("X", font_size=SIZE_BODY, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(circle_x.get_center())
        lbl_y = Text("Y", font_size=SIZE_BODY, color=THEME_AMBER, font=FONT_PRIMARY, weight=BOLD).move_to(circle_y.get_center())
        
        title_text = Text("Mutual Information", font_size=SIZE_TITLE - 8, color=THEME_EMERALD, font=FONT_PRIMARY, weight=BOLD).move_to(UP * 2.2)
        subtitle_text = Text("Thông tin tương hỗ là gì?", font_size=SIZE_BODY - 4, color=TEXT_SECONDARY, font=FONT_PRIMARY).next_to(title_text, DOWN, buff=0.25)
        
        # Animate circles sliding together
        self.play(FadeIn(circle_x), FadeIn(lbl_x), FadeIn(circle_y), FadeIn(lbl_y), run_time=1.0)
        
        target_x = LEFT * 0.6 + DOWN * 0.2
        target_y = RIGHT * 0.6 + DOWN * 0.2
        
        final_x = Circle(radius=1.2, color=THEME_BLUE, stroke_width=3, fill_color=THEME_BLUE, fill_opacity=0.15).shift(target_x)
        final_y = Circle(radius=1.2, color=THEME_AMBER, stroke_width=3, fill_color=THEME_AMBER, fill_opacity=0.15).shift(target_y)
        intersection_shape = Intersection(final_x, final_y, color=THEME_EMERALD, stroke_width=4, fill_color=THEME_EMERALD, fill_opacity=0.45)
        glow_intersection = create_3b1b_glow(intersection_shape, color=THEME_EMERALD, n_layers=4, opacity=0.2)
        lbl_ixy = MathTex(r"I(X; Y)", font_size=SIZE_BODY, color=THEME_EMERALD).move_to(DOWN * 0.2)
        
        self.play(
            circle_x.animate.shift(RIGHT * 0.9),
            lbl_x.animate.shift(RIGHT * 0.3),  # Shift to center of non-overlapping crescent (x = -1.2)
            circle_y.animate.shift(LEFT * 0.9),
            lbl_y.animate.shift(LEFT * 0.3),   # Shift to center of non-overlapping crescent (x = 1.2)
            Write(title_text),
            FadeIn(subtitle_text, shift=UP * 0.1),
            run_time=1.5
        )
        self.play(FadeIn(intersection_shape), FadeIn(glow_intersection), FadeIn(lbl_ixy), run_time=0.8)
        self.wait(1.5)
        
        # Clean up
        self.play(
            FadeOut(circle_x), FadeOut(lbl_x),
            FadeOut(circle_y), FadeOut(lbl_y),
            FadeOut(intersection_shape), FadeOut(glow_intersection), FadeOut(lbl_ixy),
            FadeOut(title_text), FadeOut(subtitle_text),
            run_time=TIME_FAST
        )
        self.wait(1.0)
        
        # Subtitle 1
        sub1 = create_subtitle("Mutual information đo lượng thông tin X cung cấp về Y. H(Y) là bất định ban đầu.")
        self.play(FadeIn(sub1))
        self.wait(7.0)
        
        # 2. Visualize Entropy H(Y)
        # Rectangle representing uncertainty (shifted to center x=0.0, width 2.2)
        h_y_rect = Rectangle(width=2.2, height=3.6, color=THEME_AMBER, fill_color=THEME_AMBER, fill_opacity=0.4, stroke_width=3).shift(UP * 0.8)
        h_y_label = MathTex(r"H(Y)", font_size=SIZE_FORMULA, color=THEME_AMBER).move_to(h_y_rect.get_center())
        h_y_desc = Text("Sự bất định ban đầu của Y", font_size=18, color=THEME_AMBER, font=FONT_PRIMARY).next_to(h_y_rect, UP, buff=0.25)
        
        self.play(Create(h_y_rect), Write(h_y_label), Write(h_y_desc), run_time=TIME_NORMAL)
        self.wait(10.0)
        
        # Introduce X (text/box on the left, shifted to x = -4.2)
        x_box = RoundedRectangle(width=2.1, height=1.0, corner_radius=0.08, stroke_color=THEME_BLUE, stroke_width=2).shift(LEFT * 4.2 + UP * 0.8)
        x_label = Text("Quan sát X", font_size=SIZE_CAPTION, color=THEME_BLUE, font=FONT_PRIMARY, weight=BOLD).move_to(x_box.get_center())
        
        self.play(FadeIn(x_box, shift=RIGHT * 0.2), Write(x_label), run_time=TIME_NORMAL)
        
        # Subtitle 2
        sub2 = create_subtitle("H(Y|X) là bất định còn lại sau khi biết X. Phần giảm đi chính là I(X;Y).")
        self.play(Transform(sub1, sub2))
        self.wait(7.0)
        
        # Animate shrinking of H(Y) to H(Y|X)
        # The top part of the rectangle will split and move to the right as I(X;Y)
        # both aligned to the same baseline y = -1.0
        h_yx_rect = Rectangle(width=2.2, height=1.4, color=THEME_BLUE, fill_color=THEME_BLUE, fill_opacity=0.4, stroke_width=3).shift(DOWN * 0.3)
        h_yx_label = MathTex(r"H(Y \mid X)", font_size=SIZE_BODY, color=THEME_BLUE).move_to(h_yx_rect.get_center())
        
        i_xy_rect = Rectangle(width=2.2, height=2.2, color=THEME_EMERALD, fill_color=THEME_EMERALD, fill_opacity=0.5, stroke_width=3).shift(RIGHT * 4.2 + UP * 0.1)
        i_xy_label = MathTex(r"I(X; Y)", font_size=SIZE_FORMULA, color=THEME_EMERALD).move_to(i_xy_rect.get_center())
        i_xy_desc = Text("Mutual Information\n(Giảm thiểu bất định)", font_size=18, color=THEME_EMERALD, font=FONT_PRIMARY).next_to(i_xy_rect, UP, buff=0.25)
        
        # Flow arrow from X to the split
        flow_arrow = Arrow(x_box.get_right(), h_y_rect.get_left(), color=THEME_BLUE, stroke_width=3)
        
        self.play(Create(flow_arrow), run_time=TIME_FAST)
        self.play(
            ReplacementTransform(h_y_rect, VGroup(h_yx_rect, i_xy_rect)),
            Transform(h_y_label, h_yx_label),
            flow_arrow.animate.put_start_and_end_on(x_box.get_right(), h_yx_rect.get_left()),
            FadeOut(h_y_desc),
            FadeIn(i_xy_label), FadeIn(i_xy_desc),
            run_time=TIME_SLOW
        )
        self.wait(11.0)
        
        # 3. Formula Display
        # Display the equation: I(X; Y) = H(Y) - H(Y|X)
        equation = MathTex(
            r"I(X; Y)",            # 0
            r"=",                  # 1
            r"H(Y)",               # 2
            r"-",                  # 3
            r"H(Y \mid X)",        # 4
            font_size=SIZE_FORMULA
        ).shift(DOWN * 2.1)
        fit_to_width(equation, max_width=8.4)
        
        equation[0].set_color(THEME_EMERALD)
        equation[2].set_color(THEME_AMBER)
        equation[4].set_color(THEME_BLUE)
        
        self.play(Write(equation), run_time=TIME_NORMAL)
        self.wait(11.0)
        
        # Takeaway
        insight = create_insight_box(
            "Thông tin chính là sự giảm thiểu bất định.",
            color=THEME_EMERALD,
            font_size=SIZE_CAPTION
        ).to_edge(DOWN, buff=0.7)
        
        self.play(FadeOut(sub1), FadeIn(insight, shift=UP * 0.2), run_time=TIME_NORMAL)
        self.wait(11.5)
        
        # Outro
        self.play(
            FadeOut(insight), FadeOut(equation),
            FadeOut(h_yx_rect), FadeOut(h_y_label), FadeOut(x_box), FadeOut(x_label),
            FadeOut(flow_arrow), FadeOut(i_xy_rect), FadeOut(i_xy_label), FadeOut(i_xy_desc),
            run_time=TIME_NORMAL
        )
        self.wait(3.5)
