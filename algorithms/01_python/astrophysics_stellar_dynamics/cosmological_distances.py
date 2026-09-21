"""
Comoving, Luminosity, and Angular Diameter Distances.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 29).
"""
import numpy as np
from scipy.integrate import quad
from friedmann_cosmology import hubble_parameter_z

def luminosity_distance(z: float, H0: float = 70.0, Om_m: float = 0.3, Om_l: float = 0.7) -> float:
    """Luminosity distance d_L(z) = (1+z) * c * int_0^z dz' / H(z')."""
    c = 299792.458  # km/s
    integrand = lambda zp: 1.0 / hubble_parameter_z(zp, H0, Om_m, 0.0, Om_l)
    dc, _ = quad(integrand, 0.0, z)
    return float((1.0 + z) * c * dc)
