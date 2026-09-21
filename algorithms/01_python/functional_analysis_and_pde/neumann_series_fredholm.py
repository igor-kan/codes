"""
Neumann Series Solution for Fredholm Integral Equations of Second Kind:
phi(x) = f(x) + lambda int_a^b K(x, y) phi(y) dy.
Reference: Hassani, Mathematical Methods for Physics, Ch. 24.
"""
import numpy as np

def solve_fredholm_neumann(K_matrix: np.ndarray, f_vec: np.ndarray, lam: float, dx: float, max_iter: int = 25) -> np.ndarray:
    """
    phi = (I - lambda K)^{-1} f = sum_{m=0}^infty (lambda K dx)^m f.
    """
    phi = f_vec.copy()
    current = f_vec.copy()
    op = lam * K_matrix * dx
    
    for _ in range(max_iter):
        current = op @ current
        phi += current
        if np.linalg.norm(current) < 1e-12:
            break
    return phi
