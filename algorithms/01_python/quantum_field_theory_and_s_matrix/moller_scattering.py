"""Tree-Level QED Moller Scattering (e- + e- -> e- + e-).

Differential cross section in center of mass frame for unpolarized electrons.
Reference: Landau & Lifshitz Vol 4 (Quantum Electrodynamics).
"""
import numpy as np

ALPHA_EM = 1.0 / 137.035999084  # Fine-structure constant


def moller_diff_cross_section_cm(s: float, theta: float, m: float = 0.51099895e-3) -> float:
    """Calculate unpolarized Moller differential cross section dsigma/dOmega (in natural units GeV^-2).

    Parameters:
        s: Center-of-mass energy squared (GeV^2).
        theta: CM scattering angle (radians).
        m: Electron mass in GeV.
    """
    if theta <= 0.0 or theta >= np.pi:
        raise ValueError("Scattering angle theta must be in (0, pi)")
    
    E = np.sqrt(s) / 2.0
    if E <= m:
        raise ValueError("Energy below electron mass threshold")
    
    p = np.sqrt(E**2 - m**2)
    v = p / E  # velocity
    gamma = E / m

    sin_th = np.sin(theta)
    cos_th = np.cos(theta)

    # Ultrarelativistic approximation when E >> m or standard exact Landau formula
    term1 = (2.0 * gamma**2 - 1.0)**2 / (gamma**4 * sin_th**4)
    term2 = (2.0 * gamma**2 - 1.0) / (gamma**4 * sin_th**2)
    term3 = ((gamma**2 - 1.0) / (2.0 * gamma**2))**2 * (1.0 + 4.0 / sin_th**2)

    prefactor = (ALPHA_EM / (2.0 * m * gamma * v**2))**2
    return float(prefactor * (term1 - term2 + term3))
