"""
Oort Constants (A, B) and Galactic Differential Rotation.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 24).
"""
import numpy as np

def oort_constants(theta0: float, r0: float, dtheta_dr: float):
    """
    Oort constants for Milky Way disk rotation:
    A = -0.5 * (d Theta / dr - Theta0 / r0)
    B = -0.5 * (d Theta / dr + Theta0 / r0)
    """
    omega0 = theta0 / r0
    A = -0.5 * (dtheta_dr - omega0)
    B = -0.5 * (dtheta_dr + omega0)
    return float(A), float(B)

def radial_velocity_oort(l: float, d: float, A: float) -> float:
    """Line-of-sight radial velocity v_r = A d sin(2 l)."""
    return float(A * d * np.sin(2.0 * l))
