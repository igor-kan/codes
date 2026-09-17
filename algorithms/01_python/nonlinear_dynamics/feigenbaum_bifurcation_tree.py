"""Logistic Map Period Doubling and Feigenbaum Universality."""

from typing import List, Tuple
import numpy as np


class FeigenbaumCascade:
    """Analyzes the logistic map: x_{n+1} = r * x_n * (1 - x_n)."""

    FEIGENBAUM_DELTA = 4.66920160910299
    FEIGENBAUM_ALPHA = 2.50290787509589

    @classmethod
    def iterate(cls, r: float, x0: float = 0.5, n_transient: int = 500, n_samples: int = 100) -> np.ndarray:
        """Returns attractor samples after discarding transient iterations."""
        x = x0
        for _ in range(n_transient):
            x = r * x * (1.0 - x)

        samples = np.zeros(n_samples)
        for i in range(n_samples):
            x = r * x * (1.0 - x)
            samples[i] = x
        return samples

    @classmethod
    def lyapunov_exponent(cls, r: float, x0: float = 0.2, n_iterations: int = 5000) -> float:
        """lambda = lim (1/N) * sum ln|r * (1 - 2*x_n)|."""
        x = x0
        total = 0.0
        for _ in range(n_iterations):
            deriv = np.abs(r * (1.0 - 2.0 * x))
            if deriv > 1e-12:
                total += np.log(deriv)
            x = r * x * (1.0 - x)
        return total / n_iterations
