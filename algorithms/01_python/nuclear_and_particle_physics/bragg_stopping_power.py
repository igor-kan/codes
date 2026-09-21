"""
Bethe-Bloch Heavy Charged Particle Stopping Power.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 7).
"""
import numpy as np

def bethe_bloch_stopping_power(beta: float, z_particle: int = 1, Z_medium: int = 6, I_eV: float = 78.0) -> float:
    """Relative Bethe-Bloch -dE/dx ~ (z^2 / beta^2) [ln(2 m_e c^2 beta^2 gamma^2 / I) - beta^2]."""
    if beta <= 0.0 or beta >= 1.0:
        return 0.0
    gamma = 1.0 / np.sqrt(1.0 - beta**2)
    m_e_c2_eV = 510998.95
    arg = 2.0 * m_e_c2_eV * (beta**2) * (gamma**2) / I_eV
    if arg <= 1.0:
        return 0.0
    term = np.log(arg) - beta**2
    return float((z_particle**2 / beta**2) * term)
