"""
Lie bracket [X, Y] and Lie derivative of vector fields.
Reference: Penrose, The Road to Reality, Ch. 12 & 14.
"""
import numpy as np
from typing import Callable

def lie_bracket_numerical(X_func: Callable[[np.ndarray], np.ndarray],
                          Y_func: Callable[[np.ndarray], np.ndarray],
                          x: np.ndarray, eps: float = 1e-5) -> np.ndarray:
    """
    Computes the Lie bracket [X, Y]^a = X^b d_b Y^a - Y^b d_b X^a at point x.
    """
    dim = len(x)
    jac_Y = np.zeros((dim, dim))
    jac_X = np.zeros((dim, dim))
    
    for i in range(dim):
        dx = np.zeros(dim)
        dx[i] = eps
        jac_Y[:, i] = (Y_func(x + dx) - Y_func(x - dx)) / (2.0 * eps)
        jac_X[:, i] = (X_func(x + dx) - X_func(x - dx)) / (2.0 * eps)
        
    X_val = X_func(x)
    Y_val = Y_func(x)
    
    bracket = jac_Y @ X_val - jac_X @ Y_val
    return bracket
