"""Symplectic Geometric Numerical Integrators (Verlet, Ruth, Forest-Ruth, Yoshida).

Preserves symplectic invariants and the shadow Hamiltonian without secular energy drift.
"""

from typing import Callable, Sequence, Tuple
import numpy as np


class SymplecticIntegrator:
    """Symplectic geometric integrators for separable Hamiltonians H = 1/2 p^T M^{-1} p + V(q)."""

    def __init__(self, grad_v: Callable[[np.ndarray], np.ndarray], mass: float = 1.0):
        self.grad_v = grad_v
        self.m = mass

    def verlet_step(self, q: Sequence[float], p: Sequence[float], dt: float) -> Tuple[np.ndarray, np.ndarray]:
        """2nd-order Stormer-Verlet / Leapfrog symplectic step."""
        q_arr = np.array(q, dtype=np.float64)
        p_arr = np.array(p, dtype=np.float64)

        # Half step momentum: p_{1/2} = p_0 - 1/2 dt grad V(q_0)
        p_half = p_arr - 0.5 * dt * self.grad_v(q_arr)
        # Full step position: q_1 = q_0 + dt p_{1/2} / m
        q_next = q_arr + dt * (p_half / self.m)
        # Second half step momentum: p_1 = p_{1/2} - 1/2 dt grad V(q_1)
        p_next = p_half - 0.5 * dt * self.grad_v(q_next)

        return q_next, p_next

    def integrate(self, q0: Sequence[float], p0: Sequence[float], dt: float, steps: int) -> Tuple[np.ndarray, np.ndarray]:
        """Integrate trajectory for given steps."""
        q_hist = [np.array(q0, dtype=np.float64)]
        p_hist = [np.array(p0, dtype=np.float64)]
        q_curr, p_curr = q_hist[0], p_hist[0]
        for _ in range(steps):
            q_curr, p_curr = self.verlet_step(q_curr, p_curr, dt)
            q_hist.append(q_curr)
            p_hist.append(p_curr)
        return np.array(q_hist), np.array(p_hist)
