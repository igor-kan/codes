"""Bi-CGSTAB: Biconjugate Gradient Stabilized Solver for Non-Symmetric Linear Systems."""
import numpy as np


def bicgstab(A: np.ndarray, b: np.ndarray, tol: float = 1e-9, max_iter: int = 1000) -> np.ndarray:
    """Solve A x = b using Bi-CGSTAB without transpose."""
    n = len(b)
    x = np.zeros(n)
    r = b - A @ x
    r_hat = r.copy()
    rho_prev = alpha = omega = 1.0
    v = p = np.zeros(n)
    
    for _ in range(max_iter):
        rho = np.dot(r_hat, r)
        if abs(rho) < 1e-16:
            break
        beta = (rho / rho_prev) * (alpha / omega)
        p = r + beta * (p - omega * v)
        v = A @ p
        alpha = rho / np.dot(r_hat, v)
        s = r - alpha * v
        if np.linalg.norm(s) < tol:
            x += alpha * p
            break
        t = A @ s
        omega = np.dot(t, s) / np.dot(t, t)
        x += alpha * p + omega * s
        r = s - omega * t
        if np.linalg.norm(r) < tol:
            break
        rho_prev = rho
    return x
