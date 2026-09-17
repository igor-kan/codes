"""Noether's Theorem and Continuous Symmetry Generators in Classical Mechanics.

Associates continuous symmetry transformations of the Lagrangian to conserved Noether charges (Arnold §20, Landau §6-§9).
"""

from typing import Callable, Sequence
import numpy as np


class NoetherTheorem:
    """Noether charge evaluation from infinitesimal symmetry generators."""

    @staticmethod
    def conserved_charge(generalized_momentum: Sequence[float],
                         symmetry_generator: Sequence[float],
                         gauge_term: float = 0.0) -> float:
        """Q = sum_i p_i xi^i(q, t) - F(q, t)."""
        p = np.array(generalized_momentum, dtype=np.float64)
        xi = np.array(symmetry_generator, dtype=np.float64)
        return float(np.dot(p, xi) - gauge_term)

    @staticmethod
    def angular_momentum_3d(position: Sequence[float], linear_momentum: Sequence[float]) -> np.ndarray:
        """Conserved charge under SO(3) rotational symmetry: L = r x p."""
        r = np.array(position, dtype=np.float64)
        p = np.array(linear_momentum, dtype=np.float64)
        return np.cross(r, p)

    @staticmethod
    def runge_lenz_vector(position: Sequence[float], velocity: Sequence[float],
                          mass: float, k_potential: float) -> np.ndarray:
        """Laplace-Runge-Lenz conserved vector for Kepler 1/r potential: A = p x L - m k r_hat."""
        r = np.array(position, dtype=np.float64)
        v = np.array(velocity, dtype=np.float64)
        p = mass * v
        l = np.cross(r, p)
        r_norm = np.linalg.norm(r)
        r_hat = r / r_norm
        return np.cross(p, l) - mass * k_potential * r_hat
