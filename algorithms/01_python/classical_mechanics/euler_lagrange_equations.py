"""Euler-Lagrange Equations and Cyclic Coordinates in Configuration Space.

Implements variational mechanics: d/dt(dL/d dot{q}^i) - dL/dq^i = 0 (Landau Vol 1 Ch. 1, Goldstein Ch. 1-2).
"""

from typing import Callable, Sequence, List
import numpy as np


class EulerLagrangeSystem:
    """Euler-Lagrange equations solver and cyclic coordinate identification."""

    def __init__(self, lagrangian: Callable[[np.ndarray, np.ndarray, float], float], degrees_of_freedom: int, eps: float = 1e-5):
        self.l = lagrangian
        self.n = degrees_of_freedom
        self.eps = eps

    def generalized_forces(self, q: Sequence[float], q_dot: Sequence[float], t: float = 0.0) -> np.ndarray:
        """Partial derivatives dL/dq^i."""
        q_arr = np.array(q, dtype=np.float64)
        qd_arr = np.array(q_dot, dtype=np.float64)
        forces = np.zeros(self.n, dtype=np.float64)
        for i in range(self.n):
            qp = q_arr.copy()
            qm = q_arr.copy()
            qp[i] += self.eps
            qm[i] -= self.eps
            forces[i] = (self.l(qp, qd_arr, t) - self.l(qm, qd_arr, t)) / (2.0 * self.eps)
        return forces

    def cyclic_coordinates(self, q_sample: Sequence[float], q_dot_sample: Sequence[float], tol: float = 1e-6) -> List[int]:
        """Identifies cyclic (ignorable) coordinates where dL/dq^k == 0 (conserved conjugate momentum)."""
        forces = self.generalized_forces(q_sample, q_dot_sample)
        return [i for i, f in enumerate(forces) if abs(f) < tol]
