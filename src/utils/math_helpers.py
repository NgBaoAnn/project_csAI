"""
Math Helpers — Utility functions cho math animations.
Import: from utils.math_helpers import *
"""

import numpy as np
from manim import *
from utils.theme import *


def generate_cluster(center, n_points=30, std=0.8, seed=None):
    """
    Tạo cluster data points dạng Gaussian.
    
    Args:
        center: (x, y) tuple — tâm cluster
        n_points: số điểm
        std: standard deviation
        seed: random seed (cho reproducibility)
    
    Returns:
        List of (x, y) tuples
    """
    if seed is not None:
        np.random.seed(seed)
    
    x_coords = np.random.normal(loc=center[0], scale=std, size=n_points)
    y_coords = np.random.normal(loc=center[1], scale=std, size=n_points)
    
    return list(zip(x_coords, y_coords))


def create_data_cloud(center, n_points=30, std=0.8, color=THEME_BLUE,
                       radius=0.06, seed=None):
    """
    Tạo VGroup chứa data point dots tạo thành cloud.
    
    Returns:
        VGroup of Dot objects
    """
    points = generate_cluster(center, n_points, std, seed)
    dots = [
        Dot(point=[x, y, 0], color=color, radius=radius)
        for x, y in points
    ]
    return VGroup(*dots)


def animate_data_cloud_in(scene, cloud, lag_ratio=0.05, run_time=2.0):
    """Animate data cloud xuất hiện với staggered effect."""
    scene.play(
        LaggedStart(
            *[FadeIn(d, scale=0.5) for d in cloud],
            lag_ratio=lag_ratio
        ),
        run_time=run_time
    )


def create_decision_boundary(axes, slope, intercept, color=THEME_PURPLE,
                              stroke_width=3):
    """
    Tạo decision boundary line trên axes.
    y = slope * x + intercept
    """
    x_min = axes.x_range[0]
    x_max = axes.x_range[1]
    
    line = axes.plot(
        lambda x: slope * x + intercept,
        x_range=[x_min, x_max],
        color=color,
        stroke_width=stroke_width
    )
    return line


def create_accuracy_counter(initial=95, font_size=48, color=THEME_EMERALD):
    """
    Tạo animated accuracy counter.
    Dùng DecimalNumber để animate giá trị.
    """
    counter = DecimalNumber(
        initial,
        num_decimal_places=1,
        font_size=font_size,
        color=color
    )
    percent = Text("%", font_size=font_size, color=color)
    percent.next_to(counter, RIGHT, buff=0.1)
    
    return VGroup(counter, percent)


def create_loss_landscape_2d(axes, func=None, color=THEME_BLUE):
    """
    Tạo 2D loss landscape trên axes.
    Default: simple quadratic.
    """
    if func is None:
        func = lambda x: 0.5 * (x - 1) ** 2 + 0.3 * np.sin(3 * x) + 1
    
    graph = axes.plot(func, color=color, stroke_width=3)
    return graph


def create_causal_graph(nodes, edges, node_colors=None):
    """
    Tạo causal graph (DAG) đơn giản.
    
    Args:
        nodes: dict {label: position} — e.g., {"X": LEFT, "Y": RIGHT, "Z": UP}
        edges: list of (from_label, to_label) tuples
        node_colors: dict {label: color} — optional
    
    Returns:
        VGroup chứa nodes và edges
    """
    if node_colors is None:
        node_colors = {}
    
    all_objects = VGroup()
    node_objects = {}
    
    # Create nodes
    for label, pos in nodes.items():
        color = node_colors.get(label, THEME_BLUE)
        circle = Circle(radius=0.4, color=color, fill_opacity=0.2)
        text = Text(label, font_size=SIZE_CAPTION, color=TEXT_PRIMARY)
        node = VGroup(circle, text).move_to(pos)
        node_objects[label] = node
        all_objects.add(node)
    
    # Create edges
    for from_label, to_label in edges:
        from_node = node_objects[from_label]
        to_node = node_objects[to_label]
        arrow = Arrow(
            from_node.get_center(),
            to_node.get_center(),
            color=TEXT_MUTED,
            buff=0.45,
            stroke_width=2
        )
        all_objects.add(arrow)
    
    return all_objects
