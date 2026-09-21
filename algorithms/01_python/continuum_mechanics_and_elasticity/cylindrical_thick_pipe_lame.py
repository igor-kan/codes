"""Lamé Solution for Thick-Walled Cylindrical Pressure Vessels.

Radial stress sigma_r(r) and hoop (tangential) stress sigma_theta(r)
under internal pressure P_i at r = a and external pressure P_o at r = b:
sigma_r(r) = (P_i a^2 - P_o b^2)/(b^2 - a^2) - (P_i - P_o) a^2 b^2 / (r^2 (b^2 - a^2))
sigma_th(r) = (P_i a^2 - P_o b^2)/(b^2 - a^2) + (P_i - P_o) a^2 b^2 / (r^2 (b^2 - a^2)).
"""
import numpy as np
from typing import Tuple


def lame_cylinder_stresses(a: float, b: float, Pi: float, Po: float, r: float) -> Tuple[float, float]:
    """Calculate radial and hoop stress at radius r, where a <= r <= b."""
    if r < a or r > b:
        raise ValueError("Radius r must be between inner radius a and outer radius b")
    
    A = (Pi * a**2 - Po * b**2) / (b**2 - a**2)
    B = (Pi - Po) * (a**2) * (b**2) / (b**2 - a**2)
    
    sigma_r = A - B / (r**2)
    sigma_theta = A + B / (r**2)
    return float(sigma_r), float(sigma_theta)
