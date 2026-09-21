"""
Takens' Delay Embedding Theorem for Phase-Space Reconstruction.
Reference: Gershenfeld, The Nature of Mathematical Modeling, Ch. 14; Takens (1981).
"""
import numpy as np

def delay_embed_1d(time_series: np.ndarray, embedding_dim: int, delay: int) -> np.ndarray:
    """
    Constructs delay matrix Y_i = [x_i, x_{i + delay}, ..., x_{i + (m - 1) * delay}].
    """
    n = len(time_series)
    max_idx = n - (embedding_dim - 1) * delay
    if max_idx <= 0:
        raise ValueError("Time series too short for given embedding dimension and delay.")
        
    embedded = np.zeros((max_idx, embedding_dim))
    for m in range(embedding_dim):
        embedded[:, m] = time_series[m * delay : max_idx + m * delay]
    return embedded
