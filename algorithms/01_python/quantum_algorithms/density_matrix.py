"""Density Matrix Operator rho, Purity, von Neumann Entropy, and Partial Trace.

Encapsulates mixed and entangled states on Hilbert spaces.
"""

from typing import Sequence, Tuple
import numpy as np


class DensityMatrix:
    """Density operator rho representing pure or mixed quantum states."""

    def __init__(self, matrix: Sequence[Sequence[complex]]):
        self.rho = np.array(matrix, dtype=np.complex128)
        if self.rho.ndim != 2 or self.rho.shape[0] != self.rho.shape[1]:
            raise ValueError("Density matrix must be square")
        # Trace should be 1
        tr = np.trace(self.rho)
        if abs(tr - 1.0) > 1e-6:
            raise ValueError(f"Density matrix must have trace 1, got {tr}")
        # Hermiticity
        if not np.allclose(self.rho, self.rho.conj().T, atol=1e-7):
            raise ValueError("Density matrix must be Hermitian")
        self.dim = self.rho.shape[0]

    @property
    def purity(self) -> float:
        """gamma = Tr(rho^2) in [1/dim, 1]. Pure state iff gamma == 1."""
        return float(np.real(np.trace(self.rho @ self.rho)))

    @property
    def von_neumann_entropy(self) -> float:
        """S = - Tr(rho log2 rho) = - sum lambda_i log2(lambda_i)."""
        evals = np.linalg.eigvalsh(self.rho)
        entropy = 0.0
        for ev in evals:
            if ev > 1e-12:
                entropy -= ev * np.log2(ev)
        return float(entropy)

    @classmethod
    def partial_trace_bipartite(cls, rho_ab: np.ndarray, dim_a: int, dim_b: int) -> np.ndarray:
        """Compute partial trace over subsystem B: rho_A = Tr_B(rho_AB)."""
        tensor_4d = rho_ab.reshape((dim_a, dim_b, dim_a, dim_b))
        return np.trace(tensor_4d, axis1=1, axis2=3)
