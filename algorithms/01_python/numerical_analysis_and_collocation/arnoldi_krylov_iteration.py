"""Arnoldi Iteration for Krylov Subspace Projection and Hessenberg Reduction."""
import numpy as np


def arnoldi_iteration(A: np.ndarray, b: np.ndarray, m: int) -> tuple:
    """Construct orthonormal basis V_m and upper Hessenberg matrix H_m."""
    n = A.shape[0]
    V = np.zeros((n, m + 1))
    H = np.zeros((m + 1, m))
    
    V[:, 0] = b / np.linalg.norm(b)
    for j in range(m):
        w = A @ V[:, j]
        for i in range(j + 1):
            H[i, j] = np.dot(V[:, i], w)
            w -= H[i, j] * V[:, i]
        H[j + 1, j] = np.linalg.norm(w)
        if H[j + 1, j] > 1e-12 and j + 1 < m + 1:
            V[:, j + 1] = w / H[j + 1, j]
        else:
            break
    return V[:, :m], H[:m, :m]
