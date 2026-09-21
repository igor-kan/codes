"""
Dynamic Hedge Ratio Estimation for Pairs Trading via 1D Kalman Filter.
Reference: Pal, Practical Time Series Analysis; Prado.
"""
import numpy as np

def kalman_hedge_ratio(y: np.ndarray, x: np.ndarray, delta: float = 1e-4) -> np.ndarray:
    """
    State: beta_t. Observation: y_t = beta_t x_t + eps_t.
    """
    n = len(y)
    beta = np.zeros(n)
    P = 1.0
    R = 0.01  # Measurement noise
    
    current_beta = 1.0
    for t in range(n):
        # Predict
        P += delta
        # Update
        F = x[t] * P * x[t] + R
        K = P * x[t] / F
        v = y[t] - x[t] * current_beta
        current_beta += K * v
        P -= K * x[t] * P
        beta[t] = current_beta
        
    return beta
