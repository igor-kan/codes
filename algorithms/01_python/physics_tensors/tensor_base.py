"""General Multi-Index Tensor Representation with Covariant and Contravariant Indices.

Supports tensor valence (p, q), contractions, outer product, and Einstein summation.
"""

from typing import Tuple, Sequence, Optional
import numpy as np


class Tensor:
    """Multi-index Tensor with valence (p, q).

    p: number of contravariant (upper) indices.
    q: number of covariant (lower) indices.
    """

    def __init__(self, data: Sequence, valence: Tuple[int, int] = (0, 0), dim: Optional[int] = None):
        self.data = np.array(data, dtype=np.float64)
        self.valence = valence  # (p, q)
        p, q = valence
        rank = p + q
        if rank == 0 and self.data.ndim == 0:
            self.dim = dim or 0
        else:
            if self.data.ndim != rank:
                raise ValueError(f"Data ndim {self.data.ndim} does not match rank p+q={rank}")
            self.dim = self.data.shape[0] if rank > 0 else (dim or 0)
            for s in self.data.shape:
                if s != self.dim:
                    raise ValueError("All dimensions must be equal for a tensor over a fixed manifold dimension")

    @property
    def rank(self) -> int:
        return self.valence[0] + self.valence[1]

    @property
    def p(self) -> int:
        return self.valence[0]

    @property
    def q(self) -> int:
        return self.valence[1]

    def contract(self, upper_idx: int, lower_idx: int) -> 'Tensor':
        """Contract upper index upper_idx with lower index lower_idx."""
        p, q = self.valence
        if upper_idx < 0 or upper_idx >= p:
            raise IndexError(f"upper_idx {upper_idx} out of range [0, {p-1}]")
        actual_lower = p + lower_idx
        if lower_idx < 0 or actual_lower >= p + q:
            raise IndexError(f"lower_idx {lower_idx} out of range [0, {q-1}]")

        res_data = np.trace(self.data, axis1=upper_idx, axis2=actual_lower)
        return Tensor(res_data, valence=(p - 1, q - 1), dim=self.dim)

    def tensor_product(self, other: 'Tensor') -> 'Tensor':
        """Compute outer product T ⊗ S."""
        if self.dim != other.dim and self.dim != 0 and other.dim != 0:
            raise ValueError(f"Incompatible manifold dimensions: {self.dim} vs {other.dim}")
        dim = max(self.dim, other.dim)
        p1, q1 = self.valence
        p2, q2 = other.valence
        raw_outer = np.tensordot(self.data, other.data, axes=0)
        perm = (
            list(range(0, p1)) +
            list(range(p1 + q1, p1 + q1 + p2)) +
            list(range(p1, p1 + q1)) +
            list(range(p1 + q1 + p2, p1 + q1 + p2 + q2))
        )
        new_data = np.transpose(raw_outer, perm) if raw_outer.ndim > 1 else raw_outer
        return Tensor(new_data, valence=(p1 + p2, q1 + q2), dim=dim)

    def __add__(self, other: 'Tensor') -> 'Tensor':
        if self.valence != other.valence:
            raise ValueError(f"Cannot add tensors with different valences: {self.valence} vs {other.valence}")
        return Tensor(self.data + other.data, valence=self.valence, dim=self.dim)

    def __sub__(self, other: 'Tensor') -> 'Tensor':
        if self.valence != other.valence:
            raise ValueError(f"Cannot subtract tensors with different valences: {self.valence} vs {other.valence}")
        return Tensor(self.data - other.data, valence=self.valence, dim=self.dim)

    def __mul__(self, scalar: float) -> 'Tensor':
        return Tensor(self.data * scalar, valence=self.valence, dim=self.dim)

    def __rmul__(self, scalar: float) -> 'Tensor':
        return self.__mul__(scalar)

    def to_numpy(self) -> np.ndarray:
        return self.data.copy()
