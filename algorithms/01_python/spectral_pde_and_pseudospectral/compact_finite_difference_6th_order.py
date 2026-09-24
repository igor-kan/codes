"""4th-Order Tridiagonal Pade Compact Finite Difference First Derivative."""
import numpy as np


def solve_compact_derivative_1d(u: np.ndarray, dx: float) -> np.ndarray:
    """Solve alpha * f'_{i-1} + f'_i + alpha * f'_{i+1} = a * (f_{i+1} - f_{i-1}) / (2 dx) with periodic boundaries."""
    N = len(u)
    alpha = 0.25
    a = 1.5
    
    A = np.eye(N) + alpha * np.roll(np.eye(N), 1, axis=1) + alpha * np.roll(np.eye(N), -1, axis=1)
    b = a * (np.roll(u, -1) - np.roll(u, 1)) / (2.0 * dx)
    return np.linalg.solve(A, b)
