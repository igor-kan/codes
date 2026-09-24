"""Singular Spectrum Analysis (SSA) for Time Series Trajectory Matrix."""
import numpy as np


def ssa_decompose(series: np.ndarray, L: int) -> tuple:
    """Construct Hankel trajectory matrix and compute singular spectrum."""
    N = len(series)
    K = N - L + 1
    X = np.zeros((L, K))
    for i in range(K):
        X[:, i] = series[i:i + L]
    U, s, Vt = np.linalg.svd(X, full_matrices=False)
    return U, s, Vt
