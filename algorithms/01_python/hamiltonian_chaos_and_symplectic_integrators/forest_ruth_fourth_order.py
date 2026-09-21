"""Forest-Ruth 4th-Order Explicit Symplectic Integrator.

Coefficients for separable Hamiltonian H = T(p) + V(q):
theta = 1 / (2 - 2^(1/3)).
"""
import numpy as np
from typing import Callable, Tuple

_THETA = 1.0 / (2.0 - 2.0**(1.0 / 3.0))


def forest_ruth_step(q: np.ndarray, p: np.ndarray, dt: float,
                     force_fn: Callable[[np.ndarray], np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    """Single Forest-Ruth 4th order symplectic integration step."""
    # Step 1
    q1 = q + _THETA * 0.5 * dt * p
    p1 = p + _THETA * dt * force_fn(q1)
    # Step 2
    q2 = q1 + (1.0 - _THETA) * 0.5 * dt * p1
    p2 = p1 + (1.0 - 2.0 * _THETA) * dt * force_fn(q2)
    # Step 3
    q3 = q2 + (1.0 - _THETA) * 0.5 * dt * p2
    p3 = p2 + _THETA * dt * force_fn(q3)
    # Step 4
    q4 = q3 + _THETA * 0.5 * dt * p3
    return q4, p3
