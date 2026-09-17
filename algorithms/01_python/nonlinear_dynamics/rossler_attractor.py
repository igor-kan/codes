"""Rössler Chaotic Attractor."""

import numpy as np


class RosslerAttractor:
    """Simulates the Rössler system:
    dx/dt = -y - z
    dy/dt = x + a * y
    dz/dt = b + z * (x - c)
    """

    def __init__(self, a: float = 0.2, b: float = 0.2, c: float = 5.7):
        self.a = a
        self.b = b
        self.c = c

    def derivatives(self, state: np.ndarray) -> np.ndarray:
        x, y, z = state
        dx = -y - z
        dy = x + self.a * y
        dz = self.b + z * (x - self.c)
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
