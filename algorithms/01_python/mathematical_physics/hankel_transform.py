"""
Quasi-Discrete Hankel Transform (Fourier-Bessel Transform).
References: Riley, Hobson, Bence - Mathematical Methods for Physics and Engineering (Ch. 13).
"""
import numpy as np
from bessel_functions import bessel_j0

def hankel_transform_0(func, k_grid: np.ndarray, r_max: float = 20.0, n_points: int = 1000) -> np.ndarray:
    """Compute 0-th order Hankel transform: F(k) = int_0^inf f(r) J_0(k*r) r dr."""
    r = np.linspace(1e-5, r_max, n_points)
    dr = r[1] - r[0]
    f_r = func(r)
    
    F_k = np.zeros_like(k_grid, dtype=float)
    for idx, k in enumerate(k_grid):
        kernel = np.array([bessel_j0(float(k * ri)) for ri in r])
        integrand = f_r * kernel * r
        F_k[idx] = np.trapezoid(integrand, r)
    return F_k
