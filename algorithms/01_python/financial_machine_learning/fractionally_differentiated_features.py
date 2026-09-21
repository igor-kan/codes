"""
Fractional Differentiation of Time Series to Preserve Memory and Achieve Stationarity.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 5.
"""
import numpy as np

def get_fractional_weights(d: float, size: int) -> np.ndarray:
    """
    Computes weights w_k = - w_{k-1} * (d - k + 1) / k with w_0 = 1.
    """
    w = [1.0]
    for k in range(1, size):
        w.append(-w[-1] / k * (d - k + 1))
    return np.array(w)

def fractional_diff(series: np.ndarray, d: float, threshold: float = 1e-4) -> np.ndarray:
    w = get_fractional_weights(d, len(series))
    w = w[np.abs(w) > threshold]
    k = len(w)
    out = np.zeros(len(series) - k + 1)
    for i in range(len(out)):
        out[i] = np.dot(w, series[i:i+k][::-1])
    return out
