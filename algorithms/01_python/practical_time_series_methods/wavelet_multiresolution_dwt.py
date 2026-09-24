"""Discrete Haar Wavelet Transform (DWT) Decomposition."""
import numpy as np


def haar_dwt(signal: np.ndarray) -> tuple:
    """Single-level discrete Haar transform."""
    n = len(signal)
    if n % 2 != 0:
        signal = signal[:-1]
        n -= 1
    approx = (signal[0::2] + signal[1::2]) / np.sqrt(2.0)
    detail = (signal[0::2] - signal[1::2]) / np.sqrt(2.0)
    return approx, detail
