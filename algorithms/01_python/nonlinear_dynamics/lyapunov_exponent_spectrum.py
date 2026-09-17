"""Maximal Lyapunov Exponent estimation via trajectory perturbation."""

from typing import Callable
import numpy as np


class LyapunovExponent:
    """Estimates maximal Lyapunov exponent lambda_max using continuous trajectory renormalization."""

    @classmethod
    def estimate_max_exponent(
        cls,
        deriv_fn: Callable[[np.ndarray], np.ndarray],
        state0: np.ndarray,
        dt: float = 0.01,
        steps: int = 1000,
        d0: float = 1e-7,
    ) -> float:
        """Computes lambda_max = (1 / (N * dt)) * sum(ln(d_k / d0))."""
        x1 = state0.copy()
        # Initial displaced point
        pert = np.random.randn(len(state0))
        pert = d0 * pert / np.linalg.norm(pert)
        x2 = x1 + pert

        lyap_sum = 0.0

        for _ in range(steps):
            # RK4 step for x1
            k1 = deriv_fn(x1)
            k2 = deriv_fn(x1 + 0.5 * dt * k1)
            k3 = deriv_fn(x1 + 0.5 * dt * k2)
            k4 = deriv_fn(x1 + dt * k3)
            x1 += (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

            # RK4 step for x2
            k1 = deriv_fn(x2)
            k2 = deriv_fn(x2 + 0.5 * dt * k1)
            k3 = deriv_fn(x2 + 0.5 * dt * k2)
            k4 = deriv_fn(x2 + dt * k3)
            x2 += (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

            # Measure distance
            diff = x2 - x1
            d_curr = np.linalg.norm(diff)
            if d_curr > 0:
                lyap_sum += np.log(d_curr / d0)
                # Renormalize x2 back to d0
                x2 = x1 + (d0 / d_curr) * diff

        total_time = steps * dt
        return float(lyap_sum / total_time)
