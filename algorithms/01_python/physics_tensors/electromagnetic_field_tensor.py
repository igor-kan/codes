"""Electromagnetic Faraday Tensor F_{mu nu} and Dual Tensor *F^{mu nu}.

Encapsulates electric and magnetic fields into a relativistic antisymmetric rank-2 tensor.
"""

from typing import Sequence, Tuple
import numpy as np


class ElectromagneticFieldTensor:
    """Faraday 2-form tensor F_{mu nu}."""

    def __init__(self, e_field: Sequence[float], b_field: Sequence[float], c: float = 1.0):
        ex, ey, ez = e_field
        bx, by, bz = b_field
        self.c = c
        self.f = np.array([
            [0.0, -ex / c, -ey / c, -ez / c],
            [ex / c, 0.0, bz, -by],
            [ey / c, -bz, 0.0, bx],
            [ez / c, by, -bx, 0.0]
        ], dtype=np.float64)

    @property
    def matrix(self) -> np.ndarray:
        return self.f

    def lorentz_invariants(self) -> Tuple[float, float]:
        """Compute I_1 = F_{mu nu} F^{mu nu} and I_2 = F_{mu nu} *F^{mu nu}."""
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        inv_eta = eta
        f_up = inv_eta @ self.f @ inv_eta
        i1 = float(np.einsum('mn,mn->', self.f, f_up))

        ex, ey, ez = self.f[1:, 0] * self.c
        bx, by, bz = self.f[3, 2], self.f[1, 3], self.f[2, 1]
        e = np.array([ex, ey, ez])
        b = np.array([bx, by, bz])
        i2 = float(-4.0 * np.dot(e, b) / self.c)
        return i1, i2
