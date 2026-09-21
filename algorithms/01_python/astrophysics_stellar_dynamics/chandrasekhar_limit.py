"""
Chandrasekhar Mass Limit for Relativistic Degenerate Electron Gas.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 16).
"""
import numpy as np

def chandrasekhar_mass(mu_e: float = 2.0) -> float:
    """
    M_Ch = (omega_3^0 / 4 pi) * ((h c / G)^(3/2)) * (1 / (mu_e m_H)^2)
    For Carbon/Oxygen white dwarf (mu_e = 2), M_Ch approx 1.44 Solar Masses (2.86e30 kg).
    """
    h = 6.62607015e-34
    c = 2.99792458e8
    G = 6.67430e-11
    m_H = 1.6735575e-27

    # Prefactor from n=3 Lane-Emden polytrope (omega_3^0 approx 2.01824)
    omega3 = 2.01824
    m_ch = (omega3 / (4.0 * np.pi)) * ((h * c / G)**1.5) / ((mu_e * m_H)**2)
    return float(m_ch)
