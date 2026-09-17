"""Ideal Magnetohydrodynamic (MHD) Alfven Waves.

Calculates Alfven wave phase speed v_A = B / sqrt(mu_0 rho) and dispersion relation omega = k_parallel v_A.
"""

import numpy as np


class AlfvenWave:
    """MHD shear Alfvén wave characteristics."""

    MU_0 = 1.25663706212e-6

    @classmethod
    def alfven_speed(cls, magnetic_field_tesla: float, mass_density: float) -> float:
        """v_A = B / sqrt(mu_0 rho)."""
        return float(magnetic_field_tesla / np.sqrt(cls.MU_0 * mass_density))

    @classmethod
    def wave_frequency(cls, k_parallel: float, magnetic_field: float, mass_density: float) -> float:
        """omega = k_parallel * v_A."""
        return float(abs(k_parallel) * cls.alfven_speed(magnetic_field, mass_density))
