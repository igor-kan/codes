"""
Kovalevskaya Top Dynamics and Invariant of Motion.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def kovalevskaya_invariant(w1: float, w2: float, gamma1: float, gamma2: float, c: float = 1.0) -> float:
    """
    Kovalevskaya 4th conserved quantity K = |(w1 + i w2)^2 - c (gamma1 + i gamma2)|^2
    = (w1^2 - w2^2 - c gamma1)^2 + (2 w1 w2 - c gamma2)^2.
    """
    term1 = w1**2 - w2**2 - c * gamma1
    term2 = 2.0 * w1 * w2 - c * gamma2
    return float(term1**2 + term2**2)
