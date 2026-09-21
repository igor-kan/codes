"""
Grassberger-Procaccia Algorithm for Correlation Dimension D_2.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 14; Grassberger & Procaccia (1983).
"""
import numpy as np

def correlation_sum(points: np.ndarray, r: float) -> float:
    """
    C(r) = (2 / N(N-1)) sum_{i < j} Theta(r - ||x_i - x_j||).
    """
    n = len(points)
    count = 0
    for i in range(n):
        dists = np.linalg.norm(points[i+1:] - points[i], axis=1)
        count += np.sum(dists < r)
    total_pairs = n * (n - 1) / 2.0
    return float(count / total_pairs)
