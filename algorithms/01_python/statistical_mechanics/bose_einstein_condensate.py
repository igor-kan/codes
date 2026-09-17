"""Bose-Einstein Distribution and Critical Condensation Temperature T_c.

Models ideal Bose gas in 3D harmonic trap and macroscopically occupied ground state.
"""

import numpy as np


class BoseEinsteinCondensation:
    """Ideal Bose gas thermodynamics."""

    HBAR = 1.054571817e-34
    K_B = 1.380649e-23
    ZETA_3 = 1.202056903159594

    @classmethod
    def critical_temperature_harmonic_trap(cls, num_particles: int, geometric_mean_omega: float) -> float:
        """T_c = hbar omega_bar / k_B * (N / zeta(3))^{1/3}."""
        factor = (num_particles / cls.ZETA_3)**(1.0 / 3.0)
        return float((cls.HBAR * geometric_mean_omega / cls.K_B) * factor)

    @classmethod
    def condensed_fraction(cls, t: float, t_c: float) -> float:
        """N_0 / N = 1 - (T / T_c)^3 for T < T_c."""
        if t >= t_c:
            return 0.0
        return float(1.0 - (t / t_c)**3)
