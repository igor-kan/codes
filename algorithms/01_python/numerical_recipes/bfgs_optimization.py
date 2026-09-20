"""
BFGS Quasi-Newton Optimization with Inverse Hessian Updating.
References: Press et al. - Numerical Recipes (Ch. 10).
"""
import numpy as np

def bfgs_optimize(func, grad_func, x0, tol=1e-6, max_iter=200):
    """BFGS unconstrained minimization."""
    x = np.array(x0, dtype=float)
    n = len(x)
    H = np.eye(n)  # Initial inverse Hessian approximation

    for _ in range(max_iter):
        g = grad_func(x)
        if np.linalg.norm(g) < tol:
            break
        p = -H @ g

        # Backtracking line search (Armijo condition)
        alpha = 1.0
        c1 = 1e-4
        f_curr = func(x)
        while func(x + alpha * p) > f_curr + c1 * alpha * np.dot(g, p):
            alpha *= 0.5
            if alpha < 1e-8:
                break

        s = alpha * p
        x_next = x + s
        g_next = grad_func(x_next)
        y = g_next - g

        # Update H via BFGS formula
        rho = 1.0 / np.dot(y, s)
        if np.isfinite(rho) and rho > 0:
            I = np.eye(n)
            H = (I - rho * np.outer(s, y)) @ H @ (I - rho * np.outer(y, s)) + rho * np.outer(s, s)

        x = x_next

    return x
