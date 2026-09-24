"""Fractional Differentiation for Financial Time Series Stationarity (Lopez de Prado).

Preserves memory while achieving stationarity via expanding binomial weights:
(1 - B)^d = sum_{k=0}^infty (-1)^k * (d choose k) * B^k.
"""
import numpy as np


def get_fractional_weights(d: float, size: int) -> np.ndarray:
    """Compute binomial expansion weights for fractional differencing."""
    w = [1.0]
    for k in range(1, size):
        w.append(-w[-1] / k * (d - k + 1))
    return np.array(w[::-1])


def fractional_diff(series: np.ndarray, d: float, threshold: float = 1e-4) -> np.ndarray:
    """Apply fractional differencing with weight cutoff threshold."""
    weights = get_fractional_weights(d, len(series))
    weights = weights[np.abs(weights) > threshold]
    res = np.convolve(series, weights, mode="valid")
    return res
