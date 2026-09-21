"""
Friedmann Equation and Cosmological Scale Factor.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 29).
"""
import numpy as np

def hubble_parameter_z(z: float, H0: float = 70.0, Om_m: float = 0.3, Om_r: float = 1e-4, Om_lambda: float = 0.7) -> float:
    """H(z) = H0 sqrt(Om_r (1+z)^4 + Om_m (1+z)^3 + Om_lambda)."""
    e_sq = Om_r * (1.0 + z)**4 + Om_m * (1.0 + z)**3 + Om_lambda
    return float(H0 * np.sqrt(e_sq))
