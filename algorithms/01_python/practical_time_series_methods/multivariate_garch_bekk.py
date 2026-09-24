"""BEKK(1,1,1) Multivariate GARCH Positive Definite Covariance Structure."""
import numpy as np


def bekk_covariance_step(C: np.ndarray, A: np.ndarray, B: np.ndarray,
                         eps_prev: np.ndarray, H_prev: np.ndarray) -> np.ndarray:
    """H_t = C C^T + A (eps_{t-1} eps_{t-1}^T) A^T + B H_{t-1} B^T."""
    return C @ C.T + A @ np.outer(eps_prev, eps_prev) @ A.T + B @ H_prev @ B.T
