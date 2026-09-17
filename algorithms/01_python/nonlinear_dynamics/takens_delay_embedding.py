"""Takens' Delay-Coordinate Phase Space Embedding."""

import numpy as np


class TakensEmbedding:
    """Reconstructs state space from a single scalar time series x(t):
    v(t) = [x(t), x(t + tau), x(t + 2*tau), ..., x(t + (m-1)*tau)]
    """

    @classmethod
    def embed(cls, time_series: np.ndarray, dimension_m: int, delay_tau: int) -> np.ndarray:
        """Constructs delay coordinate embedded matrix of shape (N - (m-1)*tau, m)."""
        n = len(time_series)
        n_vectors = n - (dimension_m - 1) * delay_tau
        if n_vectors <= 0:
            raise ValueError("Time series too short for given embedding dimension and delay.")

        embedded = np.zeros((n_vectors, dimension_m))
        for j in range(dimension_m):
            embedded[:, j] = time_series[j * delay_tau : j * delay_tau + n_vectors]

        return embedded
