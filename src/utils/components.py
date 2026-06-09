"""
Reusable Components — 3Blue1Brown Style
Các building blocks dùng chung cho tất cả scenes.
Import: from utils.components import *
"""

from manim import *
from utils.theme import *
import textwrap


SAFE_FRAME_WIDTH = 12.4
SAFE_FRAME_HEIGHT = 6.2
SUBTITLE_MAX_CHARS = 78
CALLOUT_MAX_CHARS = 48


def _wrapped_lines(text, max_chars):
    lines = []
    for raw_line in str(text).splitlines() or [""]:
        wrapped = textwrap.wrap(raw_line, width=max_chars) if raw_line else [""]
        lines.extend(wrapped)
    return "\n".join(lines)


def fit_to_width(mobject, max_width=SAFE_FRAME_WIDTH):
    """Scale an object down if it is wider than the safe frame."""
    if mobject.get_width() > max_width:
        mobject.scale_to_fit_width(max_width)
    return mobject


def fit_to_height(mobject, max_height=SAFE_FRAME_HEIGHT):
    """Scale an object down if it is taller than the safe frame."""
    if mobject.get_height() > max_height:
        mobject.scale_to_fit_height(max_height)
    return mobject


def fit_to_frame(mobject, max_width=SAFE_FRAME_WIDTH, max_height=SAFE_FRAME_HEIGHT):
    """Keep a mobject inside the visual safe area without upscaling it."""
    fit_to_width(mobject, max_width=max_width)
    fit_to_height(mobject, max_height=max_height)
    return mobject


def create_text_block(
    text,
    font_size=SIZE_BODY,
    color=TEXT_PRIMARY,
    max_chars=CALLOUT_MAX_CHARS,
    weight=NORMAL,
    line_spacing=0.82,
):
    """Create wrapped project text with the shared typography."""
    return Text(
        _wrapped_lines(text, max_chars=max_chars),
        font_size=font_size,
        color=color,
        font=FONT_PRIMARY,
        weight=weight,
        line_spacing=line_spacing,
        should_center=True,
    )


def create_section_title(title_text, subtitle_text="", number=""):
    """Tạo title card với phong cách kính (glassmorphism) hiện đại và đặc sắc."""
    elements = []

    if number:
        num = Text(
            number,
            font_size=52,
            color=THEME_BLUE_LIGHT,
            font=FONT_PRIMARY,
            weight=BOLD
        )
        elements.append(num)

    # Clean title with a beautiful gradient
    title = Text(
        title_text,
        font_size=SIZE_TITLE - 8,
        font=FONT_PRIMARY,
        weight=BOLD,
    )
    title.set_color_by_gradient(THEME_BLUE, THEME_BLUE_LIGHT)
    
    # Title glow
    title_glow = create_3b1b_glow(title, color=THEME_BLUE, n_layers=4, opacity=0.15)
    title_group = VGroup(title_glow, title)
    elements.append(title_group)

    if subtitle_text:
        subtitle = Text(
            subtitle_text,
            font_size=SIZE_BODY - 4,
            color=TEXT_SECONDARY,
            font=FONT_PRIMARY,
            weight=MEDIUM,
        )
        elements.append(subtitle)

    content = VGroup(*elements).arrange(DOWN, buff=0.3)
    
    # Underline
    underline = Line(LEFT, RIGHT, color=THEME_EMERALD, stroke_width=2.5)
    underline.set_width(max(title.get_width() * 0.75, 2.0))
    if subtitle_text:
        underline.next_to(title_group, DOWN, buff=0.15)
        subtitle.next_to(underline, DOWN, buff=0.2)
        content = VGroup(title_group, underline, subtitle)
    else:
        underline.next_to(title_group, DOWN, buff=0.18)
        content = VGroup(title_group, underline)

    # Surrounding glassmorphic panel
    card_bg = RoundedRectangle(
        width=max(content.get_width() + 1.6, 6.5),
        height=content.get_height() + 1.0,
        corner_radius=0.18,
        stroke_color=THEME_BLUE,
        stroke_width=1.6,
        stroke_opacity=0.35,
        fill_color=BG_PANEL,
        fill_opacity=0.75
    )
    
    # Inner border highlight
    card_inner = RoundedRectangle(
        width=card_bg.get_width() - 0.08,
        height=card_bg.get_height() - 0.08,
        corner_radius=0.17,
        stroke_color=TEXT_PRIMARY,
        stroke_width=0.8,
        stroke_opacity=0.12,
        fill_opacity=0
    )
    
    # Put content on top of background
    content.move_to(card_bg.get_center())
    
    return VGroup(card_bg, card_inner, content)


