"""
Stirling's Asymptotic Power Series for ln Gamma(z) with Bernoulli Numbers.
Reference: Mauch, Intro to Applied Mathematics, Ch. 27.
"""
import numpy as np

def stirling_ln_gamma(z: float) -> float:
    """
    ln Gamma(z) approx (z - 1/2) ln(z) - z + 1/2 ln(2 pi) + 1/(12 z) - 1/(360 z^3).
    """
    return float((z - 0.5) * np.log(z) - z + 0.5 * np.log(2.0 * np.pi) + 1.0 / (12.0 * z) - 1.0 / (360.0 * z**3))
