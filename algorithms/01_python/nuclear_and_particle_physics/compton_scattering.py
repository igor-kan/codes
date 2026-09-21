"""
Relativistic Compton Scattering Kinematics.
References: Halliday, Resnick, Krane - Physics (Vol. 2).
"""
import numpy as np

H_PLANCK = 6.62607015e-34
M_ELECTRON = 9.1093837e-31
C_LIGHT = 2.99792458e8
LAMBDA_COMPTON = H_PLANCK / (M_ELECTRON * C_LIGHT)  # 2.42631023867e-12 m

def compton_wavelength_shift(theta_rad: float) -> float:
    """Delta lambda = lambda_C (1 - cos(theta))."""
    return float(LAMBDA_COMPTON * (1.0 - np.cos(theta_rad)))

def scattered_photon_energy(E_gamma_eV: float, theta_rad: float) -> float:
    """Scattered photon energy E' = E / (1 + (E / m_e c^2)(1 - cos theta))."""
    m_e_c2_eV = 510998.95
    return float(E_gamma_eV / (1.0 + (E_gamma_eV / m_e_c2_eV) * (1.0 - np.cos(theta_rad))))
