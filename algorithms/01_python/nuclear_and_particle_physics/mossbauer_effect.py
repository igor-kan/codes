"""
Mössbauer Effect Recoilless Gamma Emission Fraction.
References: Kenneth S. Krane - Modern Physics.
"""
import numpy as np

def mossbauer_recoil_energy(E_gamma_keV: float, mass_amu: float) -> float:
    """Nuclear recoil energy E_R = E_gamma^2 / (2 M c^2) in eV."""
    M_c2_keV = mass_amu * 931494.0
    return float((E_gamma_keV**2 / (2.0 * M_c2_keV)) * 1000.0)
