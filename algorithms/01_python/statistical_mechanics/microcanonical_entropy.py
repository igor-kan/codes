"""Boltzmann Microcanonical Entropy S = k_B ln Omega(E) and Temperature 1/T = dS/dE.

Fundamental relation of statistical thermodynamics.
"""

import numpy as np


class MicrocanonicalEntropy:
    """Microcanonical entropy and thermodynamic temperature."""

    K_B = 1.380649e-23

    @classmethod
    def entropy(cls, microstates_omega: float) -> float:
        """S = k_B ln Omega."""
        return float(cls.K_B * np.log(max(1.0, microstates_omega)))

    @classmethod
    def temperature_from_finite_difference(cls, e1: float, e2: float,
                                            omega1: float, omega2: float) -> float:
        """1/T = (S2 - S1) / (E2 - E1)."""
        ds = cls.entropy(omega2) - cls.entropy(omega1)
        de = e2 - e1
        inv_t = ds / de
        return float(1.0 / inv_t)
