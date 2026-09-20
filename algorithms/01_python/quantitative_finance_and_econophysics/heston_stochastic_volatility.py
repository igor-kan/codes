"""
Heston Stochastic Volatility Simulation with Full Truncation Euler Scheme.
References: Jovanovic - Econophysics and Financial Economics.
"""
import numpy as np

def simulate_heston_path(S0, v0, kappa, theta, xi, rho, r, dt, n_steps):
    """Simulate single asset price S and variance v path under Heston model."""
    S = np.zeros(n_steps)
    v = np.zeros(n_steps)
    S[0] = S0
    v[0] = v0

    cov_matrix = np.array([[1.0, rho], [rho, 1.0]])
    L = np.linalg.cholesky(cov_matrix)

    for i in range(1, n_steps):
        z = L @ np.random.normal(size=2)
        v_pos = max(v[i - 1], 0.0)
        sqrt_v = np.sqrt(v_pos)

        # Full truncation update for variance
        v[i] = v[i - 1] + kappa * (theta - v_pos) * dt + xi * sqrt_v * np.sqrt(dt) * z[1]
        # Asset price update
        S[i] = S[i - 1] * np.exp((r - 0.5 * v_pos) * dt + sqrt_v * np.sqrt(dt) * z[0])

    return S, v
