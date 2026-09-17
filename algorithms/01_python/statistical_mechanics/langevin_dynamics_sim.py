"""Langevin Stochastic Differential Equation for Brownian Motion.

Simulates m dot{v} = - gamma v + sqrt(2 gamma k_B T) xi(t) with fluctuation-dissipation theorem.
"""

from typing import Tuple
import numpy as np


class LangevinDynamics:
    """Langevin stochastic particle integrator."""

    def __init__(self, mass: float, friction: float, temperature: float, k_b: float = 1.0):
        self.m = mass
        self.gamma = friction
        self.t = temperature
        self.kb = k_b
        # Noise strength sigma = sqrt(2 gamma k_B T)
        self.sigma = np.sqrt(2.0 * self.gamma * self.kb * self.t)

    def step(self, x: float, v: float, dt: float) -> Tuple[float, float]:
        """Euler-Maruyama step."""
        noise = np.random.normal(0.0, np.sqrt(dt))
        dv = (- (self.gamma / self.m) * v) * dt + (self.sigma / self.m) * noise
        v_next = v + dv
        x_next = x + v_next * dt
        return x_next, v_next
