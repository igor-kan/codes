"""Almgren-Chriss Optimal Order Execution with Market Impact and Risk Aversion.

Minimizes E[x_t] + lambda * Var[x_t] under permanent and temporary impact.
"""
import numpy as np


def optimal_execution_trajectory(X_total: float, T: float, N: int,
                                 gamma_perm: float, eta_temp: float,
                                 sigma: float, lam_risk: float) -> np.ndarray:
    """Calculate optimal inventory trajectory x_j across N execution intervals."""
    tau = T / N
    kappa_sq = (lam_risk * sigma**2) / eta_temp
    kappa = np.sqrt(kappa_sq)
    
    j_steps = np.arange(N + 1)
    sinh_total = np.sinh(kappa * T)
    if np.isclose(sinh_total, 0.0):
        # Linear execution if no risk aversion
        return X_total * (1.0 - j_steps / N)
    
    trajectory = X_total * np.sinh(kappa * (T - j_steps * tau)) / sinh_total
    return trajectory
