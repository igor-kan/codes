"""Method of Steepest Descent for Saddle Point Asymptotic Integrals."""
import numpy as np


def saddle_point_gaussian_integral(f0: float, f_double_prime: float, lam: float) -> float:
    """Evaluate leading order asymptotic I(lambda) approx exp(lambda * f0) * sqrt(2 * pi / (lambda * |f''(z0)|))."""
    if f_double_prime <= 0 or lam <= 0:
        raise ValueError("Curvature and lambda must be positive for saddle minimum")
    return float(np.exp(lam * f0) * np.sqrt(2.0 * np.pi / (lam * f_double_prime)))
