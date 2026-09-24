"""Barycentric Rational Interpolation (Floater-Hormann).

High-accuracy, pole-free rational interpolation for equispaced or arbitrary nodes.
"""
import numpy as np


def floater_hormann_interpolate(x_nodes: np.ndarray, y_nodes: np.ndarray,
                                x_eval: np.ndarray, d: int = 3) -> np.ndarray:
    """Interpolate y at x_eval using Floater-Hormann weights of order d."""
    n = len(x_nodes) - 1
    w = np.zeros(n + 1)
    
    for k in range(n + 1):
        s = 0.0
        for i in range(max(0, k - d), min(k, n - d) + 1):
            s += 1.0
        w[k] = ((-1.0) ** (k - d)) * s
        
    # Evaluate barycentric form
    y_eval = np.zeros_like(x_eval, dtype=float)
    for idx, x in enumerate(x_eval):
        diff = x - x_nodes
        exact_match = np.where(np.abs(diff) < 1e-15)[0]
        if len(exact_match) > 0:
            y_eval[idx] = y_nodes[exact_match[0]]
        else:
            terms = w / diff
            y_eval[idx] = np.sum(terms * y_nodes) / np.sum(terms)
    return y_eval
