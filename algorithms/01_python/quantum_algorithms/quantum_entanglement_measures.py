"""Entanglement Measures: Concurrence, Negativity, and Logarithmic Negativity.

Quantifies quantum entanglement in bipartite density matrices rho_{AB}.
"""

import numpy as np


class EntanglementMeasures:
    """Calculates bipartite entanglement metrics."""

    @staticmethod
    def negativity(rho_ab: np.ndarray, dim_a: int = 2, dim_b: int = 2) -> float:
        """Negativity N(rho) = (||rho^{T_B}||_1 - 1) / 2 = sum |lambda_negative|."""
        # Partial transpose with respect to B
        tensor = rho_ab.reshape((dim_a, dim_b, dim_a, dim_b))
        pt = np.transpose(tensor, (0, 3, 2, 1)).reshape((dim_a * dim_b, dim_a * dim_b))
        evals = np.linalg.eigvalsh(pt)
        neg_sum = np.sum(np.abs(evals[evals < 0]))
        return float(neg_sum)

    @staticmethod
    def logarithmic_negativity(rho_ab: np.ndarray, dim_a: int = 2, dim_b: int = 2) -> float:
        """E_N(rho) = log2 ||rho^{T_B}||_1."""
        neg = EntanglementMeasures.negativity(rho_ab, dim_a, dim_b)
        return float(np.log2(2.0 * neg + 1.0))