def create_insight_box(text, color=THEME_AMBER, font_size=SIZE_BODY, max_width=10.8, max_chars=CALLOUT_MAX_CHARS):
    """Tạo box highlight mảnh, giống một mathematical callout."""
    content = create_text_block(
        text,
        font_size=font_size,
        color=TEXT_PRIMARY,
        max_chars=max_chars,
        weight=MEDIUM,
    )
    fit_to_width(content, max_width=max_width - 0.7)
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
    return create_text_block(text, font_size=font_size, color=color, max_chars=34)


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


def create_subtle_grid(color=GRID_COLOR, stroke_opacity=0.05, stroke_width=1):
    """Tạo grid mờ làm nền canvas."""
    grid = VGroup()
    # Vertical lines
    for x in range(-7, 8, 2):
        grid.add(
            Line(
                [x, -4.5, 0],
                [x, 4.5, 0],
                color=color,
                stroke_opacity=stroke_opacity,
                stroke_width=stroke_width,
            )
        )
    # Horizontal lines
    for y in range(-4, 5, 1):
        grid.add(
            Line(
                [-7.5, y, 0],
                [7.5, y, 0],
                color=color,
                stroke_opacity=stroke_opacity,
                stroke_width=stroke_width,
            )
        )
    return grid


def setup_dark_scene(scene):
    """Setup dark background cho scene. Gọi ở đầu construct()."""
    scene.camera.background_color = BG_DARK
    # Add persistent subtle grid
    grid = create_subtle_grid(stroke_opacity=0.05)
    scene.add(grid)


def fade_out_all(scene, run_time=TIME_NORMAL):
    """Fade out tất cả objects trên scene."""
    if scene.mobjects:
        scene.play(
            *[FadeOut(mob) for mob in scene.mobjects],
            run_time=run_time
        )


def animate_title_card(scene, title_text, subtitle_text=""):
    """Animate một title card hoàn chỉnh với hiệu ứng hiện đại."""
    card = create_section_title(title_text, subtitle_text)
    
    # Animate card drawing
    scene.play(
        FadeIn(card[0], scale=0.92),  # card_bg
        FadeIn(card[1], scale=0.92),  # card_inner
        Write(card[2]),               # content
        run_time=TIME_NORMAL
    )
    scene.wait(TIME_PAUSE)
    scene.play(FadeOut(card), run_time=TIME_FAST)


def create_subtitle(text, font_size=SIZE_CAPTION, color=TEXT_SECONDARY, max_width=86):
    """
    Tạo subtitle đồng bộ với TV1 caption style.
    """
    return create_bottom_caption(text, font_size=font_size, color=color, max_width=max_width)


def create_bottom_caption(text, font_size=SIZE_CAPTION, color=TEXT_SECONDARY, max_width=86, buff=0.65):
    """Caption đáy giống TV1: không nền, ít chữ, nằm ngoài vùng nội dung chính."""
    caption = create_text_block(
        text,
        font_size=font_size,
        color=color,
        max_chars=max_width,
        line_spacing=0.78,
    )
    fit_to_width(caption, max_width=11.6)
    caption.to_edge(DOWN, buff=buff)
    return caption
