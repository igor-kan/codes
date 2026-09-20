"""
QR Decomposition via Householder Reflections.
References: Press et al. - Numerical Recipes (Ch. 2); Kincaid & Cheney (Ch. 4).
"""
import numpy as np

def householder_qr(A: np.ndarray):
    """Compute QR decomposition of matrix A using Householder reflectors."""
    m, n = A.shape
    Q = np.eye(m)
    R = A.astype(float).copy()

    for k in range(min(m - 1, n)):
        x = R[k:, k]
        norm_x = np.linalg.norm(x)
        if norm_x == 0:
            continue
        sign = 1.0 if x[0] >= 0 else -1.0
        u1 = x[0] + sign * norm_x
        w = x / u1
        w[0] = 1.0
        beta = 2.0 / np.dot(w, w)

        # Apply Householder to R[k:, k:]
        R[k:, k:] -= beta * np.outer(w, np.dot(w, R[k:, k:]))
        # Accumulate Q
        Q[:, k:] -= beta * np.outer(np.dot(Q[:, k:], w), w)

    return Q, R
