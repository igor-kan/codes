"""Unscented Kalman Filter (UKF) Merwe Scaled Sigma Points Generator."""
import numpy as np


def generate_sigma_points(x: np.ndarray, P: np.ndarray, alpha: float = 1e-3, beta: float = 2.0, kappa: float = 0.0) -> tuple:
    """Compute 2n+1 Merwe scaled sigma points and weights."""
    n = len(x)
    lam = alpha**2 * (n + kappa) - n
    c = n + lam
    
    A = np.linalg.cholesky(c * P)
    sigma_pts = np.zeros((2 * n + 1, n))
    sigma_pts[0] = x
    for i in range(n):
        sigma_pts[i + 1] = x + A[:, i]
        sigma_pts[n + i + 1] = x - A[:, i]
        
    Wm = np.full(2 * n + 1, 0.5 / c)
    Wc = np.full(2 * n + 1, 0.5 / c)
    Wm[0] = lam / c
    Wc[0] = lam / c + (1.0 - alpha**2 + beta)
    return sigma_pts, Wm, Wc
