"""
Hardy-Weinberg Equilibrium Dynamics with Viability Selection.
Reference: Campbell Biology (12th Ed.), Ch. 23 (The Evolution of Populations).
"""
import numpy as np
from typing import Tuple

def next_generation_allele_frequency(p: float, w_AA: float, w_Aa: float, w_aa: float) -> Tuple[float, float]:
    """
    Computes allele frequency p' in the next generation given fitnesses w_AA, w_Aa, w_aa:
    mean_w = p^2 w_AA + 2 p q w_Aa + q^2 w_aa
    p' = (p^2 w_AA + p q w_Aa) / mean_w
    """
    q = 1.0 - p
    mean_w = (p**2) * w_AA + 2.0 * p * q * w_Aa + (q**2) * w_aa
    p_prime = ((p**2) * w_AA + p * q * w_Aa) / mean_w
    return float(p_prime), float(mean_w)
