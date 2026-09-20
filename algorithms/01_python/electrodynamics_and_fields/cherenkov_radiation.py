"""
Cherenkov Radiation Angle and Frank-Tamm Formula.
References: Landau & Lifshitz - Electrodynamics of Continuous Media (Vol. 8).
"""
import numpy as np

def cherenkov_angle(beta: float, n_refractive: float) -> float:
    """Cherenkov emission cone angle cos(theta) = 1 / (beta * n). Returns angle in radians or None if sub-threshold."""
    if beta * n_refractive <= 1.0:
        return 0.0
    return float(np.arccos(1.0 / (beta * n_refractive)))

def frank_tamm_power_density(omega: float, beta: float, n_refractive: float, q: float = 1.0, c: float = 1.0) -> float:
    """Frank-Tamm spectral energy output per unit length d^2W / (dx domega) = (q^2 / (4 pi eps0 c^2)) omega (1 - 1/(beta^2 n^2))."""
    if beta * n_refractive <= 1.0:
        return 0.0
    return float((q**2 / (4.0 * np.pi * c**2)) * omega * (1.0 - 1.0 / (beta**2 * n_refractive**2)))
