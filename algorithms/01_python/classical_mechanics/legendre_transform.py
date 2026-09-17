"""Fenchel-Legendre Duality between Lagrangian L(q, dot{q}) and Hamiltonian H(q, p).

Implements Arnold §14: p_i = dL/d dot{q}^i, H(q, p) = p dot{q} - L, and Hessian strict convexity check.
"""

from typing import Callable, Sequence
import numpy as np
from scipy.optimize import root


class LegendreTransform:
    """Legendre involution connecting Lagrangian and Hamiltonian formalisms."""

    def __init__(self, lagrangian: Callable[[np.ndarray, np.ndarray], float], degrees_of_freedom: int, eps: float = 1e-5):
        self.lagrangian = lagrangian
        self.n = degrees_of_freedom
        self.eps = eps

    def generalized_momentum(self, q: Sequence[float], q_dot: Sequence[float]) -> np.ndarray:
        """p_i = dL / d dot{q}^i."""
        q_arr = np.array(q, dtype=np.float64)
        qd_arr = np.array(q_dot, dtype=np.float64)
        p = np.zeros(self.n, dtype=np.float64)
        for i in range(self.n):
            qdp = qd_arr.copy()
            qdm = qd_arr.copy()
            qdp[i] += self.eps
            qdm[i] -= self.eps
            p[i] = (self.lagrangian(q_arr, qdp) - self.lagrangian(q_arr, qdm)) / (2.0 * self.eps)
        return p

    def hessian_convexity_check(self, q: Sequence[float], q_dot: Sequence[float]) -> bool:
        """Verify that d^2 L / d dot{q}^i d dot{q}^j is strictly positive definite."""
        q_arr = np.array(q, dtype=np.float64)
        qd_arr = np.array(q_dot, dtype=np.float64)
        hess = np.zeros((self.n, self.n), dtype=np.float64)
        for i in range(self.n):
            for j in range(self.n):
                qpp = qd_arr.copy()
                qpm = qd_arr.copy()
                qmp = qd_arr.copy()
                qmm = qd_arr.copy()
                qpp[i] += self.eps
                qpp[j] += self.eps
                qpm[i] += self.eps
                qpm[j] -= self.eps
                qmp[i] -= self.eps
                qmp[j] += self.eps
                qmm[i] -= self.eps
                qmm[j] -= self.eps
                hess[i, j] = (
                    self.lagrangian(q_arr, qpp) - self.lagrangian(q_arr, qpm) -
                    self.lagrangian(q_arr, qmp) + self.lagrangian(q_arr, qmm)
                ) / (4.0 * (self.eps**2))
        evals = np.linalg.eigvalsh(hess)
        return bool(np.all(evals > 1e-8))

    def evaluate_hamiltonian(self, q: Sequence[float], p: Sequence[float], q_dot_guess: Sequence[float]) -> float:
        """H(q, p) = p dot{q} - L(q, dot{q}) solving p = dL/d dot{q} for dot{q}."""
        q_arr = np.array(q, dtype=np.float64)
        p_target = np.array(p, dtype=np.float64)

        def res(qd):
            return self.generalized_momentum(q_arr, qd) - p_target

        sol = root(res, np.array(q_dot_guess, dtype=np.float64))
        if np.linalg.norm(res(sol.x)) > 1e-4:
            raise RuntimeError("Legendre transform root-finding failed for generalized velocities")
        qd_star = sol.x
        return float(np.dot(p_target, qd_star) - self.lagrangian(q_arr, qd_star))
