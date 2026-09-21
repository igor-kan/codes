"""
Eddington Critical Radiation Luminosity.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 10).
"""
import numpy as np

def eddington_luminosity(mass_solar: float) -> float:
    """L_Edd = 4 pi G M c / kappa_es approx 1.26e31 * (M / M_sun) Watts."""
    return float(1.26e31 * mass_solar)
