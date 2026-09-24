"""Sequential Monte Carlo Effective Sample Size (ESS) Diagnostic."""
import numpy as np


def effective_sample_size(weights: np.ndarray) -> float:
    """ESS = 1 / sum(w_i^2)."""
    norm_w = weights / np.sum(weights)
    return float(1.0 / np.sum(norm_w**2))
