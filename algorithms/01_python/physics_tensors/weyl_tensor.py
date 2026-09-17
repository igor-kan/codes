"""Conformal Weyl Curvature Tensor C_{rho sigma mu nu}.

Represents the free gravitational field and conformal curvature in dim >= 4.
"""

import numpy as np


class WeylCurvatureTensor:
    """Weyl tensor C_{abcd}."""

    def __init__(self, data: np.ndarray):
        self.data = np.array(data, dtype=np.float64)
        self.dim = self.data.shape[0]
        if self.dim < 3:
            raise ValueError("Weyl tensor identically vanishes in dimensions n < 3")

    @classmethod
    def from_riemann_and_ricci(cls, r_cov: np.ndarray, ricci_cov: np.ndarray,
                                scalar: float, g: np.ndarray) -> 'WeylCurvatureTensor':
        """Construct C_{abcd} from fully covariant Riemann, Ricci, and scalar."""
        n = g.shape[0]
        c = np.zeros((n, n, n, n), dtype=np.float64)
        for a in range(n):
            for b in range(n):
                for m in range(n):
                    for nu in range(n):
                        term1 = r_cov[a, b, m, nu]
                        term2 = (1.0 / (n - 2.0)) * (
                            g[a, m] * ricci_cov[nu, b] - g[a, nu] * ricci_cov[m, b] +
                            g[b, nu] * ricci_cov[m, a] - g[b, m] * ricci_cov[nu, a]
                        )
                        term3 = (scalar / ((n - 1.0) * (n - 2.0))) * (
                            g[a, m] * g[nu, b] - g[a, nu] * g[m, b]
                        )
                        c[a, b, m, nu] = term1 - term2 + term3
        return cls(c)

    def is_conformally_flat(self, tol: float = 1e-6) -> bool:
        """Check if C_{abcd} == 0."""
        return bool(np.all(np.abs(self.data) < tol))
