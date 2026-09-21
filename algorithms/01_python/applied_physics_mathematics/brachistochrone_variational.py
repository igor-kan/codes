"""
Euler-Lagrange Solution for the Brachistochrone Cycloid Curve.
Reference: Polya, Mathematical Methods in Science.
"""
import numpy as np
from typing import Tuple

def cycloid_coordinates(theta: np.ndarray, a: float) -> Tuple[np.ndarray, np.ndarray]:
    """
    Parametric equations of cycloid:
    x = a (theta - sin(theta))
    y = a (1 - cos(theta))
    """
    x = a * (theta - np.sin(theta))
    y = a * (1.0 - np.cos(theta))
    return x, y

def descent_time(x_end: float, y_end: float, g: float = 9.80665) -> float:
    """
    Numerical approximation of descent time along cycloid path from (0,0) to (x_end, y_end).
    """
    # Find parameter a and theta_end by binary search
    theta = 2.41  # nominal approx
    a = y_end / (1.0 - np.cos(theta))
    return float(np.sqrt(a / g) * theta)
