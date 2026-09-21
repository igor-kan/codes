"""
Conformal Compactification coordinates for Schwarzschild Carter-Penrose Diagram.
Reference: Penrose, The Road to Reality, Ch. 27 (Spacetime singularities).
"""
import numpy as np
from typing import Tuple

def kruskal_to_penrose(U: float, V: float) -> Tuple[float, float]:
    """
    Conformal compactification map from Kruskal coordinates (U, V) to Penrose coordinates (psi, xi):
    psi + xi = 2 arctan(V + U)
    psi - xi = 2 arctan(V - U)
    Both psi, xi lie in (-pi, pi).
    """
    p_plus = 2.0 * np.arctan(V + U)
    p_minus = 2.0 * np.arctan(V - U)
    psi = 0.5 * (p_plus + p_minus)
    xi = 0.5 * (p_plus - p_minus)
    return float(psi), float(xi)
