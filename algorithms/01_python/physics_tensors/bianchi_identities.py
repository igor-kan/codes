"""First (Algebraic) and Second (Differential) Bianchi Identities.

Verifies nabla_[lambda R_{alpha beta| mu nu]} = 0 and the contracted Bianchi identity nabla_mu G^{mu nu} = 0.
"""

from typing import Sequence
import numpy as np


class BianchiIdentities:
    """Bianchi identity checks for differential geometry and general relativity."""

    @staticmethod
    def verify_algebraic_bianchi(riemann_cov: np.ndarray, tol: float = 1e-7) -> bool:
        """R_{abcd} + R_{acdb} + R_{adbc} = 0."""
        dim = riemann_cov.shape[0]
        for a in range(dim):
            for b in range(dim):
                for c in range(dim):
                    for d in range(dim):
                        val = riemann_cov[a, b, c, d] + riemann_cov[a, c, d, b] + riemann_cov[a, d, b, c]
                        if abs(val) > tol:
                            return False
        return True

    @staticmethod
    def verify_contracted_bianchi(divergence_einstein: Sequence[float], tol: float = 1e-6) -> bool:
        """Verifies nabla_mu G^{mu nu} == 0."""
        return bool(np.all(np.abs(divergence_einstein) < tol))
