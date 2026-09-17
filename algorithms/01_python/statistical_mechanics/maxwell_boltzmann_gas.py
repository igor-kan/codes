"""Maxwell-Boltzmann Molecular Speed Distribution and Equipartition.

Implements f(v) = 4 pi (m / 2 pi k_B T)^{3/2} v^2 exp(- m v^2 / 2 k_B T) and characteristic velocities.
"""

from typing import Tuple
import numpy as np


class MaxwellBoltzmannGas:
    """Classical Maxwell-Boltzmann velocity distribution."""

    K_B = 1.380649e-23

    def __init__(self, molecular_mass: float, temperature: float):
        self.m = molecular_mass
        self.t = temperature

    def most_probable_speed(self) -> float:
        """v_p = sqrt(2 k_B T / m)."""
        return float(np.sqrt(2.0 * self.K_B * self.t / self.m))

    def mean_speed(self) -> float:
        """<v> = sqrt(8 k_B T / pi m)."""
        return float(np.sqrt(8.0 * self.K_B * self.t / (np.pi * self.m)))

    def rms_speed(self) -> float:
        """v_rms = sqrt(3 k_B T / m)."""
        return float(np.sqrt(3.0 * self.K_B * self.t / self.m))

    def probability_density(self, v: float) -> float:
        """f(v) speed probability density."""
        factor = 4.0 * np.pi * ((self.m / (2.0 * np.pi * self.K_B * self.t))**1.5)
        return float(factor * (v**2) * np.exp(- self.m * (v**2) / (2.0 * self.K_B * self.t)))
