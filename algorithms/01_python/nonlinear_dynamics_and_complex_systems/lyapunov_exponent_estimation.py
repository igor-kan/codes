"""
Largest Lyapunov Exponent Estimation from 1D Discrete Chaotic Maps.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 13.
"""
import numpy as np
from typing import Callable

def estimate_1d_lyapunov(map_func: Callable[[float], float],
                         deriv_func: Callable[[float], float],
                         x0: float, n_iterations: int = 5000, n_transient: int = 500) -> float:
    """
    lambda = lim_{n -> infty} (1 / n) sum_{i=0}^{n-1} ln |f'(x_i)|.
    """
    x = x0
    for _ in range(n_transient):
        x = map_func(x)
        
    lyap_sum = 0.0
    for _ in range(n_iterations):
        df = abs(deriv_func(x))
        if df > 0:
            lyap_sum += np.log(df)
        x = map_func(x)
        
    return float(lyap_sum / n_iterations)
