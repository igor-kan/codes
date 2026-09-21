"""
Fermat's Principle Ray Tracing in Gradient-Index (GRIN) Media.
Reference: Polya, Mathematical Methods in Science, Ch. 2.
"""
import numpy as np
from typing import Callable, Tuple

def trace_ray_grin(n_func: Callable[[float, float], float],
                   grad_n_func: Callable[[float, float], Tuple[float, float]],
                   start_pos: Tuple[float, float],
                   initial_angle: float,
                   steps: int = 100, ds: float = 0.05) -> np.ndarray:
    """
    Ray equation from Fermat's principle: d/ds (n dr/ds) = grad n.
    """
    traj = np.zeros((steps, 2))
    pos = np.array(start_pos, dtype=float)
    dr_ds = np.array([np.cos(initial_angle), np.sin(initial_angle)], dtype=float)
    
    for i in range(steps):
        traj[i] = pos
        n_val = n_func(pos[0], pos[1])
        grad_n = np.array(grad_n_func(pos[0], pos[1]))
        
        # d^2 r / ds^2 = (1/n) (grad n - (dr/ds . grad n) dr/ds)
        tangential_grad = np.dot(dr_ds, grad_n)
        d2r = (grad_n - tangential_grad * dr_ds) / n_val
        
        dr_ds += d2r * ds
        dr_ds /= np.linalg.norm(dr_ds)
        pos += dr_ds * ds
        
    return traj
