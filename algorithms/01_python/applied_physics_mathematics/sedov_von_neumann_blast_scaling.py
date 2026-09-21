"""
Sedov-von Neumann Self-Similar Blast Wave Radius Scaling.
Reference: Zeldovich & Raizer, Physics of Shock Waves; Sedov (1959).
Note: Uses dimensional analysis to derive R(t) = C (E / rho)^(1/5) t^(2/5).
"""
import numpy as np

def blast_radius(time: np.ndarray, energy: float, density: float, xi_0: float = 1.033) -> np.ndarray:
    """
    R(t) = xi_0 * (E / rho)^(1/5) * t^(2/5).
    """
    return xi_0 * ((energy / density)**0.2) * (time**0.4)
