"""Infinitesimal Small-Deformation Strain Tensor varepsilon_{ij}.

Decomposes displacement gradient into symmetric strain and antisymmetric rotation tensors.
"""

from typing import Sequence, Tuple
import numpy as np


class InfinitesimalStrainTensor:
    """Infinitesimal strain tensor varepsilon_{ij}."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.strain = np.array(matrix, dtype=np.float64)
        if self.strain.shape != (3, 3):
            raise ValueError("Strain tensor must be 3x3")
        if not np.allclose(self.strain, self.strain.T):
            raise ValueError("Infinitesimal strain tensor must be symmetric")

    @classmethod
    def from_displacement_gradient(cls, grad_u: Sequence[Sequence[float]]) -> Tuple['InfinitesimalStrainTensor', np.ndarray]:
        """Compute strain eps = 1/2 (grad u + grad u^T) and rotation omega = 1/2 (grad u - grad u^T)."""
        h = np.array(grad_u, dtype=np.float64)
        if h.shape != (3, 3):
            raise ValueError("Displacement gradient must be 3x3")
        eps = 0.5 * (h + h.T)
        omega = 0.5 * (h - h.T)
        return cls(eps), omega

    @property
    def volumetric_strain(self) -> float:
        """epsilon_v = tr(epsilon) = dV / V."""
        return float(np.trace(self.strain))

    @property
    def deviatoric_strain(self) -> np.ndarray:
        """e_{ij} = varepsilon_{ij} - 1/3 eps_v delta_{ij}."""
        return self.strain - (self.volumetric_strain / 3.0) * np.eye(3)
