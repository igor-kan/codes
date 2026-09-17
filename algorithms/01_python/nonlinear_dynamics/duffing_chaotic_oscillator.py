"""Duffing Chaotic Oscillator with periodic forcing."""

from typing import Tuple
import numpy as np


class DuffingOscillator:
    """Forced damped nonlinear oscillator:
    d^2 x / dt^2 + delta * dx/dt + alpha * x + beta * x^3 = gamma * cos(omega * t)
    """

    def __init__(
        self, delta: float = 0.2, alpha: float = -1.0, beta: float = 1.0, gamma: float = 0.3, omega: float = 1.0
    ):
        self.delta = delta
        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma
        self.omega = omega

    def derivatives(self, state: np.ndarray, t: float) -> np.ndarray:
        x, v = state
        dx = v
        dv = -self.delta * v - self.alpha * x - self.beta * (x**3) + self.gamma * np.cos(self.omega * t)
        return np.array([dx, dv])

    def integrate_rk4(self, state0: np.ndarray, dt: float, steps: int) -> Tuple[np.ndarray, np.ndarray]:
        t = np.linspace(0, steps * dt, steps + 1)
        trajectory = np.zeros((steps + 1, 2))
        trajectory[0] = state0
        curr = state0.copy()

        for i in range(steps):
            ti = t[i]
            k1 = self.derivatives(curr, ti)
            k2 = self.derivatives(curr + 0.5 * dt * k1, ti + 0.5 * dt)
            k3 = self.derivatives(curr + 0.5 * dt * k2, ti + 0.5 * dt)
            k4 = self.derivatives(curr + dt * k3, ti + dt)
            curr += (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
            trajectory[i + 1] = curr

        return t, trajectory
