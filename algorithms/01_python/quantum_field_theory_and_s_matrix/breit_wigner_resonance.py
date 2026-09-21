"""Relativistic Breit-Wigner Lineshape for Intermediate Particle Resonances.

sigma(E) = (12 * pi / M^2) * (Gamma_in * Gamma_out) / ((s - M^2)^2 + M^2 * Gamma_tot^2).
"""
import numpy as np


def relativistic_breit_wigner(s: float, m_res: float, gamma_tot: float, gamma_in: float, gamma_out: float) -> float:
    """Calculate cross section for resonant scattering via intermediate resonance."""
    if s <= 0 or m_res <= 0:
        raise ValueError("s and m_res must be positive")
    
    num = 12.0 * np.pi * gamma_in * gamma_out
    denom = (s - m_res**2)**2 + (m_res * gamma_tot)**2
    return float(num / denom)


def z_boson_cross_section(e_cm: float) -> float:
    """Z-boson resonant e+ e- -> hadrons peak at M_Z = 91.1876 GeV, Gamma_Z = 2.4952 GeV."""
    m_z = 91.1876
    gamma_z = 2.4952
    gamma_ee = 0.0839
    gamma_had = 1.7444
    s = e_cm**2
    return relativistic_breit_wigner(s, m_z, gamma_z, gamma_ee, gamma_had)
