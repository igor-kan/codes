"""
Kelvin-Helmholtz Sheared Interface Growth Rate.
References: Landau & Lifshitz - Fluid Mechanics.
"""
import numpy as np

def kh_growth_rate(k: float, rho1: float, rho2: float, U1: float, U2: float) -> float:
    """Growth rate sigma = k |U1 - U2| sqrt(rho1 rho2) / (rho1 + rho2)."""
    return float(k * abs(U1 - U2) * np.sqrt(rho1 * rho2) / (rho1 + rho2))
