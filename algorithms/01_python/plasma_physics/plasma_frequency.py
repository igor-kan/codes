"""Electron and Ion Plasma Oscillations (Langmuir Frequency).

Calculates omega_pe = sqrt(n_e e^2 / (eps_0 m_e)) and EM cutoff index n^2 = 1 - omega_pe^2 / omega^2.
"""

import numpy as np


class PlasmaFrequency:
    """Langmuir plasma oscillation frequencies."""

    EPS_0 = 8.8541878128e-12
    E_CHARGE = 1.602176634e-19
    M_E = 9.1093837e-31

    @classmethod
    def electron_plasma_frequency(cls, electron_density: float) -> float:
        """omega_pe = sqrt(n_e e^2 / (eps_0 m_e)) in rad/s."""
        return float(np.sqrt(electron_density * (cls.E_CHARGE**2) / (cls.EPS_0 * cls.M_E)))

    @classmethod
    def dielectric_permittivity(cls, wave_omega: float, electron_density: float) -> float:
        """eps(omega) = 1 - omega_pe^2 / omega^2."""
        w_pe = cls.electron_plasma_frequency(electron_density)
        return float(1.0 - (w_pe / wave_omega)**2)
