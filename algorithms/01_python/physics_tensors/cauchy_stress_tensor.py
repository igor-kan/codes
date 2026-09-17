"""Cauchy Stress Tensor sigma_{ij} in Continuum Mechanics.

Computes traction vectors, principal stresses, deviatoric stress, and von Mises yield criterion.
"""

from typing import Sequence, Tuple
import numpy as np


class CauchyStressTensor:
    """3D Symmetric Cauchy stress tensor."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.sigma = np.array(matrix, dtype=np.float64)
        if self.sigma.shape != (3, 3):
            raise ValueError("Stress tensor must be a 3x3 matrix")
        if not np.allclose(self.sigma, self.sigma.T):
            raise ValueError("Cauchy stress tensor must be symmetric (balance of angular momentum)")

    def traction(self, normal_vector: Sequence[float]) -> np.ndarray:
        """Traction vector t = sigma * n."""
        n = np.array(normal_vector, dtype=np.float64)
        n = n / np.linalg.norm(n)
        return self.sigma @ n

    @property
    def hydrostatic_stress(self) -> float:
        """sigma_m = 1/3 tr(sigma)."""
        return float(np.trace(self.sigma) / 3.0)

    @property
    def deviatoric_stress(self) -> np.ndarray:
        """s_{ij} = sigma_{ij} - sigma_m delta_{ij}."""
        return self.sigma - self.hydrostatic_stress * np.eye(3)

    def invariants(self) -> Tuple[float, float, float]:
        """Stress invariants I_1, J_2, J_3."""
        i1 = float(np.trace(self.sigma))
        s = self.deviatoric_stress
        j2 = 0.5 * float(np.trace(s @ s))
        j3 = float(np.linalg.det(s))
        return i1, j2, j3

    def von_mises_equivalent_stress(self) -> float:
        """sigma_vM = sqrt(3 * J_2)."""
        _, j2, _ = self.invariants()
        return np.sqrt(3.0 * max(0.0, j2))

    def principal_stresses(self) -> np.ndarray:
        """Principal stresses sorted descending: sigma_1 >= sigma_2 >= sigma_3."""
        evals = np.linalg.eigvalsh(self.sigma)
        return np.sort(evals)[::-1]
