"""Crank-Nicolson Unconditionally Stable Method for 1D Heat Equation."""
import numpy as np


def crank_nicolson_1d(u0: np.ndarray, alpha: float, dx: float, dt: float, n_steps: int) -> np.ndarray:
    """Solve u_t = alpha * u_xx over n_steps."""
    r = alpha * dt / (2.0 * dx**2)
    n = len(u0)
    
    main_A = (1.0 + 2.0 * r) * np.ones(n - 2)
    off_A = -r * np.ones(n - 3)
    A = np.diag(main_A) + np.diag(off_A, 1) + np.diag(off_A, -1)
    
    main_B = (1.0 - 2.0 * r) * np.ones(n - 2)
    off_B = r * np.ones(n - 3)
    B = np.diag(main_B) + np.diag(off_B, 1) + np.diag(off_B, -1)
    
    u = u0.copy()
    for _ in range(n_steps):
        rhs = B @ u[1:-1]
        u[1:-1] = np.linalg.solve(A, rhs)
    return u
