"""Natural and Clamped Cubic Spline Interpolation with Tridiagonal Matrix Solve."""
import numpy as np


def natural_cubic_spline_coefficients(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    """Compute second derivative moments M_i for natural boundary conditions."""
    n = len(x) - 1
    h = np.diff(x)
    mu = np.zeros(n)
    lam = np.zeros(n)
    d = np.zeros(n + 1)
    
    A = np.zeros((n + 1, n + 1))
    A[0, 0] = 1.0
    A[n, n] = 1.0
    
    for i in range(1, n):
        A[i, i - 1] = h[i - 1]
        A[i, i] = 2.0 * (h[i - 1] + h[i])
        A[i, i + 1] = h[i]
        d[i] = 6.0 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])
        
    M = np.linalg.solve(A, d)
    return M
