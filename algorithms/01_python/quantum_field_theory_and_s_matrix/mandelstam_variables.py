"""Mandelstam Variables for Relativistic 2-to-2 Scattering Kinematics.

Calculates s, t, u invariants and center-of-mass frame kinematics:
p1 + p2 -> p3 + p4.
Invariance: s + t + u = m1^2 + m2^2 + m3^2 + m4^2.
"""
import numpy as np
from typing import Dict, Tuple
from feynman_slash import minkowski_dot


def calculate_mandelstam(p1: np.ndarray, p2: np.ndarray, p3: np.ndarray, p4: np.ndarray) -> Dict[str, float]:
    """Calculate s = (p1+p2)^2, t = (p1-p3)^2, u = (p1-p4)^2."""
    s = minkowski_dot(p1 + p2, p1 + p2)
    t = minkowski_dot(p1 - p3, p1 - p3)
    u = minkowski_dot(p1 - p4, p1 - p4)
    return {"s": s, "t": t, "u": u}


def verify_mandelstam_sum(s: float, t: float, u: float, masses: Tuple[float, float, float, float]) -> bool:
    """Verify s + t + u = sum(m_i^2)."""
    sum_m2 = sum(m**2 for m in masses)
    return np.isclose(s + t + u, sum_m2, atol=1e-8)


def cm_scattering_angles(s: float, m: float, theta: float) -> Tuple[float, float]:
    """Calculate t and u for elastic scattering of identical mass m at scattering angle theta."""
    if s < 4.0 * m**2:
        raise ValueError("Center of mass energy squared s is below threshold 4*m^2")
    p_cm_sq = 0.25 * s - m**2
    t = -2.0 * p_cm_sq * (1.0 - np.cos(theta))
    u = -2.0 * p_cm_sq * (1.0 + np.cos(theta))
    return t, u
