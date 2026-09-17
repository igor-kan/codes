"""Kinetic Boltzmann Transport Equation with BGK Relaxation Operator.

Simulates df/dt + v df/dx = - (f - f_0) / tau for non-equilibrium gas relaxation.
"""

import numpy as np


class BoltzmannBGK1D:
    """1D kinetic relaxation simulator."""

    def __init__(self, relaxation_time: float):
        self.tau = relaxation_time

    def relax_step(self, f_dist: np.ndarray, f_eq: np.ndarray, dt: float) -> np.ndarray:
        """f(t + dt) = f + (dt / tau) (f_eq - f)."""
        return f_dist + (dt / self.tau) * (f_eq - f_dist)
