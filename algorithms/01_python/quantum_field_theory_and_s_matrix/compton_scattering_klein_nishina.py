"""Klein-Nishina Differential Cross Section for Compton Scattering.

Unpolarized photon-electron scattering gamma + e- -> gamma + e-.
"""
import numpy as np

ALPHA_EM = 1.0 / 137.035999084
M_ELECTRON = 0.51099895e-3  # GeV
R0_SQ = (ALPHA_EM / M_ELECTRON)**2  # Classical electron radius squared in natural units


def compton_scattered_photon_energy(omega_in: float, theta: float, m: float = M_ELECTRON) -> float:
    """Scattered photon energy omega_out = omega_in / (1 + (omega_in / m)*(1 - cos(theta)))."""
    return omega_in / (1.0 + (omega_in / m) * (1.0 - np.cos(theta)))


def klein_nishina_diff_cross_section(omega_in: float, theta: float, m: float = M_ELECTRON) -> float:
    """Klein-Nishina formula for dsigma/dOmega."""
    omega_out = compton_scattered_photon_energy(omega_in, theta, m)
    P = omega_out / omega_in
    sin_th = np.sin(theta)
    
    return float(0.5 * (ALPHA_EM / m)**2 * P**2 * (P + 1.0 / P - sin_th**2))
