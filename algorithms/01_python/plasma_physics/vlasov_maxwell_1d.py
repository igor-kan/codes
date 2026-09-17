"""1D Vlasov Kinetic Equation via Split-Operator Advection.

Solves df/dt + v df/dx - (e/m) E df/dv = 0 on phase space grid (x, v).
"""

from typing import Tuple
import numpy as np


class Vlasov1D:
    """1D Vlasov phase space solver."""

    def __init__(self, nx: int, nv: int, dx: float, dv: float):
        self.nx = nx
        self.nv = nv
        self.dx = dx
        self.dv = dv
        self.f = np.zeros((nx, nv), dtype=np.float64)

    def advect_x(self, v_grid: np.ndarray, dt: float):
        """Advect in space: f(x, v) -> f(x - v dt, v)."""
        for j, v_val in enumerate(v_grid):
            shift = int(np.round(v_val * dt / self.dx))
            self.f[:, j] = np.roll(self.f[:, j], shift)
