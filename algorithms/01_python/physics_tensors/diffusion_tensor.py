"""Diffusion Tensor D_{ij} and Fractional Anisotropy (FA) in Diffusion MRI.

Models anisotropic molecular Brownian motion in fibrous tissues and materials.
"""

from typing import Sequence, Tuple
import numpy as np


class DiffusionTensor:
    """3x3 symmetric positive-definite diffusion tensor."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.d = np.array(matrix, dtype=np.float64)
        if self.d.shape != (3, 3):
            raise ValueError("Diffusion tensor must be 3x3")
        if not np.allclose(self.d, self.d.T):
            raise ValueError("Diffusion tensor must be symmetric")
        evals = np.linalg.eigvalsh(self.d)
        if np.any(evals < 0.0):
            raise ValueError("Diffusion tensor must be positive semi-definite")

    @property
    def principal_diffusivities(self) -> Tuple[float, float, float]:
        """Eigenvalues sorted descending: lambda_1 >= lambda_2 >= lambda_3."""
        evals = np.linalg.eigvalsh(self.d)
        sorted_evals = np.sort(evals)[::-1]
        return float(sorted_evals[0]), float(sorted_evals[1]), float(sorted_evals[2])

    @property
    def mean_diffusivity(self) -> float:
        """MD = 1/3 (lambda_1 + lambda_2 + lambda_3)."""
        return float(np.trace(self.d) / 3.0)

    @property
    def fractional_anisotropy(self) -> float:
        """FA = sqrt(3/2) * sqrt(sum((lambda_i - MD)^2)) / sqrt(sum(lambda_i^2))."""
        l1, l2, l3 = self.principal_diffusivities
        md = self.mean_diffusivity
        denom = np.sqrt(l1**2 + l2**2 + l3**2)
        if denom < 1e-15:
            return 0.0
        num = np.sqrt((l1 - md)**2 + (l2 - md)**2 + (l3 - md)**2)
        return float(np.sqrt(1.5) * (num / denom))
