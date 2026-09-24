"""Levenberg-Marquardt Damped Least Squares Non-Linear Optimization."""
import numpy as np


def levenberg_marquardt_fit(residual_fn, jacobian_fn, p0: np.ndarray,
                            lam: float = 1e-2, max_iter: int = 50) -> np.ndarray:
    """Optimize parameters p minimizing sum of squares of residuals."""
    p = p0.copy().astype(float)
    for _ in range(max_iter):
        r = residual_fn(p)
        J = jacobian_fn(p)
        H = J.T @ J
        H_damped = H + lam * np.diag(np.diag(H) + 1e-4)
        g = J.T @ r
        step = np.linalg.solve(H_damped, -g)
        p_new = p + step
        if np.sum(residual_fn(p_new)**2) < np.sum(r**2):
            p = p_new
            lam /= 2.0
            if np.linalg.norm(step) < 1e-7:
                break
        else:
            lam *= 4.0
    return p
