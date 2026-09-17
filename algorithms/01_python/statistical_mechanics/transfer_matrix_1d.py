"""Exact 1D Ising Model Partition Function via 2x2 Transfer Matrix.

Proves absence of phase transitions at T > 0 in 1D: Z_N = lambda_+^N + lambda_-^N.
"""

import numpy as np


class TransferMatrix1D:
    """Transfer matrix method for 1D Ising chain."""

    def __init__(self, coupling_j: float, external_field_h: float = 0.0, temperature: float = 1.0):
        self.j = coupling_j
        self.h = external_field_h
        self.t = temperature
        self.beta = 1.0 / temperature

    def transfer_matrix(self) -> np.ndarray:
        """T = [[exp(beta(J + h)), exp(-beta J)], [exp(-beta J), exp(beta(J - h))]]."""
        b = self.beta
        j = self.j
        h = self.h
        return np.array([
            [np.exp(b * (j + h)), np.exp(-b * j)],
            [np.exp(-b * j),     np.exp(b * (j - h))]
        ], dtype=np.float64)

    def eigenvalues(self) -> np.ndarray:
        """Eigenvalues lambda_+ >= lambda_-."""
        t_mat = self.transfer_matrix()
        evals = np.linalg.eigvalsh(t_mat)
        return np.sort(evals)[::-1]

    def free_energy_per_spin_infinite_limit(self) -> float:
        """f = - k_B T ln(lambda_+)."""
        l_plus = self.eigenvalues()[0]
        return float(- self.t * np.log(l_plus))
