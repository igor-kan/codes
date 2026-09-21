"""
Brownian Motion Simulation and Quadratic Variation Convergence.
Reference: Evans & Rosenthal; Karatzas & Shreve, Brownian Motion.
"""
import numpy as np

def simulate_brownian_path(t_end: float, n_steps: int, seed: int = 42) -> np.ndarray:
    rng = np.random.default_rng(seed)
    dt = t_end / n_steps
    dW = rng.normal(0.0, np.sqrt(dt), size=n_steps)
    W = np.concatenate([[0.0], np.cumsum(dW)])
    return W

def quadratic_variation(path: np.ndarray) -> float:
    """sum (W_{k+1} - W_k)^2 -> T almost surely as dt -> 0."""
    diffs = np.diff(path)
    return float(np.sum(diffs**2))
