"""Householder Reflection QR Matrix Decomposition (Kincaid & Cheney).

A = Q * R, where Q is orthogonal and R is upper triangular.
"""
import numpy as np


def qr_householder(A: np.ndarray) -> tuple:
    """Compute QR decomposition using Householder reflectors."""
    m, n = A.shape
    R = A.copy().astype(float)
    Q = np.eye(m)
    
    for k in range(min(m - 1, n)):
        x = R[k:, k]
        norm_x = np.linalg.norm(x)
        if norm_x < 1e-14:
            continue
        v = x.copy()
        sign = 1.0 if x[0] >= 0 else -1.0
        v[0] += sign * norm_x
        v /= np.linalg.norm(v)
        
        H = np.eye(m - k) - 2.0 * np.outer(v, v)
        R[k:, k:] = H @ R[k:, k:]
        
        H_full = np.eye(m)
        H_full[k:, k:] = H
        Q = Q @ H_full
        
    return Q, R
