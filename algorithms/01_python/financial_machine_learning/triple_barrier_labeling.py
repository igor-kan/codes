"""
Triple Barrier Labeling Method for Financial Event Detection.
Reference: Marcos Lopez de Prado, Advances in Financial Machine Learning, Ch. 3.
"""
import numpy as np

def apply_triple_barrier(prices: np.ndarray, upper_factor: float = 0.02,
                         lower_factor: float = 0.02, max_holding: int = 10) -> np.ndarray:
    """
    Labels each event:
    +1: Upper profit-taking barrier touched first
    -1: Lower stop-loss barrier touched first
     0: Vertical time barrier touched first
    """
    n = len(prices)
    labels = np.zeros(n, dtype=int)
    
    for i in range(n):
        p0 = prices[i]
        upper = p0 * (1.0 + upper_factor)
        lower = p0 * (1.0 - lower_factor)
        end_idx = min(i + max_holding, n)
        
        for t in range(i + 1, end_idx):
            if prices[t] >= upper:
                labels[i] = 1
                break
            elif prices[t] <= lower:
                labels[i] = -1
                break
    return labels
