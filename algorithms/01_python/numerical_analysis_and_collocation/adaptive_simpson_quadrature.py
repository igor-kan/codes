"""Adaptive Simpson's Quadrature with Recursive Error Estimation."""
from typing import Callable


def _simpson(f: Callable[[float], float], a: float, b: float) -> float:
    c = 0.5 * (a + b)
    return (b - a) / 6.0 * (f(a) + 4.0 * f(c) + f(b))


def _adaptive_step(f: Callable[[float], float], a: float, b: float,
                   tol: float, whole: float, depth: int) -> float:
    c = 0.5 * (a + b)
    left = _simpson(f, a, c)
    right = _simpson(f, c, b)
    if depth <= 0 or abs(left + right - whole) <= 15.0 * tol:
        return left + right + (left + right - whole) / 15.0
    return (_adaptive_step(f, a, c, tol / 2.0, left, depth - 1) +
            _adaptive_step(f, c, b, tol / 2.0, right, depth - 1))


def adaptive_simpson(f: Callable[[float], float], a: float, b: float, tol: float = 1e-8) -> float:
    """Compute integral of f from a to b to within tolerance."""
    whole = _simpson(f, a, b)
    return _adaptive_step(f, a, b, tol, whole, depth=20)
