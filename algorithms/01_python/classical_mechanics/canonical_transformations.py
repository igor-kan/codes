"""Canonical Transformations and Generating Functions (F1, F2, F3, F4).

Implements Arnold §45 and Landau §45: (q, p) -> (Q, P) preserving Poisson brackets and symplectic form.
"""

from typing import Callable, Sequence, Tuple
import numpy as np


class CanonicalTransformation:
    """Canonical transformations via generating functions."""

    def __init__(self, degrees_of_freedom: int, eps: float = 1e-5):
        self.n = degrees_of_freedom
        self.eps = eps

    def from_f1(self, f1: Callable[[np.ndarray, np.ndarray], float],
                q: Sequence[float], q_new: Sequence[float]) -> Tuple[np.ndarray, np.ndarray]:
        """Type 1 generating function F_1(q, Q): p_i = dF_1/dq_i, P_i = - dF_1/dQ_i."""
        q_arr = np.array(q, dtype=np.float64)
        qn_arr = np.array(q_new, dtype=np.float64)

        p = np.zeros(self.n, dtype=np.float64)
        p_new = np.zeros(self.n, dtype=np.float64)

        for i in range(self.n):
            qp = q_arr.copy()
            qm = q_arr.copy()
            qp[i] += self.eps
            qm[i] -= self.eps
            p[i] = (f1(qp, qn_arr) - f1(qm, qn_arr)) / (2.0 * self.eps)

            qnp = qn_arr.copy()
            qnm = qn_arr.copy()
            qnp[i] += self.eps
            qnm[i] -= self.eps
            p_new[i] = - (f1(q_arr, qnp) - f1(q_arr, qnm)) / (2.0 * self.eps)

        return p, p_new

    def from_f2(self, f2: Callable[[np.ndarray, np.ndarray], float],
                q: Sequence[float], p_new: Sequence[float]) -> Tuple[np.ndarray, np.ndarray]:
        """Type 2 generating function F_2(q, P): p_i = dF_2/dq_i, Q_i = dF_2/dP_i."""
        q_arr = np.array(q, dtype=np.float64)
        pn_arr = np.array(p_new, dtype=np.float64)

        p = np.zeros(self.n, dtype=np.float64)
        q_new = np.zeros(self.n, dtype=np.float64)

        for i in range(self.n):
            qp = q_arr.copy()
            qm = q_arr.copy()
            qp[i] += self.eps
            qm[i] -= self.eps
            p[i] = (f2(qp, pn_arr) - f2(qm, pn_arr)) / (2.0 * self.eps)

            pnp = pn_arr.copy()
            pnm = pn_arr.copy()
            pnp[i] += self.eps
            pnm[i] -= self.eps
            q_new[i] = (f2(q_arr, pnp) - f2(q_arr, pnm)) / (2.0 * self.eps)

        return p, q_new
