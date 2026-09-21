"""
Pade Approximant [1/1] from Power Series Coefficients c0 + c1 x + c2 x^2:
R_{1,1}(x) = (a0 + a1 x) / (1 + b1 x).
Reference: Mauch, Intro to Applied Mathematics; Baker, Pade Approximants.
"""
import numpy as np
from typing import Tuple

def pade_11_coefficients(c0: float, c1: float, c2: float) -> Tuple[float, float, float]:
    """
    b1 = - c2 / c1
    a0 = c0
    a1 = c1 + b1 c0
    """
    if c1 == 0.0:
        raise ValueError("c1 must be non-zero for [1/1] Pade approximant.")
    b1 = -c2 / c1
    a0 = c0
    a1 = c1 + b1 * c0
    return a0, a1, b1

def eval_pade_11(x: float, a0: float, a1: float, b1: float) -> float:
    return float((a0 + a1 * x) / (1.0 + b1 * x))
