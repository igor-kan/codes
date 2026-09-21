"""
Bet Sizing via Gaussian Sigmoid Mapping from Model Probabilities.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 10.
"""
import numpy as np
from scipy.stats import norm

def compute_bet_size(prob: float, num_classes: int = 2) -> float:
    """
    m = 2 * N( (p - 1/k) / sqrt(p*(1-p)) ) - 1.
    """
    p_null = 1.0 / num_classes
    if np.isclose(prob, 1.0): return 1.0
    if np.isclose(prob, 0.0): return -1.0
    
    z = (prob - p_null) / np.sqrt(prob * (1.0 - prob))
    m = 2.0 * norm.cdf(z) - 1.0
    return float(m)
