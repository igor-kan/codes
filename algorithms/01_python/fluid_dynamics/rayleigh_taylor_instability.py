"""Rayleigh-Taylor Interfacial Instability Analysis.

Computes dispersion relation omega^2 = - g k (rho_2 - rho_1) / (rho_2 + rho_1) and exponential growth.
"""

import numpy as np


class RayleighTaylorInstability:
    """Interfacial hydrodynamic instability."""

    G = 9.80665

    @classmethod
    def atwood_number(cls, rho_heavy: float, rho_light: float) -> float:
        """A = (rho_2 - rho_1) / (rho_2 + rho_1)."""
        return float((rho_heavy - rho_light) / (rho_heavy + rho_light))

    @classmethod
    def growth_rate(cls, wavenumber_k: float, rho_heavy: float, rho_light: float) -> float:
        """gamma = sqrt(A * g * k)."""
        a = cls.atwood_number(rho_heavy, rho_light)
        if a <= 0.0:
            return 0.0
        return float(np.sqrt(a * cls.G * wavenumber_k))
