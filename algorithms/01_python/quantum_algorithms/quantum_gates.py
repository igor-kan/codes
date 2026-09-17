"""Standard Quantum Logic Gates in SU(2) and U(2^n).

Implements Pauli X, Y, Z, Hadamard H, Phase S, T, CNOT, CZ, and SWAP.
"""

import numpy as np


class QuantumGates:
    """Universal quantum logic gate operators."""

    I = np.eye(2, dtype=np.complex128)
    X = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=np.complex128)
    Y = np.array([[0.0, -1.0j], [1.0j, 0.0]], dtype=np.complex128)
    Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=np.complex128)
    H = (1.0 / np.sqrt(2.0)) * np.array([[1.0, 1.0], [1.0, -1.0]], dtype=np.complex128)
    S = np.array([[1.0, 0.0], [0.0, 1.0j]], dtype=np.complex128)
    T = np.array([[1.0, 0.0], [0.0, np.exp(1.0j * np.pi / 4.0)]], dtype=np.complex128)

    CNOT = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 1.0, 0.0]
    ], dtype=np.complex128)

    SWAP = np.array([
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 1.0]
    ], dtype=np.complex128)

    @staticmethod
    def is_unitary(matrix: np.ndarray, tol: float = 1e-8) -> bool:
        """U^dagger U = I."""
        m = np.array(matrix, dtype=np.complex128)
        prod = m.conj().T @ m
        return bool(np.allclose(prod, np.eye(m.shape[0]), atol=tol))
