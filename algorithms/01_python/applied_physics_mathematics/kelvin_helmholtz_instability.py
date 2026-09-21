"""
Kelvin-Helmholtz Hydrodynamic Shear Instability Dispersion Relation.
Reference: Zeldovich; Chandrasekhar, Hydrodynamic and Hydromagnetic Stability.
"""
import numpy as np

def kh_growth_rate(k: float, rho1: float, rho2: float, U1: float, U2: float) -> float:
    """
    Im(omega) = k * sqrt(rho1 * rho2) * |U1 - U2| / (rho1 + rho2).
    """
    growth = k * np.sqrt(rho1 * rho2) * abs(U1 - U2) / (rho1 + rho2)
    return float(growth)
