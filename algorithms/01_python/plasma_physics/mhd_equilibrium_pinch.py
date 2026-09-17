"""Bennett Pinch Equilibrium in Cylindrical Plasmas.

Calculates Bennett relation I^2 = 8 pi / mu_0 * N k_B (T_e + T_i).
"""

import numpy as np


class BennettPinch:
    """Cylindrical z-pinch equilibrium."""

    MU_0 = 1.25663706212e-6
    K_B = 1.380649e-23

    @classmethod
    def bennett_current(cls, linear_density_n: float, total_temp_kelvin: float) -> float:
        """I = sqrt(8 pi k_B N T / mu_0)."""
        factor = 8.0 * np.pi * cls.K_B * linear_density_n * total_temp_kelvin / cls.MU_0
        return float(np.sqrt(factor))
