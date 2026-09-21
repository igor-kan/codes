"""
Saha Ionization Equation for Thermal Plasma in Stellar Atmospheres.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 8).
"""
import numpy as np

def saha_ionization_ratio(T: float, Pe: float, chi_eV: float, U_ratio: float = 0.5) -> float:
    """
    Saha equation: N_{i+1} / N_i = (2 k T / P_e) * (U_{i+1} / U_i) * (2 pi m_e k T / h^2)^(3/2) * exp(-chi / (k T)).
    """
    k_B = 1.380649e-23
    m_e = 9.1093837e-31
    h = 6.62607015e-34
    chi_J = chi_eV * 1.602176634e-19

    thermal_vol = (2.0 * np.pi * m_e * k_B * T / (h**2))**1.5
    prefactor = (2.0 * k_B * T / Pe) * U_ratio * thermal_vol
    exp_factor = np.exp(-chi_J / (k_B * T))
    return float(prefactor * exp_factor)
