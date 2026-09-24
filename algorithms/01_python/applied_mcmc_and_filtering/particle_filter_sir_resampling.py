"""Sequential Importance Resampling (SIR) Systematic Resampling Algorithm."""
import numpy as np


def systematic_resample(weights: np.ndarray) -> np.ndarray:
    """Systematic resampling of particles based on normalized weights."""
    N = len(weights)
    positions = (np.arange(N) + np.random.rand()) / N
    indexes = np.zeros(N, dtype=int)
    cumulative_sum = np.cumsum(weights)
    i, j = 0, 0
    while i < N:
        if positions[i] < cumulative_sum[j]:
            indexes[i] = j
            i += 1
        else:
            j += 1
    return indexes
