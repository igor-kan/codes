"""Online Dynamic Hedge Ratio Estimation via 1D State Space Kalman Filter.

y_t = beta_t * x_t + eps_t
beta_{t+1} = beta_t + eta_t.
"""
import numpy as np


def kalman_hedge_ratio(x: np.ndarray, y: np.ndarray, delta: float = 1e-4, R: float = 1e-3) -> np.ndarray:
    """Estimate dynamic regression hedge ratio beta_t online."""
    n = len(x)
    beta = np.zeros(n)
    P = 1.0
    beta_hat = 0.0
    
    for t in range(n):
        # Predict
        P_prior = P + delta
        # Update
        F = x[t]**2 * P_prior + R
        K = (P_prior * x[t]) / F
        e = y[t] - x[t] * beta_hat
        beta_hat = beta_hat + K * e
        P = (1.0 - K * x[t]) * P_prior
        beta[t] = beta_hat
        
    return beta
