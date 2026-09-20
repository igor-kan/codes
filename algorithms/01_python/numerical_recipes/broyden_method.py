"""
Broyden's Quasi-Newton Method for Nonlinear Systems.
References: Press et al. - Numerical Recipes (Ch. 9).
"""
import numpy as np

def broyden_solve(f_sys, x0, tol=1e-7, max_iter=100):
    """Broyden's 'good' method with rank-1 Jacobian updates."""
    x = np.array(x0, dtype=float)
    n = len(x)
    # Initial Jacobian via finite differences
    eps = 1e-6
    B = np.zeros((n, n))
    f0 = f_sys(x)
    for j in range(n):
        x_step = x.copy()
        x_step[j] += eps
        B[:, j] = (f_sys(x_step) - f0) / eps

    H = np.linalg.inv(B)  # Inverse Jacobian approximation

    for _ in range(max_iter):
        f = f_sys(x)
        if np.linalg.norm(f) < tol:
            return x
        s = -H @ f
        x_new = x + s
        f_new = f_sys(x_new)
        y = f_new - f
        
        # Sherman-Morrison update of inverse Jacobian H
        denom = np.dot(s, H @ y)
        if abs(denom) > 1e-12:
            H = H + np.outer(s - H @ y, s @ H) / denom
        x = x_new
    return x
