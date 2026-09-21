"""Maximal Lyapunov Exponent via Tangent Space Benettin Renormalization.

Computes lambda_max = lim_(t -> inf) (1/t) * sum_k ln(||delta_q(t_k)|| / d0)
using linearized tangent flow.
"""
import numpy as np
from typing import Callable


def benettin_lyapunov_exponent(q0: np.ndarray, p0: np.ndarray,
                               force_fn: Callable[[np.ndarray], np.ndarray],
                               force_jacobian: Callable[[np.ndarray], np.ndarray],
                               dt: float, n_steps: int, renorm_steps: int = 10,
                               d0: float = 1e-8) -> float:
    """Estimate maximal Lyapunov exponent for Hamiltonian flow."""
    q = q0.copy()
    p = p0.copy()
    # Tangent vector in phase space (dq, dp)
    w = np.zeros(2 * len(q0))
    w[0] = d0

    lyap_sum = 0.0
    total_time = n_steps * dt

    for step in range(1, n_steps + 1):
        # Symplectic leapfrog on base trajectory
        F = force_fn(q)
        p += 0.5 * dt * F
        q += dt * p
        F_next = force_fn(q)
        p += 0.5 * dt * F_next

        # Tangent map evolution
        J = force_jacobian(q)
        # dw_p/dt = J @ dq, dw_q/dt = dp
        w[:len(q)] += dt * w[len(q):]
        w[len(q):] += dt * (J @ w[:len(q)])

        if step % renorm_steps == 0:
            dist = np.linalg.norm(w)
            lyap_sum += np.log(dist / d0)
            w = (w / dist) * d0

    return float(lyap_sum / total_time)
