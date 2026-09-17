"""Fokker-Planck 1D Probability Density Evolution.

Solves d P / dt = - d/dx (A(x) P) + 1/2 d^2/dx^2 (B(x) P) using conservative finite differences.
"""

from typing import Callable, Sequence
import numpy as np


class FokkerPlanck1D:
    """1D Fokker-Planck PDE solver."""

    def __init__(self, x_grid: Sequence[float], drift_a: Callable[[float], float], diffusion_b: float):
        self.x = np.array(x_grid, dtype=np.float64)
        self.dx = self.x[1] - self.x[0]
        self.a_func = drift_a
        self.b_const = diffusion_b
        self.n = len(self.x)

    def step(self, p: np.ndarray, dt: float) -> np.ndarray:
        """Explicit conservative time step."""
        p_next = p.copy()
        # Flux J = A P - 1/2 B dP/dx
        j = np.zeros(self.n + 1)
        for i in range(1, self.n):
            a_mid = self.a_func(0.5 * (self.x[i - 1] + self.x[i]))
            dp_dx = (p[i] - p[i - 1]) / self.dx
            p_mid = 0.5 * (p[i - 1] + p[i])
            j[i] = a_mid * p_mid - 0.5 * self.b_const * dp_dx

        for i in range(self.n):
            p_next[i] -= (dt / self.dx) * (j[i + 1] - j[i])
        return p_next
