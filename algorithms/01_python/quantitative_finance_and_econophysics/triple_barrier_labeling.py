"""
De Prado's Triple Barrier Method for Financial Labeling.
References: Marcos Lopez de Prado - Advances in Financial Machine Learning (Ch. 3).
"""
import numpy as np

def apply_triple_barrier(prices: np.ndarray, pt_mult: float = 1.0, sl_mult: float = 1.0, max_holding: int = 10, vol: float = 0.02) -> list:
    """
    Apply triple barrier labeling:
    +1: Upper profit-taking barrier touched first
    -1: Lower stop-loss barrier touched first
     0: Vertical time-out barrier touched
    """
    labels = []
    n = len(prices)
    for i in range(n - max_holding):
        p0 = prices[i]
        upper = p0 * (1.0 + pt_mult * vol)
        lower = p0 * (1.0 - sl_mult * vol)
        label = 0
        for step in range(1, max_holding + 1):
            p = prices[i + step]
            if p >= upper:
                label = 1
                break
            elif p <= lower:
                label = -1
                break
        labels.append(label)
    return labels
