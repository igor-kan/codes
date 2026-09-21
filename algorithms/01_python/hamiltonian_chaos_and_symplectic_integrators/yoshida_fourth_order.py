"""Yoshida 4th-Order Symplectic Integrator.

Composition of 2nd-order symmetric Verlet steps with sub-steps:
w1 = w3 = 1 / (2 - 2^(1/3))
w0 = -2^(1/3) / (2 - 2^(1/3))
yielding an explicit symplectic method of order 4.
"""
import numpy as np
from typing import Callable, Tuple
from symplectic_verlet import velocity_verlet_step

_CBRT_2 = 2.0**(1.0 / 3.0)
W1 = 1.0 / (2.0 - _CBRT_2)
W0 = -_CBRT_2 / (2.0 - _CBRT_2)


def yoshida4_step(q: np.ndarray, p: np.ndarray, dt: float,
                  force_fn: Callable[[np.ndarray], np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
    """Single Yoshida 4th-order symplectic integration step."""
    q1, p1 = velocity_verlet_step(q, p, W1 * dt, force_fn)
    q2, p2 = velocity_verlet_step(q1, p1, W0 * dt, force_fn)
    q3, p3 = velocity_verlet_step(q2, p2, W1 * dt, force_fn)
    return q3, p3


def yoshida4_integrate(q0: np.ndarray, p0: np.ndarray, t_span: Tuple[float, float],
                       n_steps: int, force_fn: Callable[[np.ndarray], np.ndarray]) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Integrate trajectory using Yoshida 4th-order method."""
    dt = (t_span[1] - t_span[0]) / n_steps
    times = np.linspace(t_span[0], t_span[1], n_steps + 1)
    
    q_traj = [q0.copy()]
    p_traj = [p0.copy()]
    q, p = q0.copy(), p0.copy()
    
    for _ in range(n_steps):
        q, p = yoshida4_step(q, p, dt, force_fn)
        q_traj.append(q.copy())
        p_traj.append(p.copy())
        
    return times, np.array(q_traj), np.array(p_traj)
