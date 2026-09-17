"""2D Incompressible Navier-Stokes in Vorticity-Streamfunction Formulation.

Solves d omega / dt + u d omega / dx + v d omega / dy = nu nabla^2 omega, nabla^2 psi = - omega.
"""

from typing import Tuple
import numpy as np


class VorticityStreamfunction2D:
    """2D incompressible Navier-Stokes solver on uniform grid."""

    def __init__(self, nx: int, ny: int, dx: float, kinematic_viscosity: float):
        self.nx = nx
        self.ny = ny
        self.dx = dx
        self.nu = kinematic_viscosity
        self.omega = np.zeros((nx, ny), dtype=np.float64)
        self.psi = np.zeros((nx, ny), dtype=np.float64)

    def velocities_from_streamfunction(self) -> Tuple[np.ndarray, np.ndarray]:
        """u = d psi / dy, v = - d psi / dx."""
        u = np.zeros_like(self.psi)
        v = np.zeros_like(self.psi)
        u[:, 1:-1] = (self.psi[:, 2:] - self.psi[:, :-2]) / (2.0 * self.dx)
        v[1:-1, :] = - (self.psi[2:, :] - self.psi[:-2, :]) / (2.0 * self.dx)
        return u, v
