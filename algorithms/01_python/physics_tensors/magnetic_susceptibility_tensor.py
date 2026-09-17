"""Magnetic Susceptibility Tensor chi_{ij}.

Relates magnetization to applied magnetic field M_i = chi_{ij} H_j.
"""

from typing import Sequence
import numpy as np


class MagneticSusceptibilityTensor:
    """Rank-2 magnetic susceptibility tensor."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.chi = np.array(matrix, dtype=np.float64)
        if self.chi.shape != (3, 3):
            raise ValueError("Susceptibility tensor must be 3x3")

    def magnetization(self, h_field: Sequence[float]) -> np.ndarray:
        """M = chi * H."""
        h = np.array(h_field, dtype=np.float64)
        return self.chi @ h

    @property
    def magnetic_anisotropy(self) -> float:
        """Delta chi = chi_parallel - chi_perp for axial symmetry."""
        evals = np.linalg.eigvals(self.chi)
        real_evals = np.sort(np.real(evals))[::-1]
        return float(real_evals[0] - real_evals[-1])
