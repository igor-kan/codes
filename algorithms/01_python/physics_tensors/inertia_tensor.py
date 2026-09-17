"""Rotational Moment of Inertia Tensor I_{ij}.

Calculates discrete mass point inertia, principal moments/axes, and parallel axis theorem.
"""

from typing import Sequence, Tuple
import numpy as np


class InertiaTensor:
    """Rank-2 rotational inertia tensor I_{ij}."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.i_mat = np.array(matrix, dtype=np.float64)
        if self.i_mat.shape != (3, 3):
            raise ValueError("Inertia tensor must be a 3x3 matrix")
        if not np.allclose(self.i_mat, self.i_mat.T):
            raise ValueError("Inertia tensor must be symmetric")

    @classmethod
    def from_point_masses(cls, masses: Sequence[float], positions: Sequence[Sequence[float]]) -> 'InertiaTensor':
        """Compute I_{ij} = sum_k m_k (r_k^2 delta_{ij} - x_{k,i} x_{k,j})."""
        m_arr = np.array(masses, dtype=np.float64)
        r_arr = np.array(positions, dtype=np.float64)
        if len(m_arr) != len(r_arr):
            raise ValueError("Masses and positions lengths must match")

        i_mat = np.zeros((3, 3), dtype=np.float64)
        for m, r in zip(m_arr, r_arr):
            r2 = float(np.dot(r, r))
            i_mat += m * (r2 * np.eye(3) - np.outer(r, r))
        return cls(i_mat)

    def principal_moments_and_axes(self) -> Tuple[np.ndarray, np.ndarray]:
        """Returns sorted principal moments (eigenvalues) and principal axes (columns of eigenvectors)."""
        evals, evecs = np.linalg.eigh(self.i_mat)
        return evals, evecs

    def parallel_axis_theorem(self, total_mass: float, shift_vector: Sequence[float]) -> 'InertiaTensor':
        """Steiner's parallel axis theorem: I'_{ij} = I_{cm, ij} + M (d^2 delta_{ij} - d_i d_j)."""
        d = np.array(shift_vector, dtype=np.float64)
        d2 = float(np.dot(d, d))
        shifted = self.i_mat + total_mass * (d2 * np.eye(3) - np.outer(d, d))
        return InertiaTensor(shifted)

    def kinetic_energy(self, omega: Sequence[float]) -> float:
        """T = 1/2 omega^T I omega."""
        w = np.array(omega, dtype=np.float64)
        return 0.5 * float(w @ self.i_mat @ w)
