"""
Method of Dominant Balance for Singularly Perturbed Algebraic Equations:
eps x^3 + x - 1 = 0.
Reference: Mauch, Intro to Applied Mathematics, Ch. 28.
"""
import numpy as np
from typing import Tuple

def dominant_balance_cubic(eps: float) -> Tuple[float, float, float]:
    """
    One regular root: x_0 approx 1.
    Two singular boundary roots: eps x^3 + x approx 0 -> x_{1, 2} approx +- i / sqrt(eps).
    """
    r_reg = 1.0 - eps
    r_sing_imag = 1.0 / np.sqrt(eps)
    return r_reg, r_sing_imag, -r_sing_imag
