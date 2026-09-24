"""Hodrick-Prescott (HP) Filter for Trend-Cycle Macroeconomic Decomposition."""
import numpy as np


def hp_filter(y: np.ndarray, lamb: float = 1600.0) -> tuple:
    """Decompose time series y into smooth trend and cyclical components."""
    n = len(y)
    # Second-order difference matrix D2
    D2 = np.zeros((n - 2, n))
    for i in range(n - 2):
        D2[i, i] = 1.0
        D2[i, i + 1] = -2.0
        D2[i, i + 2] = 1.0
        
    I = np.eye(n)
    trend = np.linalg.solve(I + lamb * (D2.T @ D2), y)
    cycle = y - trend
    return trend, cycle
