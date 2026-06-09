"""
Theme Constants — 3Blue1Brown-inspired style.

The upstream 3b1b/videos repo uses 3b1b's own manim variant. This project uses
Manim Community, so these constants capture the visual language rather than
copying that framework: black background, serif text, saturated accents, and
thin geometric marks.
"""

import os
from pathlib import Path


HOMEBREW_TEXLIVE = Path("/opt/homebrew/opt/texlive/share")
if HOMEBREW_TEXLIVE.exists():
    os.environ.setdefault("TEXMFROOT", str(HOMEBREW_TEXLIVE))
    os.environ.setdefault("TEXMFCNF", str(HOMEBREW_TEXLIVE / "texmf-dist" / "web2c"))

# ============================================================
# COLORS
# ============================================================

# Background
BG_DARK = "#0A0E17"       # Premium dark navy blue
BG_DARKER = "#05070A"     # Deep navy blue
BG_PANEL = "#111827"      # Slate navy

# Primary 3B1B-like accents
THEME_BLUE = "#58C4DD"
THEME_BLUE_LIGHT = "#7FDBFF"

# Secondary
THEME_AMBER = "#FFFF00"
THEME_AMBER_LIGHT = "#FFF46B"

# Accent
THEME_EMERALD = "#83C167"
THEME_RED = "#FC6255"
THEME_RED_LIGHT = "#FF9A92"
THEME_PURPLE = "#9A72AC"
THEME_PURPLE_LIGHT = "#C3A6D4"
THEME_PINK = "#FF8080"
THEME_ORANGE = "#FF862F"

# Text
TEXT_PRIMARY = "#F5F5F5"
TEXT_SECONDARY = "#C9C9C9"
TEXT_MUTED = "#888888"

# Utility
GRID_COLOR = "#222222"

# Environment colors (dùng cho data visualization)
ENV_COLORS = [THEME_BLUE, THEME_AMBER, THEME_ORANGE]
ENV_NAMES = ["Environment 1", "Environment 2", "Environment 3"]

# ============================================================
# FONTS
# ============================================================

FONT_PRIMARY = "Segoe UI"
FONT_CODE = "Menlo"

# ============================================================
# FONT SIZES
# ============================================================

SIZE_TITLE = 56
SIZE_SECTION = 44
SIZE_SUBSECTION = 36
SIZE_BODY = 28
SIZE_CAPTION = 24
SIZE_SMALL = 20
SIZE_FORMULA = 42

# ============================================================
# TIMING (seconds)
# ============================================================

TIME_FAST = 0.5
TIME_NORMAL = 1.0
TIME_SLOW = 2.0
TIME_PAUSE = 1.5
TIME_LONG_PAUSE = 3.0

# ============================================================
# SPACING (Manim units)
# ============================================================

GAP_SECTION = 1.0
GAP_ITEM = 0.5
GAP_LABEL = 0.3
EDGE_BUFFER = 0.5
