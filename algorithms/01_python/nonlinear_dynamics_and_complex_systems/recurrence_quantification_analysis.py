"""
Recurrence Quantification Analysis (RQA) Recurrence Rate (RR).
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 14; Marwan et al. (2007).
"""
import numpy as np

def recurrence_rate(embedded_series: np.ndarray, threshold: float) -> float:
    """RR = (1 / N^2) sum_{i, j} Theta(eps - ||x_i - x_j||)."""
    n = len(embedded_series)
    diffs = embedded_series[:, None, :] - embedded_series[None, :, :]
    dists = np.linalg.norm(diffs, axis=2)
    recurrent = np.sum(dists < threshold)
    return float(recurrent / (n**2))
