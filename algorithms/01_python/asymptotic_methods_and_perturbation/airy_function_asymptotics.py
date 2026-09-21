"""
Asymptotic Expansions of the Airy Function Ai(x) for Large Arguments.
Reference: Mauch, Intro to Applied Mathematics, Ch. 27; Abramowitz & Stegun.
"""
import numpy as np

def airy_ai_positive_asymptotics(x: float) -> float:
    """
    Ai(x) approx (1 / (2 sqrt(pi) x^{1/4})) exp( - 2/3 x^{3/2} ) for x >> 1.
    """
    if x <= 0:
        raise ValueError("Valid for positive x >> 1.")
    prefactor = 1.0 / (2.0 * np.sqrt(np.pi) * (x**0.25))
    return float(prefactor * np.exp(- (2.0 / 3.0) * (x**1.5)))
