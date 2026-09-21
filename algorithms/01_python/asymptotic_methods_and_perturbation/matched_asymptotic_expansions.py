"""
Matched Asymptotic Expansions for Singular Boundary Layer Problems:
eps y'' + y' + y = 0, y(0)=0, y(1)=1.
Reference: Mauch, Intro to Applied Mathematics, Ch. 29.
"""
import numpy as np

def composite_boundary_layer_solution(x: np.ndarray, eps: float) -> np.ndarray:
    """
    Outer solution: y_out = exp(1 - x).
    Inner solution: y_in = exp(1) * (1 - exp(-x / eps)).
    Composite additive solution: y_comp = exp(1 - x) - exp(1 - x / eps).
    """
    return np.exp(1.0 - x) - np.exp(1.0 - x / eps)
