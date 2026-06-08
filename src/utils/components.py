"""
Reusable Components — 3Blue1Brown Style
Các building blocks dùng chung cho tất cả scenes.
Import: from utils.components import *
"""

from manim import *
from utils.theme import *


def create_section_title(title_text, subtitle_text="", number=""):
    """Tạo title card theo tinh thần 3B1B: serif, ít khung, nhiều khoảng thở."""
    elements = []

    if number:
        num = Text(
            number,
            font_size=72,
            color=THEME_BLUE,
            font=FONT_PRIMARY,
            weight=BOLD
        )
        elements.append(num)

    title = Text(
        title_text,
        font_size=SIZE_TITLE,
        color=TEXT_PRIMARY,
        font=FONT_PRIMARY,
        weight=MEDIUM,
    )
    elements.append(title)

    if subtitle_text:
        subtitle = Text(
            subtitle_text,
            font_size=SIZE_BODY,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
        )
        elements.append(subtitle)

    return VGroup(*elements).arrange(DOWN, buff=0.4)


def create_insight_box(text, color=THEME_AMBER, font_size=SIZE_BODY):
    """Tạo box highlight mảnh, giống một mathematical callout."""
    content = Text(
        text,
        font_size=font_size,
        color=TEXT_PRIMARY,
        font=FONT_PRIMARY
    )
    box = SurroundingRectangle(
        content,
        color=color,
        buff=0.3,
        corner_radius=0.04,
        stroke_width=1.6
    )
    return VGroup(box, content)


def create_3b1b_glow(mobject, color=THEME_BLUE, n_layers=4, opacity=0.16):
    """Tạo glow thủ công bằng vài bản sao mờ phía sau object."""
    layers = VGroup()
    for index in range(n_layers, 0, -1):
        layer = mobject.copy()
        layer.set_color(color)
        layer.set_opacity(opacity / index)
        layer.scale(1 + 0.018 * index)
        layers.add(layer)
    return layers


def create_chalk_underline(mobject, color=THEME_AMBER, buff=0.08):
    """Đường underline ngắn, mảnh, dùng cho emphasis."""
    line = Line(LEFT, RIGHT, color=color, stroke_width=3)
    line.set_width(mobject.get_width() * 1.04)
    line.next_to(mobject, DOWN, buff=buff)
    return line


def create_label(text, color=TEXT_SECONDARY, font_size=SIZE_CAPTION):
    """Tạo label nhỏ cho annotations."""
    return Text(
        text,
        font_size=font_size,
        color=color,
        font=FONT_PRIMARY
    )


def create_env_dot(x, y, env_index=0, radius=0.06):
    """Tạo data point dot cho environment visualization."""
    return Dot(
        point=[x, y, 0],
        color=ENV_COLORS[env_index % len(ENV_COLORS)],
        radius=radius
    )


def create_formula(latex_string, font_size=SIZE_FORMULA):
    """Tạo math formula với style thống nhất."""
    return MathTex(
        latex_string,
        font_size=font_size,
        color=TEXT_PRIMARY
    )


def setup_dark_scene(scene):
    """Setup dark background cho scene. Gọi ở đầu construct()."""
    scene.camera.background_color = BG_DARK


def fade_out_all(scene, run_time=TIME_NORMAL):
    """Fade out tất cả objects trên scene."""
    if scene.mobjects:
        scene.play(
            *[FadeOut(mob) for mob in scene.mobjects],
            run_time=run_time
        )


def animate_title_card(scene, title_text, subtitle_text=""):
    """Animate một title card hoàn chỉnh."""
    card = create_section_title(title_text, subtitle_text)
    scene.play(FadeIn(card, shift=UP * 0.3), run_time=TIME_NORMAL)
    scene.wait(TIME_PAUSE)
    scene.play(FadeOut(card), run_time=TIME_FAST)
