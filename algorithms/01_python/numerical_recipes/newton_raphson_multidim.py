"""
Multidimensional Newton-Raphson Solver with Backtracking Line Search.
References: Press et al. - Numerical Recipes (Ch. 9).
"""
import numpy as np

def newton_raphson_multidim(f_sys, j_sys, x0, tol=1e-8, max_iter=100):
    """Solve F(x) = 0 using Newton-Raphson with Armijo backtracking."""
    x = np.array(x0, dtype=float)
    for _ in range(max_iter):
        F = f_sys(x)
        if np.linalg.norm(F) < tol:
            return x
        J = j_sys(x)
        dx = np.linalg.solve(J, -F)

        # Backtracking line search
        alpha = 1.0
        f_norm = np.linalg.norm(F)
        while alpha > 1e-4:
            x_new = x + alpha * dx
            if np.linalg.norm(f_sys(x_new)) < f_norm:
                break
            alpha *= 0.5

        x = x + alpha * dx
    return x
