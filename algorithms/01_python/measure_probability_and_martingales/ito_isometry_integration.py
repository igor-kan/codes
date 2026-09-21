"""
Numerical Ito Stochastic Integral and Verification of Ito Isometry.
Reference: Evans & Rosenthal; Oksendal, Stochastic Differential Equations.
"""
import numpy as np

def ito_integral_euler(f_func, W_path: np.ndarray, time_grid: np.ndarray) -> float:
    """
    Evaluates int_0^T f(t) dW_t = sum_k f(t_k) (W_{k+1} - W_k).
    """
    f_vals = f_func(time_grid[:-1])
    dW = np.diff(W_path)
    return float(np.sum(f_vals * dW))
