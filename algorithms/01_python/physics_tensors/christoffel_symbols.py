"""Christoffel Symbols of the First and Second Kind.

Computes Gamma^lambda_{mu nu} from metric derivatives and implements the geodesic equation.
"""

from typing import Callable, Sequence
import numpy as np


class ChristoffelSymbols:
    """Christoffel symbols of the second kind: Gamma^lambda_{mu nu}."""

    def __init__(self, gamma: np.ndarray):
        self.gamma = np.array(gamma, dtype=np.float64)
        if self.gamma.ndim != 3:
            raise ValueError("Christoffel symbols must be a 3D array (dim, dim, dim)")
        self.dim = self.gamma.shape[0]
        for lam in range(self.dim):
            if not np.allclose(self.gamma[lam], self.gamma[lam].T, atol=1e-8):
                raise ValueError("Christoffel symbols must be symmetric in lower indices (Levi-Civita connection)")

    @classmethod
    def from_metric_field(cls, metric_func: Callable[[np.ndarray], np.ndarray],
                           x: Sequence[float], eps: float = 1e-6) -> 'ChristoffelSymbols':
        """Compute Gamma^lambda_{mu nu} numerically at position x using finite differences."""
        x_arr = np.array(x, dtype=np.float64)
        dim = len(x_arr)
        g = metric_func(x_arr)
        inv_g = np.linalg.inv(g)

        d_g = np.zeros((dim, dim, dim), dtype=np.float64)
        for s in range(dim):
            x_plus = x_arr.copy()
            x_minus = x_arr.copy()
            x_plus[s] += eps
            x_minus[s] -= eps
            d_g[s] = (metric_func(x_plus) - metric_func(x_minus)) / (2.0 * eps)

        gamma = np.zeros((dim, dim, dim), dtype=np.float64)
        for lam in range(dim):
            for mu in range(dim):
                for nu in range(dim):
                    for sig in range(dim):
                        gamma[lam, mu, nu] += 0.5 * inv_g[lam, sig] * (
                            d_g[mu, sig, nu] + d_g[nu, sig, mu] - d_g[sig, mu, nu]
                        )
        return cls(gamma)

    def geodesic_acceleration(self, velocity: Sequence[float]) -> np.ndarray:
        """Compute geodesic acceleration d^2 x^lambda / d tau^2 = - Gamma^lambda_{mu nu} v^mu v^nu."""
        v = np.array(velocity, dtype=np.float64)
        accel = np.zeros(self.dim, dtype=np.float64)
        for lam in range(self.dim):
            accel[lam] = - float(v @ self.gamma[lam] @ v)
        return accel

    def covariant_derivative_vector(self, v: Sequence[float], grad_v: np.ndarray) -> np.ndarray:
        """Compute nabla_mu v^nu = d_mu v^nu + Gamma^nu_{mu lambda} v^lambda."""
        v_arr = np.array(v, dtype=np.float64)
        res = grad_v.copy()
        for mu in range(self.dim):
            for nu in range(self.dim):
                for lam in range(self.dim):
                    res[mu, nu] += self.gamma[nu, mu, lam] * v_arr[lam]
        return res
