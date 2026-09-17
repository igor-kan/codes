"""Riemann Curvature Tensor R^rho_{sigma mu nu}.

Computes Riemann tensor from Christoffel symbols and verifies algebraic symmetries.
"""

from typing import Callable, Sequence
import numpy as np
try:
    from .christoffel_symbols import ChristoffelSymbols
except ImportError:
    from christoffel_symbols import ChristoffelSymbols


class RiemannCurvatureTensor:
    """Rank-4 Riemann curvature tensor R^rho_{sigma mu nu}."""

    def __init__(self, data: np.ndarray):
        self.data = np.array(data, dtype=np.float64)
        if self.data.ndim != 4:
            raise ValueError("Riemann tensor must be a 4D array")
        self.dim = self.data.shape[0]

    @classmethod
    def from_christoffel_field(cls, christoffel_func: Callable[[np.ndarray], ChristoffelSymbols],
                               x: Sequence[float], eps: float = 1e-5) -> 'RiemannCurvatureTensor':
        """Compute R^rho_{sigma mu nu} = d_mu Gamma^rho_{nu sigma} - d_nu Gamma^rho_{mu sigma} + Gamma * Gamma."""
        x_arr = np.array(x, dtype=np.float64)
        dim = len(x_arr)
        cs0 = christoffel_func(x_arr)
        gamma0 = cs0.gamma

        d_gamma = np.zeros((dim, dim, dim, dim), dtype=np.float64)
        for mu in range(dim):
            xp = x_arr.copy()
            xm = x_arr.copy()
            xp[mu] += eps
            xm[mu] -= eps
            gp = christoffel_func(xp).gamma
            gm = christoffel_func(xm).gamma
            d_gamma[mu] = (gp - gm) / (2.0 * eps)

        riemann = np.zeros((dim, dim, dim, dim), dtype=np.float64)
        for rho in range(dim):
            for sig in range(dim):
                for mu in range(dim):
                    for nu in range(dim):
                        term1 = d_gamma[mu, rho, nu, sig] - d_gamma[nu, rho, mu, sig]
                        term2 = 0.0
                        for lam in range(dim):
                            term2 += gamma0[rho, mu, lam] * gamma0[lam, nu, sig] - gamma0[rho, nu, lam] * gamma0[lam, mu, sig]
                        riemann[rho, sig, mu, nu] = term1 + term2

        return cls(riemann)

    def lower_first_index(self, g: np.ndarray) -> np.ndarray:
        """Compute R_{alpha beta mu nu} = g_{alpha rho} R^rho_{beta mu nu}."""
        return np.einsum('ar,rbmn->abmn', g, self.data)

    def check_algebraic_symmetries(self, g: np.ndarray, tol: float = 1e-5) -> bool:
        """Check R_{abmn} symmetries: R_abmn = -R_abnm = -R_bamn = R_mnab and first Bianchi."""
        r_cov = self.lower_first_index(g)
        dim = self.dim
        for a in range(dim):
            for b in range(dim):
                for m in range(dim):
                    for n in range(dim):
                        if abs(r_cov[a, b, m, n] + r_cov[a, b, n, m]) > tol:
                            return False
                        if abs(r_cov[a, b, m, n] + r_cov[b, a, m, n]) > tol:
                            return False
                        if abs(r_cov[a, b, m, n] - r_cov[m, n, a, b]) > tol:
                            return False
                        bianchi1 = r_cov[a, b, m, n] + r_cov[a, m, n, b] + r_cov[a, n, b, m]
                        if abs(bianchi1) > tol:
                            return False
        return True
