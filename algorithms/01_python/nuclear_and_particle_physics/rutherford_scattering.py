"""
Rutherford Differential Scattering Cross Section and Impact Parameter.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 11).
"""
import numpy as np

def rutherford_impact_parameter(theta_rad: float, z: int, Z: int, E_kinetic_MeV: float) -> float:
    """Impact parameter b = (z Z e^2 / (8 pi eps0 E)) * cot(theta / 2)."""
    k_e2 = 1.4399645  # MeV * fm
    return float((z * Z * k_e2 / (2.0 * E_kinetic_MeV)) / np.tan(0.5 * theta_rad))

def rutherford_differential_cross_section(theta_rad: float, z: int, Z: int, E_kinetic_MeV: float) -> float:
    """dsigma/dOmega = (z Z e^2 / (16 pi eps0 E))^2 / sin^4(theta / 2)."""
    k_e2 = 1.4399645  # MeV * fm
    factor = (z * Z * k_e2 / (4.0 * E_kinetic_MeV))**2
    return float(factor / (np.sin(0.5 * theta_rad)**4))
