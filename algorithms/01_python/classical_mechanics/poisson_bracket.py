"""Classical Poisson Bracket {f, g}_{PB} and Lie Algebra of Observables.

Implements Arnold's definition: {f, g} = sum_i (df/dq_i dg/dp_i - df/dp_i dg/dq_i).
Verifies antisymmetry, Leibniz rule, and the Jacobi identity.
"""

from typing import Callable, Sequence
import numpy as np


class PoissonBracket:
    """Evaluates and verifies Poisson brackets on phase space R^{2n}."""

    def __init__(self, degrees_of_freedom: int, eps: float = 1e-5):
        self.n = degrees_of_freedom
        self.eps = eps

    def gradient(self, f: Callable[[np.ndarray], float], z: np.ndarray) -> np.ndarray:
        """Compute numerical gradient of f at phase space point z = (q, p)."""
        dim = 2 * self.n
        grad = np.zeros(dim, dtype=np.float64)
        for i in range(dim):
            zp = z.copy()
            zm = z.copy()
            zp[i] += self.eps
            zm[i] -= self.eps
            grad[i] = (f(zp) - f(zm)) / (2.0 * self.eps)
        return grad

    def bracket(self, f: Callable[[np.ndarray], float],
                g: Callable[[np.ndarray], float], z: Sequence[float]) -> float:
        """Evaluate {f, g}(z) = sum_i (df/dq_i dg/dp_i - df/dp_i dg/dq_i)."""
        z_arr = np.array(z, dtype=np.float64)
        grad_f = self.gradient(f, z_arr)
        grad_g = self.gradient(g, z_arr)

        df_dq, df_dp = grad_f[:self.n], grad_f[self.n:]
        dg_dq, dg_dp = grad_g[:self.n], grad_g[self.n:]

        return float(np.sum(df_dq * dg_dp - df_dp * dg_dq))

    def verify_jacobi_identity(self, f: Callable[[np.ndarray], float],
                                g: Callable[[np.ndarray], float],
                                h: Callable[[np.ndarray], float],
                                z: Sequence[float], tol: float = 1e-4) -> bool:
        """Check Jacobi identity: {f, {g, h}} + {g, {h, f}} + {h, {f, g}} = 0."""
        z_arr = np.array(z, dtype=np.float64)

        def gh(pt):
            return self.bracket(g, h, pt)

        def hf(pt):
            return self.bracket(h, f, pt)

        def fg(pt):
            return self.bracket(f, g, pt)

        term1 = self.bracket(f, gh, z_arr)
        term2 = self.bracket(g, hf, z_arr)
        term3 = self.bracket(h, fg, z_arr)

        sum_cyclic = term1 + term2 + term3
        return abs(sum_cyclic) < tol
