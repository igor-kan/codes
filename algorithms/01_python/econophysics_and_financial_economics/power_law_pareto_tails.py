"""Hill Estimator for Heavy-Tailed Financial Returns and Pareto Exponents.

Hill index: alpha_H = ( 1/k * sum_{i=1}^k ln(X_(n-i+1) / X_(n-k)) )^(-1).
"""
import numpy as np


def hill_estimator_tail_index(data: np.ndarray, k: int) -> float:
    """Estimate Pareto tail index alpha for top k order statistics."""
    pos_data = np.abs(data[data != 0])
    sorted_data = np.sort(pos_data)
    n = len(sorted_data)
    if k >= n or k < 2:
        raise ValueError("k must satisfy 2 <= k < n")
    
    threshold = sorted_data[n - k - 1]
    tail = sorted_data[n - k:]
    hill_sum = np.sum(np.log(tail / threshold)) / k
    return float(1.0 / hill_sum)
