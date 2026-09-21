"""Fresnel Reflection and Transmission Coefficients for TE and TM Polarization.

Brewster's angle: tan(theta_B) = n2 / n1.
Critical angle for total internal reflection: sin(theta_c) = n2 / n1 (when n1 > n2).
"""
import numpy as np
from typing import Dict


def brewster_angle(n1: float, n2: float) -> float:
    """Brewster's angle in radians where TM reflection vanishes."""
    return float(np.arctan(n2 / n1))


def critical_angle(n1: float, n2: float) -> float:
    """Critical angle for total internal reflection (n1 > n2)."""
    if n1 <= n2:
        raise ValueError("Total internal reflection requires n1 > n2")
    return float(np.arcsin(n2 / n1))


def fresnel_amplitudes(theta_i: float, n1: float, n2: float) -> Dict[str, complex]:
    """Calculate field reflection and transmission coefficients (r_s, r_p, t_s, t_p)."""
    sin_ti_sq = (n1 / n2 * np.sin(theta_i))**2
    cos_ti = np.cos(theta_i)
    cos_tt = np.sqrt(1.0 - sin_ti_sq + 0j)

    # TE (s-polarized)
    r_s = (n1 * cos_ti - n2 * cos_tt) / (n1 * cos_ti + n2 * cos_tt)
    t_s = (2.0 * n1 * cos_ti) / (n1 * cos_ti + n2 * cos_tt)

    # TM (p-polarized)
    r_p = (n2 * cos_ti - n1 * cos_tt) / (n2 * cos_ti + n1 * cos_tt)
    t_p = (2.0 * n1 * cos_ti) / (n2 * cos_ti + n1 * cos_tt)

    return {"r_s": r_s, "r_p": r_p, "t_s": t_s, "t_p": t_p}
