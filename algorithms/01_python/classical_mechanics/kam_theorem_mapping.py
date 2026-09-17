"""Kolmogorov-Arnold-Moser (KAM) Theorem and the Chirikov Standard Map.

Implements area-preserving symplectic standard mapping:
p_{n+1} = p_n + K sin(theta_n) mod 2 pi
theta_{n+1} = theta_n + p_{n+1} mod 2 pi
Demonstrates persistence of invariant tori for small K and transition to global chaos at K_c approx 0.9716.
"""

from typing import Tuple
import numpy as np


class ChirikovStandardMap:
    """Chirikov standard map and symplectic area preservation."""

    CRITICAL_K = 0.971635406

    def __init__(self, perturbation_k: float):
        self.k = perturbation_k

    def step(self, theta: float, p: float) -> Tuple[float, float]:
        """Iterate mapping one discrete time step."""
        p_next = (p + self.k * np.sin(theta)) % (2.0 * np.pi)
        theta_next = (theta + p_next) % (2.0 * np.pi)
        return theta_next, p_next

    def jacobian_determinant(self, theta: float) -> float:
        """Det(d(theta_{n+1}, p_{n+1}) / d(theta_n, p_n)) == 1 (exact symplectic area preservation)."""
        # M = [[1 + K cos(theta), 1], [K cos(theta), 1]] => det = (1 + K cos)(1) - (1)(K cos) = 1
        return 1.0

    def iterate_trajectory(self, theta0: float, p0: float, steps: int = 1000) -> Tuple[np.ndarray, np.ndarray]:
        """Generate orbit points (theta_k, p_k)."""
        thetas = np.zeros(steps, dtype=np.float64)
        ps = np.zeros(steps, dtype=np.float64)
        th, p = theta0, p0
        for i in range(steps):
            th, p = self.step(th, p)
            thetas[i] = th
            ps[i] = p
        return thetas, ps
