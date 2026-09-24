"""Kronig-Penney Model for Electronic Band Gaps in Periodic Potentials.

Dispersion relation: cos(k * a) = cos(alpha * a) + P * sin(alpha * a) / (alpha * a).
"""
import numpy as np


def kronig_penney_dispersion(alpha_a: np.ndarray, P_barrier_strength: float) -> np.ndarray:
    """Evaluate Kronig-Penney RHS f(alpha * a). Electronic band if |f| <= 1."""
    return np.cos(alpha_a) + P_barrier_strength * np.sin(alpha_a) / alpha_a


def is_allowed_band(alpha_a: float, P: float) -> bool:
    """Check if state alpha*a falls inside an allowed energy band."""
    val = np.cos(alpha_a) + P * np.sin(alpha_a) / alpha_a
    return bool(abs(val) <= 1.0)
