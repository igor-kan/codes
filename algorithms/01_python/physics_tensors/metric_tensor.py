"""Metric Tensor g_{mu nu} and Inverse Metric g^{mu nu}.

Handles index raising/lowering, metric signatures, invariant intervals, and determinants.
"""

from typing import Sequence, Tuple
import numpy as np
try:
    from .tensor_base import Tensor
except ImportError:
    from tensor_base import Tensor


class MetricTensor:
    """Rank-2 Covariant Metric Tensor g_{mu nu}."""

    def __init__(self, matrix: Sequence[Sequence[float]]):
        self.g = np.array(matrix, dtype=np.float64)
        if self.g.ndim != 2 or self.g.shape[0] != self.g.shape[1]:
            raise ValueError("Metric must be a square 2D matrix")
        if not np.allclose(self.g, self.g.T):
            raise ValueError("Metric tensor must be symmetric")

        self.dim = self.g.shape[0]
        self.det = float(np.linalg.det(self.g))
        if abs(self.det) < 1e-15:
            raise ValueError("Metric tensor must be non-degenerate (det != 0)")
        self.inv_g = np.linalg.inv(self.g)

    @property
    def signature(self) -> Tuple[int, int]:
        """Returns (p, q) count of positive and negative eigenvalues."""
        evals = np.linalg.eigvalsh(self.g)
        pos = int(np.sum(evals > 1e-10))
        neg = int(np.sum(evals < -1e-10))
        return pos, neg

    def line_element(self, dx: Sequence[float]) -> float:
        """Calculate ds^2 = g_{mu nu} dx^mu dx^nu."""
        dx_arr = np.array(dx, dtype=np.float64)
        return float(dx_arr @ self.g @ dx_arr)

    def lower_index(self, v_upper: Sequence[float]) -> np.ndarray:
        """Lower vector index: v_mu = g_{mu nu} v^nu."""
        return self.g @ np.array(v_upper, dtype=np.float64)

    def raise_index(self, w_lower: Sequence[float]) -> np.ndarray:
        """Raise 1-form index: w^mu = g^{mu nu} w_nu."""
        return self.inv_g @ np.array(w_lower, dtype=np.float64)

    def inner_product(self, u: Sequence[float], v: Sequence[float]) -> float:
        """Compute g(u, v) = g_{mu nu} u^mu v^nu."""
        u_arr = np.array(u, dtype=np.float64)
        v_arr = np.array(v, dtype=np.float64)
        return float(u_arr @ self.g @ v_arr)

    def to_tensor(self) -> Tensor:
        return Tensor(self.g, valence=(0, 2), dim=self.dim)

    def inverse_to_tensor(self) -> Tensor:
        return Tensor(self.inv_g, valence=(2, 0), dim=self.dim)
