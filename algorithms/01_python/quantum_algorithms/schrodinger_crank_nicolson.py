"""Unitary Crank-Nicolson Solver for 1D Time-Dependent Schrodinger Equation.

Solves i hbar d psi / dt = - (hbar^2 / 2m) d^2 psi / dx^2 + V(x) psi unconditionally preserving norm ||psi|| = 1.
"""

from typing import Callable, Sequence, Tuple
import numpy as np


class CrankNicolsonSchrodinger:
    """Unconditionally unitary PDE solver."""

    def __init__(self, x_grid: Sequence[float], potential_vals: Sequence[float],
                 mass: float = 1.0, hbar: float = 1.0):
        self.x = np.array(x_grid, dtype=np.float64)
        self.v = np.array(potential_vals, dtype=np.float64)
        self.dx = self.x[1] - self.x[0]
        self.n = len(self.x)
        self.m = mass
        self.hbar = hbar

    def step(self, psi: np.ndarray, dt: float) -> np.ndarray:
        """Execute one time step via Cayley form (I + i dt/2 H) psi^{n+1} = (I - i dt/2 H) psi^n."""
        diag = (self.hbar**2) / (self.m * (self.dx**2)) + self.v
        off_diag = - 0.5 * (self.hbar**2) / (self.m * (self.dx**2))

        # Hamiltonian matrix H
        h_mat = np.diag(diag) + np.diag(np.full(self.n - 1, off_diag), 1) + np.diag(np.full(self.n - 1, off_diag), -1)

        a_mat = np.eye(self.n, dtype=np.complex128) + 0.5j * (dt / self.hbar) * h_mat
        b_mat = np.eye(self.n, dtype=np.complex128) - 0.5j * (dt / self.hbar) * h_mat

        rhs = b_mat @ psi
        return np.linalg.solve(a_mat, rhs)
