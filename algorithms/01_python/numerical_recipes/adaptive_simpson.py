"""
Adaptive Simpson's Quadrature with Recursive Error Control.
References: Kincaid & Cheney - Numerical Analysis (Ch. 7).
"""
import numpy as np

def _simpson_rule(f, a, b):
    c = 0.5 * (a + b)
    return (b - a) / 6.0 * (f(a) + 4.0 * f(c) + f(b))

def _adaptive_simpson_rec(f, a, b, eps, s_whole):
    c = 0.5 * (a + b)
    s_left = _simpson_rule(f, a, c)
    s_right = _simpson_rule(f, c, b)
    s_both = s_left + s_right
    if abs(s_both - s_whole) <= 15.0 * eps:
        return s_both + (s_both - s_whole) / 15.0
    return (
        _adaptive_simpson_rec(f, a, c, 0.5 * eps, s_left) +
        _adaptive_simpson_rec(f, c, b, 0.5 * eps, s_right)
    )

def adaptive_simpson(f, a: float, b: float, tol: float = 1e-8) -> float:
    """Adaptive Simpson quadrature on [a, b]."""
    s_init = _simpson_rule(f, a, b)
    return float(_adaptive_simpson_rec(f, a, b, tol, s_init))
