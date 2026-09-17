"""Infeld-van der Waerden Symbols sigma^mu_{A dot{B}} and Two-Component Spinors.

Bridges spacetime 4-vectors to rank-2 SL(2, C) Hermitian spinors.
"""

from typing import Sequence
import numpy as np


class VanDerWaerdenSymbols:
    """Pauli / Infeld-van der Waerden sigma matrices."""

    SIGMA_0 = np.eye(2, dtype=np.complex128)
    SIGMA_1 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
    SIGMA_2 = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=np.complex128)
    SIGMA_3 = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)

    SIGMAS = [SIGMA_0, SIGMA_1, SIGMA_2, SIGMA_3]

    @classmethod
    def vector_to_spinor(cls, four_vector: Sequence[float]) -> np.ndarray:
        """X_{A dot{B}} = X_mu sigma^mu_{A dot{B}}."""
        v = np.array(four_vector, dtype=np.float64)
        mat = np.zeros((2, 2), dtype=np.complex128)
        for mu in range(4):
            mat += v[mu] * cls.SIGMAS[mu]
        return mat

    @classmethod
    def spinor_determinant(cls, spinor_mat: np.ndarray) -> float:
        """det(X) = - (X_0^2 - X_1^2 - X_2^2 - X_3^2) = - eta_{mu nu} X^mu X^nu."""
        return float(np.real(np.linalg.det(spinor_mat)))
