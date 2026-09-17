"""Maxwell Stress Tensor sigma_{ij} and Poynting Vector S.

Represents the momentum flux and electromagnetic stress in electrodynamics.
"""

from typing import Sequence
import numpy as np


class MaxwellStressTensor:
    """Maxwell stress tensor and Poynting flux."""

    EPSILON_0 = 8.8541878128e-12
    MU_0 = 1.25663706212e-6

    def __init__(self, e_field: Sequence[float], b_field: Sequence[float]):
        self.e = np.array(e_field, dtype=np.float64)
        self.b = np.array(b_field, dtype=np.float64)

    def poynting_vector(self) -> np.ndarray:
        """S = (1 / mu_0) * (E x B)."""
        return (1.0 / self.MU_0) * np.cross(self.e, self.b)

    def energy_density(self) -> float:
        """u = 1/2 (epsilon_0 E^2 + (1/mu_0) B^2)."""
        return 0.5 * (self.EPSILON_0 * np.dot(self.e, self.e) + (1.0 / self.MU_0) * np.dot(self.b, self.b))

    def stress_tensor_3d(self) -> np.ndarray:
        """sigma_{ij} = eps_0 E_i E_j + (1/mu_0) B_i B_j - 1/2 (eps_0 E^2 + (1/mu_0) B^2) delta_{ij}."""
        u = self.energy_density()
        return (self.EPSILON_0 * np.outer(self.e, self.e) +
                (1.0 / self.MU_0) * np.outer(self.b, self.b) -
                u * np.eye(3))
