"""
Shannon and Lempel-Ziv Entropy Rate Estimator for Time Series.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 18.
"""
import numpy as np
from collections import Counter

def shannon_entropy(binary_seq: str) -> float:
    """H = - sum p_i log2(p_i)."""
    n = len(binary_seq)
    if n == 0: return 0.0
    counts = Counter(binary_seq)
    h = 0.0
    for c, cnt in counts.items():
        p = cnt / n
        h -= p * np.log2(p)
    return float(h)
