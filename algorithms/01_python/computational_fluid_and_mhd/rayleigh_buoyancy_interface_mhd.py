"""Magnetized Rayleigh buoyancy interface Interface Instability.

Heavy fluid (rho_2) on top of light fluid (rho_1) under gravitational acceleration g.
Atwood number: A = (rho_2 - rho_1) / (rho_2 + rho_1).
Magnetic field B parallel to interface provides effective tension:
gamma^2 = A * g * k - (k . B)^2 / (mu_0 * (rho_1 + rho_2)).
"""
import numpy as np

MU_0 = 4.0 * np.pi * 1e-7


def atwood_number(rho1: float, rho2: float) -> float:
    """Atwood number A = (rho2 - rho1) / (rho2 + rho1)."""
    return float((rho2 - rho1) / (rho2 + rho1))


def rayleigh_buoyancy_growth_rate(rho1: float, rho2: float, g: float, k: float, B_parallel: float = 0.0) -> float:
    """Compute interface buoyancy growth rate gamma (returns 0.0 if stabilized)."""
    if rho2 <= rho1:
        return 0.0  # stable density stratification
    
    A = atwood_number(rho1, rho2)
    instab_term = A * g * k
    mag_term = (k * B_parallel)**2 / (MU_0 * (rho1 + rho2))
    diff = instab_term - mag_term
    return float(np.sqrt(diff)) if diff > 0 else 0.0
