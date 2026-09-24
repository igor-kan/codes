"""Ornstein-Uhlenbeck Mean-Reverting Spread Estimation for Statistical Arbitrage.

dX_t = theta * (mu - X_t) * dt + sigma * dW_t.
Exact discrete regression: X_{t+1} = a + b * X_t + eps.
"""
import numpy as np


def fit_ornstein_uhlenbeck(spread: np.ndarray, dt: float) -> dict:
    """Estimate OU mean reversion speed theta, long-term mean mu, and volatility sigma."""
    x = spread[:-1]
    y = spread[1:]
    n = len(x)
    
    sx = np.sum(x)
    sy = np.sum(y)
    sxx = np.sum(x * x)
    sxy = np.sum(x * y)
    syy = np.sum(y * y)
    
    b = (n * sxy - sx * sy) / (n * sxx - sx * sx)
    a = (sy - b * sx) / n
    
    residuals = y - (a + b * x)
    var_eps = np.sum(residuals**2) / (n - 2)
    
    theta = -np.log(b) / dt if b > 0 else float("nan")
    mu = a / (1.0 - b) if b != 1.0 else float("nan")
    sigma = np.sqrt(var_eps * 2.0 * theta / (1.0 - b**2)) if (b > 0 and b < 1.0) else float("nan")
    half_life = np.log(2.0) / theta if theta > 0 else float("nan")
    
    return {"theta": theta, "mu": mu, "sigma": sigma, "half_life": half_life}
