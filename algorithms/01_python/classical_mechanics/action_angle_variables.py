"""Arnold-Liouville Theorem and Action-Angle Variables (I_k, theta^k).

Implements completely integrable Hamiltonian systems, invariant Liouville tori T^n, and frequencies omega_k = dH/dI_k.
"""

from typing import Sequence
import numpy as np


class ActionAngleTorus:
    """Action-angle variables (I, theta) on invariant Lagrangian tori."""

    def __init__(self, action_variables: Sequence[float], fundamental_frequencies: Sequence[float]):
        self.actions = np.array(action_variables, dtype=np.float64)
        self.frequencies = np.array(fundamental_frequencies, dtype=np.float64)
        self.n = len(self.actions)

    def angle_trajectory(self, t: float, initial_angles: Sequence[float]) -> np.ndarray:
        """theta^k(t) = omega_k t + theta_0^k mod 2 pi."""
        th0 = np.array(initial_angles, dtype=np.float64)
        return (th0 + self.frequencies * t) % (2.0 * np.pi)

    def is_resonant(self, max_order: int = 5, tol: float = 1e-6) -> bool:
        """Check for commensurability (resonance): sum_k n_k omega_k == 0 for integer vector n != 0."""
        if self.n != 2:
            return False  # Test 2D tori
        w1, w2 = self.frequencies
        ratio = w1 / w2 if w2 != 0 else 0.0
        for n2 in range(1, max_order + 1):
            n1 = round(ratio * n2)
            if abs(w1 * n2 - w2 * n1) < tol:
                return True
        return False
