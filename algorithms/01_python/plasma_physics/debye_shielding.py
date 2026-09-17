"""Debye Shielding, Debye Length, and Plasma Parameter.

Calculates lambda_D = sqrt(eps_0 k_B T_e / (n_e e^2)) and plasma parameter Lambda = n_e lambda_D^3.
"""

import numpy as np


class DebyeShielding:
    """Debye screening in quasi-neutral plasmas."""

    EPS_0 = 8.8541878128e-12
    K_B = 1.380649e-23
    E_CHARGE = 1.602176634e-19

    @classmethod
    def debye_length(cls, electron_density: float, electron_temp_kelvin: float) -> float:
        """lambda_D = sqrt(eps_0 k_B T_e / (n_e e^2))."""
        num = cls.EPS_0 * cls.K_B * electron_temp_kelvin
        denom = electron_density * (cls.E_CHARGE**2)
        return float(np.sqrt(num / denom))

    @classmethod
    def plasma_parameter(cls, electron_density: float, electron_temp_kelvin: float) -> float:
        """Lambda = n_e * (4/3 pi lambda_D^3) (number of particles in Debye sphere)."""
        ld = cls.debye_length(electron_density, electron_temp_kelvin)
        return float(electron_density * (4.0 / 3.0) * np.pi * (ld**3))
