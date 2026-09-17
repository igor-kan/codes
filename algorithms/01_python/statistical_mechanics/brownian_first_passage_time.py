"""First-Passage Time Distribution for 1D Brownian Motion with Absorbing Barrier.

Calculates f(t) = a / sqrt(4 pi D t^3) exp(- a^2 / (4 D t)).
"""

import numpy as np


class BrownianFirstPassage:
    """First-passage time statistics."""

    @staticmethod
    def density(t: float, barrier_distance: float, diffusion_coeff: float) -> float:
        """First passage probability density."""
        if t <= 0.0:
            return 0.0
        a = barrier_distance
        d = diffusion_coeff
        return float((a / np.sqrt(4.0 * np.pi * d * (t**3))) * np.exp(- (a**2) / (4.0 * d * t)))
