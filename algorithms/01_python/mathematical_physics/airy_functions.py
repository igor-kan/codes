"""
Airy Functions Ai(x) and Bi(x).
References: Arfken, Weber, Harris - Mathematical Methods for Physicists.
"""
import numpy as np
from scipy.special import airy

def airy_ai(x: np.ndarray) -> np.ndarray:
    """Airy function of the first kind Ai(x)."""
    return airy(x)[0]

def airy_bi(x: np.ndarray) -> np.ndarray:
    """Airy function of the second kind Bi(x)."""
    return airy(x)[2]
