"""GARCH(1,1) Volatility Modeling and Variance Targeting.

sigma_t^2 = omega + alpha * eps_{t-1}^2 + beta * sigma_{t-1}^2.
Unconditional variance: sigma_inf^2 = omega / (1 - alpha - beta).
"""
import numpy as np


def garch11_filter(returns: np.ndarray, omega: float, alpha: float, beta: float) -> np.ndarray:
    """Filter conditional variance series given GARCH parameters."""
    if alpha + beta >= 1.0:
        raise ValueError("GARCH process must be covariance stationary (alpha + beta < 1)")
    n = len(returns)
    sigma2 = np.zeros(n)
    sigma2[0] = omega / (1.0 - alpha - beta)
    
    for t in range(1, n):
        sigma2[t] = omega + alpha * (returns[t - 1]**2) + beta * sigma2[t - 1]
    return sigma2
