"""
Numerical Evaluation of the Mellin Transform: M[f](s) = int_0^infty x^{s-1} f(x) dx.
Reference: Blennow, Mathematical Methods for Physics and Engineering, Ch. 6.
"""
import numpy as np
from typing import Callable

def mellin_transform_quad(f: Callable[[float], float], s: complex,
                          x_min: float = 1e-4, x_max: float = 20.0, n_points: int = 2000) -> complex:
    """
    Numerically computes Mellin transform using log-spaced trapezoidal quadrature.
    x = e^u, dx = e^u du.
    """
    u = np.linspace(np.log(x_min), np.log(x_max), n_points)
    du = u[1] - u[0]
    x = np.exp(u)
    # Integrand in u: exp(s * u) * f(exp(u))
    integrand = np.exp(s * u) * np.array([f(xi) for xi in x])
    integral = np.trapz(integrand, dx=du)
    return complex(integral)
