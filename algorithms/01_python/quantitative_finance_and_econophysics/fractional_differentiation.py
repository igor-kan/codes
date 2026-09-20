"""
Fractionally Differentiated Time Series (Fixed-Width Window).
References: Marcos Lopez de Prado - Advances in Financial Machine Learning (Ch. 5).
"""
import numpy as np

def get_fractional_weights(d: float, size: int, threshold: float = 1e-4) -> np.ndarray:
    """Compute binomial weights w_k = -w_{k-1} / k * (d - k + 1)."""
    w = [1.0]
    for k in range(1, size):
        w_k = -w[-1] / k * (d - k + 1)
        if abs(w_k) < threshold:
            break
        w.append(w_k)
    return np.array(w[::-1])  # Reverse for dot product convolution

def fractional_differentiation_ffd(series: np.ndarray, d: float, threshold: float = 1e-4) -> np.ndarray:
    """Fractional differentiation with Fixed-Width Window (FFD)."""
    series = np.asarray(series, dtype=float)
    w = get_fractional_weights(d, len(series), threshold)
    width = len(w)
    res = np.zeros(len(series) - width + 1)
    for i in range(len(res)):
        res[i] = np.dot(w, series[i:i + width])
    return res
