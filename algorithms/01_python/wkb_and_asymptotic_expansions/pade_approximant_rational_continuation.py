"""Pade Rational Approximant for Analytic Continuation of Power Series."""
import numpy as np


def pade_11_approximant(c0: float, c1: float, c2: float, x: np.ndarray) -> np.ndarray:
    """[1/1] Pade approximant R(x) = (a0 + a1 * x) / (1 + b1 * x) from series c0 + c1*x + c2*x^2."""
    b1 = -c2 / c1
    a0 = c0
    a1 = c1 + c0 * b1
    return (a0 + a1 * x) / (1.0 + b1 * x)
