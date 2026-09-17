"""Quantum Fourier Transform (QFT) and Inverse QFT Operators.

Transforms computational basis |j> to |tilde{j}> = 1/sqrt(N) sum_k omega^{j k} |k>.
"""

import numpy as np


class QuantumFourierTransform:
    """Constructs exact unitary matrix for n-qubit QFT."""

    @staticmethod
    def matrix(num_qubits: int) -> np.ndarray:
        """QFT matrix of dimension N = 2^n with omega = exp(2 pi i / N)."""
        n_dim = 2**num_qubits
        omega = np.exp(2.0j * np.pi / n_dim)
        qft = np.zeros((n_dim, n_dim), dtype=np.complex128)
        for j in range(n_dim):
            for k in range(n_dim):
                qft[j, k] = (omega**(j * k)) / np.sqrt(n_dim)
        return qft

    @classmethod
    def inverse_matrix(cls, num_qubits: int) -> np.ndarray:
        """Inverse QFT matrix QFT^dagger."""
        return cls.matrix(num_qubits).conj().T
