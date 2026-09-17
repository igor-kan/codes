"""Debye Model for Phonon Heat Capacity in Solids.

Explains T^3 low-temperature scaling and Dulong-Petit high-temperature limit 3 N k_B.
"""

import numpy as np


class DebyeSolid:
    """Debye solid lattice vibrations."""

    @staticmethod
    def low_temperature_cv(temperature: float, debye_temperature: float, num_atoms: int, k_b: float = 1.0) -> float:
        """C_V = 12 pi^4 / 5 * N k_B (T / Theta_D)^3."""
        factor = (12.0 * (np.pi**4) / 5.0) * num_atoms * k_b
        return float(factor * ((temperature / debye_temperature)**3))

    @staticmethod
    def dulong_petit_limit(num_atoms: int, k_b: float = 1.0) -> float:
        """C_V = 3 N k_B."""
        return float(3.0 * num_atoms * k_b)
