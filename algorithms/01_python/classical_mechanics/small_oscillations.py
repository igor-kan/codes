"""Theory of Small Oscillations and Normal Modes in Coupled Systems.

Implements Landau & Lifshitz Ch. 5 and Goldstein Ch. 6:
Solves generalized eigenvalue problem (K - omega^2 M) a = 0 and constructs uncoupled normal coordinates.
"""

from typing import Sequence, Tuple
import numpy as np
from scipy.linalg import eigh


class SmallOscillations:
    """Coupled harmonic oscillator normal modes analysis."""

    def __init__(self, mass_matrix: Sequence[Sequence[float]], stiffness_matrix: Sequence[Sequence[float]]):
        self.m = np.array(mass_matrix, dtype=np.float64)
        self.k = np.array(stiffness_matrix, dtype=np.float64)
        self.n = self.m.shape[0]

        if not np.allclose(self.m, self.m.T) or not np.allclose(self.k, self.k.T):
            raise ValueError("Mass and stiffness matrices must be symmetric")

    def normal_modes(self) -> Tuple[np.ndarray, np.ndarray]:
        """Solve (K - omega^2 M) a = 0.
        Returns:
            frequencies: sorted natural frequencies omega_i >= 0.
            mode_shapes: columns normalized such that A^T M A = I, A^T K A = diag(omega^2).
        """
        eigenvalues, eigenvectors = eigh(self.k, self.m)
        eigenvalues = np.maximum(0.0, eigenvalues)
        frequencies = np.sqrt(eigenvalues)
        return frequencies, eigenvectors
