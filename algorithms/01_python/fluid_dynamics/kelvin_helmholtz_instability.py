"""Kelvin-Helmholtz Shear Layer Instability Dispersion Relation.

Calculates imaginary frequency and vortex sheet roll-up growth rate.
"""

import numpy as np


class KelvinHelmholtzInstability:
    """Shear flow interface instability."""

    @staticmethod
    def growth_rate(wavenumber_k: float, u1: float, u2: float, rho1: float, rho2: float) -> float:
        """sigma = k * |u1 - u2| * sqrt(rho1 * rho2) / (rho1 + rho2)."""
        du = abs(u1 - u2)
        return float(wavenumber_k * du * np.sqrt(rho1 * rho2) / (rho1 + rho2))
