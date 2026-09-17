"""Roothaan-Hall Self-Consistent Field (SCF) Hartree-Fock Algorithm.

Solves generalized eigenvalue problem F(P) C = S C epsilon for molecular electronic structure.
"""

from typing import Tuple
import numpy as np
from scipy.linalg import eigh


class HartreeFockRoothaan:
    """Self-consistent field solver."""

    @staticmethod
    def scf_step(fock_matrix: np.ndarray, overlap_matrix: np.ndarray,
                 num_occupied_orbitals: int) -> Tuple[np.ndarray, np.ndarray]:
        """Solve F C = S C eps and compute updated density matrix P = 2 sum_{i in occ} C_i C_i^T."""
        eps, c = eigh(fock_matrix, overlap_matrix)
        c_occ = c[:, :num_occupied_orbitals]
        p_new = 2.0 * (c_occ @ c_occ.T)
        return eps, p_new
