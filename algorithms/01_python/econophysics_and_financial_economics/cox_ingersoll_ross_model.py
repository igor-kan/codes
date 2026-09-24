"""Cox-Ingersoll-Ross (CIR) Square-Root Short-Rate Model.

dr_t = k * (theta - r_t) * dt + sigma * sqrt(r_t) * dW_t.
Feller condition for strict positivity: 2 * k * theta >= sigma^2.
"""
import numpy as np


def cir_feller_satisfied(k: float, theta: float, sigma: float) -> bool:
    """Verify Feller condition."""
    return bool(2.0 * k * theta >= sigma**2)


def cir_simulate(r0: float, k: float, theta: float, sigma: float, T: float, n_steps: int, seed: int = 42) -> np.ndarray:
    """Simulate non-negative short rates with full truncation."""
    np.random.seed(seed)
    dt = T / n_steps
    r = np.zeros(n_steps + 1)
    r[0] = r0
    for t in range(n_steps):
        r_pos = max(r[t], 0.0)
        dr = k * (theta - r_pos) * dt + sigma * np.sqrt(r_pos * dt) * np.random.standard_normal()
        r[t + 1] = max(r[t] + dr, 0.0)
    return r
