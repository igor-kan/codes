"""Empirical Mode Decomposition (EMD) Sifting for Intrinsic Mode Functions (IMF)."""
import numpy as np
from scipy.interpolate import CubicSpline


def sifting_step(signal: np.ndarray) -> np.ndarray:
    """Extract first candidate mode through upper/lower envelope averaging."""
    n = len(signal)
    x = np.arange(n)
    
    # Extrema
    max_idx = np.where((signal[1:-1] > signal[:-2]) & (signal[1:-1] > signal[2:]))[0] + 1
    min_idx = np.where((signal[1:-1] < signal[:-2]) & (signal[1:-1] < signal[2:]))[0] + 1
    
    if len(max_idx) < 2 or len(min_idx) < 2:
        return signal
        
    cs_max = CubicSpline(max_idx, signal[max_idx], bc_type="natural")
    cs_min = CubicSpline(min_idx, signal[min_idx], bc_type="natural")
    
    x_valid = np.arange(max(max_idx[0], min_idx[0]), min(max_idx[-1], min_idx[-1]) + 1)
    mean_env = 0.5 * (cs_max(x_valid) + cs_min(x_valid))
    return signal[x_valid] - mean_env
