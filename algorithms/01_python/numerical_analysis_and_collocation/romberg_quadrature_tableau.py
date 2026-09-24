"""Romberg Quadrature via Richardson Extrapolation on Trapezoidal Rule."""
import numpy as np
from typing import Callable


def romberg_quadrature(f: Callable[[float], float], a: float, b: float, max_steps: int = 8) -> float:
    """Compute definite integral of f on [a, b] using Romberg tableau."""
    R = np.zeros((max_steps, max_steps))
    h = b - a
    R[0, 0] = 0.5 * h * (f(a) + f(b))
    
    for i in range(1, max_steps):
        h /= 2.0
        n_sub = 2 ** (i - 1)
        pts = a + (2 * np.arange(1, n_sub + 1) - 1) * h
        R[i, 0] = 0.5 * R[i - 1, 0] + h * np.sum([f(p) for p in pts])
        for j in range(1, i + 1):
            R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4.0**j - 1.0)
            
    return float(R[max_steps - 1, max_steps - 1])
