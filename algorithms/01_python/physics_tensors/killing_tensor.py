"""Killing Vector Fields and Rank-2 Killing Tensors K_{mu nu}.

Generates constants of geodesic motion nabla_{(lambda} K_{mu nu)} = 0 (e.g. Carter constant).
"""

from typing import Sequence
import numpy as np


class KillingTensor:
    """Second-rank symmetric Killing tensor K_{mu nu}."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.k = np.array(matrix, dtype=np.float64)
        if self.k.ndim != 2 or self.k.shape[0] != self.k.shape[1]:
            raise ValueError("Killing tensor must be square")
        if not np.allclose(self.k, self.k.T):
            raise ValueError("Killing tensor must be symmetric")

    def conserved_quantity(self, four_velocity: Sequence[float]) -> float:
        """C = K_{mu nu} u^mu u^nu is conserved along geodesics."""
        u = np.array(four_velocity, dtype=np.float64)
        return float(u @ self.k @ u)
