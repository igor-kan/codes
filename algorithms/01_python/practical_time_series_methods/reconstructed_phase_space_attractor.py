"""Time-Delay Coordinate Embedding for Strange Attractor Reconstruction."""
import numpy as np


def time_delay_embedding(series: np.ndarray, delay: int, dimension: int) -> np.ndarray:
    """Construct delay vectors [x(t), x(t-tau), ..., x(t-(m-1)tau)]."""
    n = len(series)
    max_offset = (dimension - 1) * delay
    if n <= max_offset:
        raise ValueError("Series length too short for embedding parameters")
    n_vectors = n - max_offset
    Y = np.zeros((n_vectors, dimension))
    for i in range(dimension):
        Y[:, i] = series[i * delay:i * delay + n_vectors]
    return Y
