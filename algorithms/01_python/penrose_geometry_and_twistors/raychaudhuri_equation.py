"""
Raychaudhuri Equation for expansion of null and timelike geodesic congruences.
Reference: Penrose, The Road to Reality, Ch. 27 & 28.
"""
import numpy as np

def raychaudhuri_null_derivative(theta: float, shear_sq: float, twist_sq: float, ricci_null_contraction: float) -> float:
    """
    d theta / d lambda = - 1/2 theta^2 - 2 sigma^2 + 2 omega^2 - R_{mu nu} k^mu k^nu.
    Predicts caustic / conjugate point formation when null energy condition holds (R_{mu nu} k^mu k^nu >= 0) and twist is zero.
    """
    dtheta = -0.5 * (theta**2) - 2.0 * shear_sq + 2.0 * twist_sq - ricci_null_contraction
    return float(dtheta)
