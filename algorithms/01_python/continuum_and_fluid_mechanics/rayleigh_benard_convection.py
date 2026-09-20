"""
Rayleigh-Bénard Thermal Convection and Critical Rayleigh Number.
References: Landau & Lifshitz - Fluid Mechanics.
"""
import numpy as np

def rayleigh_number(g: float, alpha_thermal: float, delta_T: float, d: float, nu: float, kappa: float) -> float:
    """Rayleigh number Ra = g alpha Delta T d^3 / (nu kappa)."""
    return float(g * alpha_thermal * delta_T * (d**3) / (nu * kappa))

def is_convection_unstable(Ra: float, Ra_critical: float = 1708.0) -> bool:
    """Rigid-rigid boundary critical Rayleigh number is approx 1708."""
    return Ra > Ra_critical
