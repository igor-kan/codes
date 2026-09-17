"""Korteweg-de Vries (KdV) exact soliton solutions.

Equation: u_t + 6 * u * u_x + u_xxx = 0
"""

import numpy as np


class KdVSoliton:
    """Exact analytical single and multi-soliton solutions to the KdV equation."""

    @classmethod
    def single_soliton(cls, x: np.ndarray, t: float, c: float, x0: float = 0.0) -> np.ndarray:
        """Single soliton wave:
        u(x, t) = (c / 2) * sech^2( (sqrt(c) / 2) * (x - c * t - x0) )
        """
        xi = 0.5 * np.sqrt(c) * (x - c * t - x0)
        # Avoid overflow in cosh
        clipped_xi = np.clip(xi, -50.0, 50.0)
        sech_val = 1.0 / np.cosh(clipped_xi)
        return (c / 2.0) * (sech_val ** 2)

    @classmethod
    def energy_invariant(cls, u: np.ndarray, dx: float) -> float:
        """First conserved integral: I1 = int u(x) dx."""
        return float(np.sum(u) * dx)
