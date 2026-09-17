"""Dielectric Permittivity Tensor varepsilon_{ij} and Optical Indicatrix.

Classifies anisotropic optical media into isotropic, uniaxial, and biaxial crystals.
"""

from typing import Sequence, Tuple
import numpy as np


class DielectricPermittivityTensor:
    """Rank-2 dielectric permittivity tensor."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.eps = np.array(matrix, dtype=np.float64)
        if self.eps.shape != (3, 3):
            raise ValueError("Dielectric tensor must be 3x3")
        if not np.allclose(self.eps, self.eps.T):
            raise ValueError("Dielectric tensor must be symmetric in lossless media")

    def principal_refractive_indices(self) -> Tuple[float, float, float]:
        """Principal indices n_i = sqrt(eps_{r, i})."""
        evals = np.linalg.eigvalsh(self.eps)
        if np.any(evals <= 0):
            raise ValueError("Permittivity eigenvalues must be positive")
        indices = np.sqrt(np.sort(evals)[::-1])
        return float(indices[0]), float(indices[1]), float(indices[2])

    def optical_classification(self, tol: float = 1e-4) -> str:
        """Classify crystal into isotropic, uniaxial, or biaxial."""
        n1, n2, n3 = self.principal_refractive_indices()
        diff12 = abs(n1 - n2)
        diff23 = abs(n2 - n3)
        if diff12 < tol and diff23 < tol:
            return "isotropic"
        elif diff12 < tol or diff23 < tol:
            return "uniaxial"
        else:
            return "biaxial"
