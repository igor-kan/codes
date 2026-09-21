"""
Hankel's Asymptotic Expansion for Bessel Function J_0(x) as x -> infty.
Reference: Chow, Mathematical Methods for Physicists, Ch. 10.
"""
import numpy as np

def bessel_j0_asymptotic(x: float) -> float:
    """
    J_0(x) approx sqrt(2 / (pi x)) * cos(x - pi / 4).
    """
    return float(np.sqrt(2.0 / (np.pi * x)) * np.cos(x - np.pi / 4.0))
