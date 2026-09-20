"""
Cointegration and Mean-Reverting Spread Estimator.
References: Jovanovic; Pal - Practical Time Series Analysis.
"""
import numpy as np

def estimate_ou_parameters(spread: np.ndarray, dt: float):
    """Calibrate OU parameters theta, mu, sigma from discrete time series via AR(1) regression."""
    x = spread[:-1]
    y = spread[1:]
    n = len(x)
    # Regression y = a x + b + eps
    a = (n * np.sum(x * y) - np.sum(x) * np.sum(y)) / (n * np.sum(x**2) - (np.sum(x))**2)
    b = (np.sum(y) - a * np.sum(x)) / n
    residuals = y - (a * x + b)
    sigma_eps = np.std(residuals)

    theta = -np.log(max(1e-6, a)) / dt
    mu = b / (1.0 - a) if abs(1.0 - a) > 1e-6 else 0.0
    sigma = sigma_eps * np.sqrt(2.0 * theta / (1.0 - a**2)) if abs(1.0 - a**2) > 1e-6 else sigma_eps
    return theta, mu, sigma
