"""Contact Geometry (M^{2n+1}, alpha), Reeb Vector Fields, and Dissipative Classical Mechanics.

Implements Arnold Appendix 4: contact 1-form alpha wedge (d alpha)^n != 0, Reeb field i_R d alpha = 0, alpha(R) = 1.
"""

from typing import Sequence
import numpy as np


class ContactGeometry:
    """Odd-dimensional contact manifold with 1-form alpha."""

    def __init__(self, degrees_of_freedom: int):
        self.n = degrees_of_freedom
        self.dim = 2 * degrees_of_freedom + 1  # Coordinates (q_1..q_n, p_1..p_n, s)

    def standard_contact_form(self, q: Sequence[float], p: Sequence[float], ds: float,
                              dq: Sequence[float], dp: Sequence[float]) -> float:
        """Standard contact 1-form alpha = ds - sum p_i dq^i."""
        p_arr = np.array(p, dtype=np.float64)
        dq_arr = np.array(dq, dtype=np.float64)
        return float(ds - np.dot(p_arr, dq_arr))

    def reeb_vector_field(self) -> np.ndarray:
        """Standard Reeb vector field R = d / ds = (0, ..., 0, 1)."""
        r = np.zeros(self.dim, dtype=np.float64)
        r[-1] = 1.0
        return r
