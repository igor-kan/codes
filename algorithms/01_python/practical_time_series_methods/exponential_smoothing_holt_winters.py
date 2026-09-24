"""Holt's Double Linear Exponential Smoothing for Trended Series."""
import numpy as np


def holt_linear_smoothing(series: np.ndarray, alpha: float, beta: float) -> tuple:
    """Compute level l_t and trend b_t components."""
    n = len(series)
    l = np.zeros(n)
    b = np.zeros(n)
    l[0] = series[0]
    b[0] = series[1] - series[0]
    
    for t in range(1, n):
        l[t] = alpha * series[t] + (1.0 - alpha) * (l[t - 1] + b[t - 1])
        b[t] = beta * (l[t] - l[t - 1]) + (1.0 - beta) * b[t - 1]
        
    return l, b
