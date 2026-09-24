"""Spherical Harmonics Evaluation Y_l^m(theta, phi)."""
import numpy as np
from scipy.special import sph_harm


def evaluate_spherical_harmonic(l: int, m: int, theta: np.ndarray, phi: np.ndarray) -> np.ndarray:
    """Evaluate Y_l^m."""
    return sph_harm(m, l, phi, theta)
