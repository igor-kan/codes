"""Gibbs Canonical Partition Function Z(beta) and Free Energy F = - k_B T ln Z.

Calculates average internal energy <E> and heat capacity C_V = k_B beta^2 <(Delta E)^2>.
"""

from typing import Sequence, Tuple
import numpy as np


class CanonicalEnsemble:
    """Canonical ensemble calculations for discrete spectrum."""

    def __init__(self, energy_levels: Sequence[float], degeneracies: Sequence[int], temperature: float, k_b: float = 1.0):
        self.energies = np.array(energy_levels, dtype=np.float64)
        self.deg = np.array(degeneracies, dtype=np.float64)
        self.t = temperature
        self.kb = k_b
        self.beta = 1.0 / (k_b * temperature)

    def partition_function(self) -> float:
        """Z = sum g_i exp(- beta E_i)."""
        return float(np.sum(self.deg * np.exp(-self.beta * self.energies)))

    def average_energy(self) -> float:
        """<E> = 1/Z sum g_i E_i exp(- beta E_i)."""
        z = self.partition_function()
        return float(np.sum(self.deg * self.energies * np.exp(-self.beta * self.energies)) / z)

    def heat_capacity(self) -> float:
        """C_V = k_B beta^2 (<E^2> - <E>^2)."""
        z = self.partition_function()
        avg_e = self.average_energy()
        avg_e2 = float(np.sum(self.deg * (self.energies**2) * np.exp(-self.beta * self.energies)) / z)
        var_e = avg_e2 - avg_e**2
        return float(self.kb * (self.beta**2) * var_e)
