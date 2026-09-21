"""
Girsanov Theorem Exponential Martingale Density Process.
Reference: Evans & Rosenthal; Shreve, Stochastic Calculus for Finance II.
"""
import numpy as np

def girsanov_radon_nikodym_density(theta: float, W_path: np.ndarray, time_grid: np.ndarray) -> np.ndarray:
    """
    Z_t = exp( - theta W_t - 1/2 theta^2 t ).
    Under measure tilde{P}, tilde{W}_t = W_t + theta t is a Brownian motion.
    """
    return np.exp(-theta * W_path - 0.5 * (theta**2) * time_grid)
