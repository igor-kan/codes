"""Dirac Propagator for Spin-1/2 Fermions.

S_F(p) = (slash(p) + m) / (p^2 - m^2 + i*epsilon).
"""
import numpy as np
from feynman_slash import feynman_slash, minkowski_dot


def dirac_propagator_momentum(p: np.ndarray, m: float, epsilon: float = 1e-6) -> np.ndarray:
    """Compute 4x4 matrix Dirac Feynman propagator in momentum space."""
    p_slash = feynman_slash(p)
    p_sq = minkowski_dot(p, p)
    scalar_denom = p_sq - m**2 + 1j * epsilon
    numerator = p_slash + m * np.eye(4, dtype=complex)
    return numerator / scalar_denom


def energy_projection_operators(p: np.ndarray, m: float) -> tuple:
    """Projection operators for positive and negative energy states: Lambda_plus, Lambda_minus."""
    p_slash = feynman_slash(p)
    I4 = np.eye(4, dtype=complex)
    lambda_plus = (p_slash + m * I4) / (2.0 * m)
    lambda_minus = (-p_slash + m * I4) / (2.0 * m)
    return lambda_plus, lambda_minus
