"""Rank-3 Piezoelectric Coupling Tensor d_{ijk}.

Links dielectric polarization to mechanical stress: P_i = d_{ijk} sigma_{jk}.
"""

from typing import Sequence
import numpy as np


class PiezoelectricTensor:
    """Rank-3 piezoelectric tensor d_{ijk} with d_{ijk} = d_{ikj}."""

    VOIGT_MAP = [(0, 0), (1, 1), (2, 2), (1, 2), (0, 2), (0, 1)]

    def __init__(self, matrix_3x6: Sequence[Sequence[float]]):
        self.d_voigt = np.array(matrix_3x6, dtype=np.float64)
        if self.d_voigt.shape != (3, 6):
            raise ValueError("Piezoelectric Voigt matrix must be 3x6")

        self.d_3d = np.zeros((3, 3, 3), dtype=np.float64)
        for i in range(3):
            for alpha, (j, k) in enumerate(self.VOIGT_MAP):
                factor = 1.0 if alpha < 3 else 0.5
                val = self.d_voigt[i, alpha] * factor
                self.d_3d[i, j, k] = val
                self.d_3d[i, k, j] = val

    def polarization(self, stress_3x3: Sequence[Sequence[float]]) -> np.ndarray:
        """P_i = d_{ijk} sigma_{jk}."""
        sigma = np.array(stress_3x3, dtype=np.float64)
        return np.einsum('ijk,jk->i', self.d_3d, sigma)
