"""
Theme Constants — 3Blue1Brown Style
Dùng chung cho tất cả scenes trong dự án.
Import: from utils.theme import *
"""

# ============================================================
# COLORS
# ============================================================

# Background
BG_DARK = "#1a1a2e"
BG_DARKER = "#16162a"

# Primary
THEME_BLUE = "#3b82f6"
THEME_BLUE_LIGHT = "#60a5fa"

# Secondary
THEME_AMBER = "#f59e0b"
THEME_AMBER_LIGHT = "#fbbf24"

# Accent
THEME_EMERALD = "#10b981"
THEME_RED = "#ef4444"
THEME_PURPLE = "#8b5cf6"
THEME_PINK = "#ec4899"
THEME_ORANGE = "#f97316"

# Text
TEXT_PRIMARY = "#e2e8f0"
TEXT_SECONDARY = "#94a3b8"
TEXT_MUTED = "#64748b"

# Utility
GRID_COLOR = "#2a2a4a"

# Environment colors (dùng cho data visualization)
ENV_COLORS = [THEME_BLUE, THEME_AMBER, THEME_ORANGE]
ENV_NAMES = ["Environment 1", "Environment 2", "Environment 3"]

# ============================================================
# FONTS
# ============================================================

FONT_PRIMARY = "Inter"
FONT_CODE = "JetBrains Mono"

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
