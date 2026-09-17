"""Van der Pol Non-linear Relaxation Oscillator."""

import numpy as np


class VanDerPolOscillator:
    """Nonlinear oscillator with non-conservative damping:
    d^2 x / dt^2 - mu * (1 - x^2) * dx/dt + x = 0
    """

    def __init__(self, mu: float = 1.0):
        self.mu = mu

    def derivatives(self, state: np.ndarray) -> np.ndarray:
        x, v = state
        dx = v
        dv = self.mu * (1.0 - x**2) * v - x
        return np.array([dx, dv])

    def integrate(self, state0: np.ndarray, dt: float = 0.01, steps: int = 1000) -> np.ndarray:
        trajectory = np.zeros((steps + 1, 2))
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
