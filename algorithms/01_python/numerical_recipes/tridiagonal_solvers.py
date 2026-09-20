"""
Tridiagonal Matrix Solvers: Thomas Algorithm & Cyclic Tridiagonal Solver.
References: Press et al. - Numerical Recipes (Ch. 2).
"""
import numpy as np

def thomas_algorithm(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> np.ndarray:
    """
    Solves A x = d for tridiagonal A:
    a: subdiagonal (length n-1)
    b: main diagonal (length n)
    c: superdiagonal (length n-1)
    d: right hand side (length n)
    """
    n = len(b)
    c_prime = np.zeros(n - 1)
    d_prime = np.zeros(n)

    c_prime[0] = c[0] / b[0]
    d_prime[0] = d[0] / b[0]

    for i in range(1, n - 1):
        denom = b[i] - a[i - 1] * c_prime[i - 1]
        c_prime[i] = c[i] / denom
        d_prime[i] = (d[i] - a[i - 1] * d_prime[i - 1]) / denom

    d_prime[n - 1] = (d[n - 1] - a[n - 2] * d_prime[n - 2]) / (b[n - 1] - a[n - 2] * c_prime[n - 2])

    x = np.zeros(n)
    x[n - 1] = d_prime[n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = d_prime[i] - c_prime[i] * x[i + 1]

    return x
