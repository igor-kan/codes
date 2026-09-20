"""
Electromagnetic Skin Depth in Conductive Media.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists.
"""
import numpy as np

def skin_depth(omega: float, sigma: float, mu: float = 1.0) -> float:
    """Skin depth delta = sqrt(2 / (omega * mu * sigma))."""
    return float(np.sqrt(2.0 / (omega * mu * sigma)))
