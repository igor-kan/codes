"""Rayleigh Surface Acoustic Waves in Elastic Half-Space.

Secular equation for Rayleigh wave speed c_R:
eta^3 - 8 eta^2 + (24 - 16 xi^2) eta + 16 (xi^2 - 1) = 0,
where eta = (c_R / c_T)^2 and xi = c_T / c_L = sqrt((1 - 2*nu) / (2*(1 - nu))).
Reference: Landau & Lifshitz Vol 7 (Theory of Elasticity).
"""
import numpy as np
from scipy.optimize import brentq


def wave_speeds(E: float, nu: float, rho: float) -> tuple:
    """Calculate bulk longitudinal (P) and transverse shear (S) wave speeds c_L, c_T."""
    c_T = np.sqrt(E / (2.0 * rho * (1.0 + nu)))
    c_L = np.sqrt(E * (1.0 - nu) / (rho * (1.0 + nu) * (1.0 - 2.0 * nu)))
    return c_L, c_T


def rayleigh_wave_speed(E: float, nu: float, rho: float) -> float:
    """Solve the Rayleigh cubic equation for surface wave speed c_R."""
    c_L, c_T = wave_speeds(E, nu, rho)
    xi_sq = (1.0 - 2.0 * nu) / (2.0 * (1.0 - nu))

    def rayleigh_poly(eta):
        return eta**3 - 8.0 * eta**2 + (24.0 - 16.0 * xi_sq) * eta + 16.0 * (xi_sq - 1.0)

    # Rayleigh root eta is in (0, 1)
    eta_root = brentq(rayleigh_poly, 0.01, 0.99)
    return float(c_T * np.sqrt(eta_root))
