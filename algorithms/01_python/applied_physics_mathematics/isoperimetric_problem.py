"""
Isoperimetric Problem and Discrete Polygon Area Maximization.
Reference: Polya, Mathematical Methods in Science, Ch. 6.
"""
import numpy as np

def isoperimetric_quotient(area: float, perimeter: float) -> float:
    """
    Isoperimetric quotient Q = 4 pi Area / Perimeter^2.
    For circle, Q = 1. For any other shape, Q < 1.
    """
    return float(4.0 * np.pi * area / (perimeter**2))

def regular_polygon_isoperimetric(n_sides: int) -> float:
    """
    Q_n = (pi / n) / tan(pi / n). As n -> infty, Q_n -> 1.
    """
    return float((np.pi / n_sides) / np.tan(np.pi / n_sides))
