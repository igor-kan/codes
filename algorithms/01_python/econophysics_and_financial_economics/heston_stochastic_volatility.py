"""Heston Stochastic Volatility Simulation via Euler-Maruyama with Full Truncation.

dS_t = mu * S_t * dt + sqrt(V_t) * S_t * dW_1
dV_t = kappa * (theta - V_t) * dt + xi * sqrt(V_t) * dW_2
corr(dW_1, dW_2) = rho.
"""
import numpy as np


def simulate_heston_paths(S0: float, V0: float, mu: float, kappa: float, theta: float,
                          xi: float, rho: float, T: float, n_steps: int, n_paths: int,
                          seed: int = 42) -> tuple:
    """Simulate asset price and variance paths."""
    np.random.seed(seed)
    dt = T / n_steps
    S = np.zeros((n_paths, n_steps + 1))
    V = np.zeros((n_paths, n_steps + 1))
    S[:, 0] = S0
    V[:, 0] = V0
    
    for t in range(n_steps):
        z1 = np.random.standard_normal(n_paths)
        z2 = rho * z1 + np.sqrt(1.0 - rho**2) * np.random.standard_normal(n_paths)
        
        v_curr = np.maximum(V[:, t], 0.0)
        V[:, t + 1] = v_curr + kappa * (theta - v_curr) * dt + xi * np.sqrt(v_curr * dt) * z2
        V[:, t + 1] = np.maximum(V[:, t + 1], 0.0)
        
        S[:, t + 1] = S[:, t] * np.exp((mu - 0.5 * v_curr) * dt + np.sqrt(v_curr * dt) * z1)
        
    return S, V
