"""
Stratonovich Midpoint Stochastic Integral and Drift Conversion.
Reference: Evans & Rosenthal; Gardiner, Stochastic Methods.
"""
import numpy as np

def stratonovich_integral(f_func, W_path: np.ndarray, time_grid: np.ndarray) -> float:
    """
    int_0^T f(W_t) o dW_t = sum_k f( (W_k + W_{k+1})/2 ) (W_{k+1} - W_k).
    """
    w_mid = 0.5 * (W_path[:-1] + W_path[1:])
    f_vals = f_func(w_mid)
    dW = np.diff(W_path)
    return float(np.sum(f_vals * dW))
