"""Stirling Asymptotic Series Expansion for Factorials and Gamma Functions."""
import numpy as np


def stirling_log_gamma(n: float) -> float:
    """ln Gamma(n) approx (n - 0.5)*ln(n) - n + 0.5*ln(2*pi) + 1/(12n)."""
    return float((n - 0.5) * np.log(n) - n + 0.5 * np.log(2.0 * np.pi) + 1.0 / (12.0 * n))
