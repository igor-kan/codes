"""Cartan Torsion Tensor T^lambda_{mu nu} and Contortion Tensor K^lambda_{mu nu}.

Implements asymmetric connections in Einstein-Cartan-Sciama-Kibble gravitation.
"""

import numpy as np


class TorsionTensor:
    """Cartan torsion tensor T^lambda_{mu nu} = Gamma^lambda_{mu nu} - Gamma^lambda_{nu mu}."""

    def __init__(self, gamma: np.ndarray):
        self.gamma = np.array(gamma, dtype=np.float64)
        dim = self.gamma.shape[0]
        self.torsion = np.zeros_like(self.gamma)
        for lam in range(dim):
            self.torsion[lam] = self.gamma[lam] - self.gamma[lam].T

    def is_torsion_free(self, tol: float = 1e-8) -> bool:
        """Checks if connection is symmetric (Levi-Civita condition)."""
        return bool(np.all(np.abs(self.torsion) < tol))
