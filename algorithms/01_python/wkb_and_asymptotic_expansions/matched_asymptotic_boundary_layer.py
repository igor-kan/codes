"""Matched Asymptotic Boundary Layer Expansion (Outer + Inner Solution).

eps * y'' + y' = 1, y(0) = 0, y(1) = 1.
"""
import numpy as np


def matched_composite_solution(x: np.ndarray, eps: float) -> np.ndarray:
    """Composite leading-order matched solution y_comp = x + (1 - exp(-x / eps))."""
    # Outer: y = x, Inner: y = 1 - exp(-X)
    return x - np.exp(-x / eps)
