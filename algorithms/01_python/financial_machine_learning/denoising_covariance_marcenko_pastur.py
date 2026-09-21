"""
Marcenko-Pastur Random Matrix Denoising of Empirical Covariance.
Reference: Marcos Lopez de Prado, Machine Learning for Asset Managers, Ch. 2.
"""
import numpy as np
from typing import Tuple

def marcenko_pastur_bounds(var: float, q: float) -> Tuple[float, float]:
    """
    lambda_{min, max} = var * (1 +- sqrt(1/q))^2 where q = T / N >= 1.
    """
    l_min = var * (1.0 - np.sqrt(1.0 / q))**2
    l_max = var * (1.0 + np.sqrt(1.0 / q))**2
    return float(l_min), float(l_max)
