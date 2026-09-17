"""Kuramoto Model of Coupled Phase Oscillators."""

from typing import Tuple
import numpy as np


class KuramotoModel:
    """Simulates N globally coupled phase oscillators:
    dtheta_i/dt = omega_i + (K / N) * sum_j sin(theta_j - theta_i)
    """

    def __init__(self, natural_frequencies: np.ndarray, coupling_k: float):
        self.omega = natural_frequencies
        self.k = coupling_k
        self.n = len(natural_frequencies)

    def order_parameter(self, theta: np.ndarray) -> Tuple[float, float]:
        """Calculates complex order parameter r * exp(i * psi) = (1/N) * sum(exp(i * theta_j)).

        Returns:
            (r, psi) where r in [0, 1] measures phase coherence.
        """
        z = np.mean(np.exp(1j * theta))
        return float(np.abs(z)), float(np.angle(z))

    def derivatives(self, theta: np.ndarray) -> np.ndarray:
        r, psi = self.order_parameter(theta)
        # Using identity: (1/N) sum sin(theta_j - theta_i) = r * sin(psi - theta_i)
        return self.omega + self.k * r * np.sin(psi - theta)

    def step_rk4(self, theta: np.ndarray, dt: float) -> np.ndarray:
        k1 = self.derivatives(theta)
        k2 = self.derivatives(theta + 0.5 * dt * k1)
        k3 = self.derivatives(theta + 0.5 * dt * k2)
        k4 = self.derivatives(theta + dt * k3)
        return theta + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
