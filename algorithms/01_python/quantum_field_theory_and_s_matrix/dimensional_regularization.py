"""Dimensional Regularization (D = 4 - 2*epsilon) and Pole Subtraction.

MS (Minimal Subtraction) and MS-bar (Modified Minimal Subtraction) schemes.
"""
import numpy as np
from scipy.special import gamma


def gamma_epsilon_pole(epsilon: float) -> float:
    """Evaluate Laurent series expansion of Gamma(epsilon) = 1/epsilon - gamma_E + O(epsilon)."""
    euler_mascheroni = 0.5772156649015328606
    return float(1.0 / epsilon - euler_mascheroni)


def ms_bar_scale_factor(mu_sq: float, epsilon: float) -> float:
    """MS-bar renormalization scale factor: (4 * pi * e^(-gamma_E))^epsilon * mu^2."""
    euler_mascheroni = 0.5772156649015328606
    factor = (4.0 * np.pi * np.exp(-euler_mascheroni))**epsilon
    return float(factor * mu_sq)
