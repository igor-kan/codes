"""Traceless Quadrupole Moment Tensor Q_{ij} and Gravitational Radiation.

Implements Q_{ij} = sum_k q_k (3 x_i x_j - r^2 delta_{ij}) and quadrupole formula dE/dt.
"""

from typing import Sequence
import numpy as np


class QuadrupoleMomentTensor:
    """Traceless quadrupole tensor Q_{ij}."""

    G = 6.67430e-11
    C = 299792458.0

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.q = np.array(matrix, dtype=np.float64)
        if self.q.shape != (3, 3):
            raise ValueError("Quadrupole tensor must be 3x3")
        if not np.allclose(self.q, self.q.T):
            raise ValueError("Quadrupole tensor must be symmetric")
        if abs(np.trace(self.q)) > 1e-7:
            raise ValueError("Quadrupole tensor must be traceless")

    @classmethod
    def from_charges(cls, charges: Sequence[float], positions: Sequence[Sequence[float]]) -> 'QuadrupoleMomentTensor':
        """Q_{ij} = sum_k q_k (3 x_i x_j - r^2 delta_{ij})."""
        q_arr = np.array(charges, dtype=np.float64)
        r_arr = np.array(positions, dtype=np.float64)
        q_mat = np.zeros((3, 3), dtype=np.float64)
        for charge, r in zip(q_arr, r_arr):
            r2 = float(np.dot(r, r))
            q_mat += charge * (3.0 * np.outer(r, r) - r2 * np.eye(3))
        return cls(q_mat)

    @classmethod
    def gravitational_radiation_power(cls, q_triple_dot: np.ndarray) -> float:
        """Einstein quadrupole formula: dE/dt = G / (5 c^5) * dddot(Q)_{ij} dddot(Q)_{ij}."""
        q_3d = np.array(q_triple_dot, dtype=np.float64)
        sum_sq = float(np.sum(q_3d**2))
        return (cls.G / (5.0 * (cls.C**5))) * sum_sq
