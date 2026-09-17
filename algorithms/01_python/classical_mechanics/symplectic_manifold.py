"""Symplectic Manifold (M^{2n}, omega) and Canonical Symplectic Matrix J.

Mathematical foundations of Hamiltonian mechanics according to V.I. Arnold.
Implements the canonical 2-form omega = sum dq^i ^ dp_i, matrix J, and symplectic condition M^T J M = J.
"""

from typing import Sequence
import numpy as np


class SymplecticManifold:
    """Symplectic phase space with dimension 2n."""

    def __init__(self, degrees_of_freedom: int):
        self.n = degrees_of_freedom
        self.dim = 2 * degrees_of_freedom
        # Standard symplectic matrix J = [[0, I], [-I, 0]]
        self.j_matrix = np.zeros((self.dim, self.dim), dtype=np.float64)
        self.j_matrix[:self.n, self.n:] = np.eye(self.n)
        self.j_matrix[self.n:, :self.n] = -np.eye(self.n)

    def is_symplectic_matrix(self, matrix: np.ndarray, tol: float = 1e-8) -> bool:
        """Check if Jacobian matrix M satisfies the symplectic condition: M^T J M = J."""
        m = np.array(matrix, dtype=np.float64)
        if m.shape != (self.dim, self.dim):
            raise ValueError(f"Matrix must have shape ({self.dim}, {self.dim})")
        res = m.T @ self.j_matrix @ m
        return bool(np.allclose(res, self.j_matrix, atol=tol))

    def symplectic_2form(self, delta_z1: Sequence[float], delta_z2: Sequence[float]) -> float:
        """Evaluate omega(delta z_1, delta z_2) = delta z_1^T J delta z_2."""
        z1 = np.array(delta_z1, dtype=np.float64)
        z2 = np.array(delta_z2, dtype=np.float64)
        return float(z1 @ self.j_matrix @ z2)

    def phase_space_volume_form(self, tangent_vectors: np.ndarray) -> float:
        """Compute the Liouville volume form Omega = omega^n / n! on 2n tangent vectors."""
        # For canonical basis vectors, volume is the Pfaffian / det of the projection
        mat = np.array(tangent_vectors, dtype=np.float64)
        if mat.shape != (self.dim, self.dim):
            raise ValueError(f"Requires {self.dim} vectors of dimension {self.dim}")
        return float(np.linalg.det(mat))
