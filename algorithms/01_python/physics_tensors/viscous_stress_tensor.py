"""Viscous Deviatoric Stress Tensor tau_{ij} in Fluid Dynamics.

Computes Navier-Stokes viscous stresses and viscous dissipation function Phi >= 0.
"""

from typing import Sequence
import numpy as np


class ViscousStressTensor:
    """Newtonian viscous stress tensor tau_{ij}."""

    def __init__(self, shear_viscosity: float, bulk_viscosity: float = 0.0):
        self.mu = shear_viscosity
        self.zeta = bulk_viscosity

    def stress_from_velocity_gradient(self, grad_v: Sequence[Sequence[float]]) -> np.ndarray:
        """tau_{ij} = 2 mu (S_{ij} - 1/3 div(v) delta_{ij}) + zeta div(v) delta_{ij}."""
        l = np.array(grad_v, dtype=np.float64)
        s = 0.5 * (l + l.T)
        div_v = float(np.trace(s))
        s_dev = s - (div_v / 3.0) * np.eye(3)
        return 2.0 * self.mu * s_dev + self.zeta * div_v * np.eye(3)

    def dissipation_function(self, grad_v: Sequence[Sequence[float]]) -> float:
        """Phi = tau_{ij} (d v_i / d x_j) >= 0."""
        tau = self.stress_from_velocity_gradient(grad_v)
        l = np.array(grad_v, dtype=np.float64)
        return float(np.einsum('ij,ij->', tau, l))
