"""Velocity Verlet and Störmer-Verlet Symplectic Integrators.

Preserves symplectic 2-form dq ^ dp and phase space volume (Liouville's theorem)
for separable Hamiltonians H(q, p) = 0.5 * p^2 + V(q).
"""
import numpy as np
from typing import Callable, Tuple


def velocity_verlet_step(q: np.ndarray, p: np.ndarray, dt: float,
                         force_fn: Callable[[np.ndarray], np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    """Single Velocity Verlet symplectic integration step."""
    F_curr = force_fn(q)
    # Half kick
    p_half = p + 0.5 * dt * F_curr
    # Full drift
    q_next = q + dt * p_half
    # Half kick
    F_next = force_fn(q_next)
    p_next = p_half + 0.5 * dt * F_next
    return q_next, p_next


def velocity_verlet_integrate(q0: np.ndarray, p0: np.ndarray, t_span: Tuple[float, float],
                              n_steps: int, force_fn: Callable[[np.ndarray], np.ndarray]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Integrate trajectory using Velocity Verlet."""
    dt = (t_span[1] - t_span[0]) / n_steps
    times = np.linspace(t_span[0], t_span[1], n_steps + 1)
    
    q_traj = [q0.copy()]
    p_traj = [p0.copy()]
    q, p = q0.copy(), p0.copy()
    
    for _ in range(n_steps):
        q, p = velocity_verlet_step(q, p, dt, force_fn)
        q_traj.append(q.copy())
        p_traj.append(p.copy())
        
    return times, np.array(q_traj), np.array(p_traj)
