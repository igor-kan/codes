"""Hamiltonian Vector Field X_H and Liouville's Theorem on Phase Volume Conservation.

Implements Arnold §16: i_{X_H} omega = -dH, flow equations dot{z} = X_H(z), and div(X_H) = 0.
"""

from typing import Callable, Sequence
import numpy as np


class HamiltonianVectorField:
    """Generates Hamiltonian vector fields and phase flows."""

    def __init__(self, hamiltonian: Callable[[np.ndarray], float], degrees_of_freedom: int, eps: float = 1e-5):
        self.h = hamiltonian
        self.n = degrees_of_freedom
        self.dim = 2 * degrees_of_freedom
        self.eps = eps

    def vector_field(self, z: Sequence[float]) -> np.ndarray:
        """Compute X_H(z) = (dH/dp, -dH/dq)^T."""
        z_arr = np.array(z, dtype=np.float64)
        grad = np.zeros(self.dim, dtype=np.float64)
        for i in range(self.dim):
            zp = z_arr.copy()
            zm = z_arr.copy()
            zp[i] += self.eps
            zm[i] -= self.eps
            grad[i] = (self.h(zp) - self.h(zm)) / (2.0 * self.eps)

        dh_dq = grad[:self.n]
        dh_dp = grad[self.n:]
        # dot{q} = dH/dp, dot{p} = -dH/dq
        return np.concatenate([dh_dp, -dh_dq])

    def divergence(self, z: Sequence[float]) -> float:
        """Compute div(X_H) = sum_i (d^2 H / dq_i dp_i - d^2 H / dp_i dq_i) == 0 (Liouville)."""
        z_arr = np.array(z, dtype=np.float64)
        div_val = 0.0
        for i in range(self.dim):
            zp = z_arr.copy()
            zm = z_arr.copy()
            zp[i] += self.eps
            zm[i] -= self.eps
            v_plus = self.vector_field(zp)[i]
            v_minus = self.vector_field(zm)[i]
            div_val += (v_plus - v_minus) / (2.0 * self.eps)
        return float(div_val)
