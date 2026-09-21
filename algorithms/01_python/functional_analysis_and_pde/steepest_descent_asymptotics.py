"""
Method of Steepest Descent / Saddle-Point Method for Asymptotics of Integrals.
Reference: Hassani, Mathematical Methods for Physics, Ch. 12; Blennow, Ch. 8.
"""
import numpy as np

def saddle_point_laplace(f_saddle: float, f_double_prime: float, k: float) -> float:
    """
    Evaluates asymptotic integral I(k) = int exp(k f(z)) dz as k -> infty:
    I(k) approx sqrt(2 pi / (k |f''(z_0)|)) exp(k f(z_0)).
    Assumes f''(z_0) < 0 along path of steepest descent.
    """
    if f_double_prime >= 0:
        raise ValueError("f''(z_0) must be negative along the path of steepest descent.")
    prefactor = np.sqrt(2.0 * np.pi / (k * abs(f_double_prime)))
    return float(prefactor * np.exp(k * f_saddle))
