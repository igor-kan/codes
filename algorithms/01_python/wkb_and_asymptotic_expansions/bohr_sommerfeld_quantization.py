"""Bohr-Sommerfeld Semiclassical WKB Action Quantization Integral."""
import numpy as np


def bohr_sommerfeld_action(E: float, V_fn, x_left: float, x_right: float, mass: float = 1.0) -> float:
    """Action integral J = int_{x_1}^{x_2} sqrt(2 * m * (E - V(x))) dx."""
    pts = np.linspace(x_left, x_right, 1000)
    dx = pts[1] - pts[0]
    p_sq = 2.0 * mass * (E - V_fn(pts))
    p_sq = np.maximum(p_sq, 0.0)
    p = np.sqrt(p_sq)
    return float(np.sum(p) * dx)
