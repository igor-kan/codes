"""Neal's Stepping-Out and Shrinkage Slice Sampler for 1D Distributions."""
import numpy as np
from typing import Callable


def slice_sample_1d(log_pdf: Callable, x0: float, n_samples: int, w: float = 1.0, seed: int = 42) -> np.ndarray:
    """Generate samples using 1D slice sampling."""
    np.random.seed(seed)
    samples = np.zeros(n_samples)
    x = x0
    for i in range(n_samples):
        log_y = log_pdf(x) - np.random.exponential(1.0)
        # Stepping out
        L = x - w * np.random.rand()
        R = L + w
        while log_pdf(L) > log_y:
            L -= w
        while log_pdf(R) > log_y:
            R += w
        # Shrinkage
        while True:
            x_cand = np.random.uniform(L, R)
            if log_pdf(x_cand) > log_y:
                x = x_cand
                break
            elif x_cand < x:
                L = x_cand
            else:
                R = x_cand
        samples[i] = x
    return samples
