"""Engle-Granger Two-Step Co-Integration Residual Stationarity."""
import numpy as np


def engle_granger_spread(y: np.ndarray, x: np.ndarray) -> np.ndarray:
    """Compute OLS residual spread e_t = y_t - (alpha + beta * x_t)."""
    X = np.column_stack([np.ones_like(x), x])
    coeffs = np.linalg.lstsq(X, y, rcond=None)[0]
    return y - X @ coeffs
