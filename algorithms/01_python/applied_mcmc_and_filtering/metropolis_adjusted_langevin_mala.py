"""MALA: Metropolis-Adjusted Langevin Algorithm."""
import numpy as np
from typing import Callable


def mala_proposal(x: np.ndarray, grad_log_p: Callable, tau: float) -> np.ndarray:
    """x' = x + tau * grad_log_p(x) + sqrt(2 * tau) * xi."""
    return x + tau * grad_log_p(x) + np.sqrt(2.0 * tau) * np.random.standard_normal(x.shape)
