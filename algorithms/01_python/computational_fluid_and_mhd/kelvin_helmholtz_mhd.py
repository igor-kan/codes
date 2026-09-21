"""Magnetized Kelvin-Helmholtz Shear Instability.

Shear interface between fluid 1 (rho_1, U_1) and fluid 2 (rho_2, U_2) with background field B.
Magnetic field parallel to flow stabilizes short wavelengths:
Stable if: (k . B)^2 / mu_0 >= (rho_1 * rho_2 / (rho_1 + rho_2)) * (k . delta_U)^2.
"""
import numpy as np

MU_0 = 4.0 * np.pi * 1e-7


def is_kh_stable_mhd(rho1: float, rho2: float, delta_u: float, B_parallel: float) -> bool:
    """Determine whether parallel magnetic field stabilizes the shear flow."""
    lhs = (B_parallel**2) / MU_0
    rhs = (rho1 * rho2 / (rho1 + rho2)) * (delta_u**2)
    return bool(lhs >= rhs)


def kh_growth_rate_unmagnetized(rho1: float, rho2: float, delta_u: float, k: float) -> float:
    """Growth rate in absence of magnetic field: gamma = k * delta_u * sqrt(rho1 * rho2) / (rho1 + rho2)."""
    return float(k * delta_u * np.sqrt(rho1 * rho2) / (rho1 + rho2))
