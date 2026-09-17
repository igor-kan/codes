"""Stress-Energy-Momentum Tensor T^{mu nu}.

Supports perfect fluids, dust, relativistic radiation, and vacuum energy.
"""

from typing import Sequence
import numpy as np


class StressEnergyTensor:
    """Stress-energy tensor T^{mu nu}."""

    def __init__(self, data: np.ndarray):
        self.data = np.array(data, dtype=np.float64)
        if self.data.ndim != 2 or self.data.shape[0] != 4 or self.data.shape[1] != 4:
            raise ValueError("Stress energy tensor must be a 4x4 matrix")
        if not np.allclose(self.data, self.data.T):
            raise ValueError("Stress-energy tensor must be symmetric")

    @classmethod
    def perfect_fluid(cls, energy_density: float, pressure: float,
                      four_velocity: Sequence[float], metric: np.ndarray) -> 'StressEnergyTensor':
        """T^{mu nu} = (rho + p) u^mu u^nu + p g^{mu nu}."""
        u = np.array(four_velocity, dtype=np.float64)
        inv_g = np.linalg.inv(metric)
        t = (energy_density + pressure) * np.outer(u, u) + pressure * inv_g
        return cls(t)

    def trace(self, metric: np.ndarray) -> float:
        """T = g_{mu nu} T^{mu nu}."""
        return float(np.einsum('mn,mn->', metric, self.data))
