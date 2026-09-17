"""Lorenz Attractor RK4 numerical integrator."""

from typing import Tuple
import numpy as np


class LorenzAttractor:
    """Simulates the classical Lorenz system:
    dx/dt = sigma * (y - x)
    dy/dt = x * (rho - z) - y
    dz/dt = x * y - beta * z
    """

    def __init__(self, sigma: float = 10.0, rho: float = 28.0, beta: float = 8.0 / 3.0):
        self.sigma = sigma
        self.rho = rho
        self.beta = beta

    def derivatives(self, state: np.ndarray) -> np.ndarray:
        x, y, z = state
        dx = self.sigma * (y - x)
        dy = x * (self.rho - z) - y
        dz = x * y - self.beta * z
        return np.array([dx, dy, dz])

    def integrate(self, state0: np.ndarray, dt: float = 0.01, steps: int = 1000) -> np.ndarray:
        trajectory = np.zeros((steps + 1, 3))
        trajectory[0] = state0
        curr = state0.copy()

        for i in range(steps):
            k1 = self.derivatives(curr)
            k2 = self.derivatives(curr + 0.5 * dt * k1)
            k3 = self.derivatives(curr + 0.5 * dt * k2)
            k4 = self.derivatives(curr + dt * k3)
            curr += (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            trajectory[i + 1] = curr

        return trajectory
