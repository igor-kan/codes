"""
Linear and Nonlinear Conjugate Gradient Solvers.
References: Press et al. - Numerical Recipes (Ch. 10).
"""
import numpy as np

def linear_conjugate_gradient(A: np.ndarray, b: np.ndarray, x0=None, tol=1e-8, max_iter=None):
    """Solve symmetric positive-definite system Ax = b."""
    n = len(b)
    x = np.zeros(n) if x0 is None else np.array(x0, dtype=float)
    if max_iter is None:
        max_iter = 2 * n

    r = b - A @ x
    p = r.copy()
    r_dot = np.dot(r, r)

    for _ in range(max_iter):
        if np.sqrt(r_dot) < tol:
            break
        Ap = A @ p
        alpha = r_dot / np.dot(p, Ap)
        x += alpha * p
        r -= alpha * Ap
        r_dot_new = np.dot(r, r)
        beta = r_dot_new / r_dot
        p = r + beta * p
        r_dot = r_dot_new

    return x
