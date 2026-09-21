"""
Numerical Cauchy Principal Value Integral around a simple pole: P.V. int_{-a}^b f(x)/(x - x0) dx.
Reference: Hassani, Mathematical Methods for Physics, Ch. 11.
"""
import numpy as np
from typing import Callable

def cauchy_principal_value_symmetric(f: Callable[[float], float], x0: float,
                                     a: float, b: float, eps: float = 1e-5, n_pts: int = 1000) -> float:
    """
    P.V. int_a^b f(x)/(x - x0) dx = lim_{eps -> 0} [ int_a^{x0 - eps} + int_{x0 + eps}^b ].
    """
    # Left segment
    x_left = np.linspace(a, x0 - eps, n_pts)
    y_left = np.array([f(x) / (x - x0) for x in x_left])
    int_left = np.trapz(y_left, x_left)
    
    # Right segment
    x_right = np.linspace(x0 + eps, b, n_pts)
    y_right = np.array([f(x) / (x - x0) for x in x_right])
    int_right = np.trapz(y_right, x_right)
    
    return float(int_left + int_right)
