"""Ideal Magnetohydrodynamic (MHD) Wave Speeds and Dispersion Relations.

Calculates:
- Alfven speed: v_A = B_0 / sqrt(mu_0 * rho_0)
- Sound speed: c_s = sqrt(gamma * P_0 / rho_0)
- Fast and slow magnetosonic speeds:
  v^4 - (c_s^2 + v_A^2) v^2 + c_s^2 v_A^2 cos^2(theta) = 0.
"""
import numpy as np
from typing import Tuple

MU_0 = 4.0 * np.pi * 1e-7  # Vacuum permeability (H/m)


def alfven_speed(B0: float, rho0: float) -> float:
    """Compute Alfven speed v_A = B0 / sqrt(mu0 * rho0)."""
    if rho0 <= 0 or B0 < 0:
        raise ValueError("Density must be positive and B0 non-negative")
    return float(B0 / np.sqrt(MU_0 * rho0))


def sound_speed(gamma: float, P0: float, rho0: float) -> float:
    """Compute adiabatic sound speed c_s = sqrt(gamma * P0 / rho0)."""
    return float(np.sqrt(gamma * P0 / rho0))


def magnetosonic_speeds(B0: float, rho0: float, P0: float, gamma: float, theta: float) -> Tuple[float, float, float]:
    """Calculate (v_fast, v_alfven, v_slow) at angle theta relative to background field B0."""
    v_a = alfven_speed(B0, rho0)
    c_s = sound_speed(gamma, P0, rho0)
    
    cos_th = np.cos(theta)
    b_term = c_s**2 + v_a**2
    c_term = c_s**2 * v_a**2 * (cos_th**2)
    disc = np.sqrt(max(0.0, b_term**2 - 4.0 * c_term))

    v_fast = np.sqrt(0.5 * (b_term + disc))
    v_slow = np.sqrt(0.5 * (b_term - disc))
    v_intermediate = v_a * abs(cos_th)

    return float(v_fast), float(v_intermediate), float(v_slow)
