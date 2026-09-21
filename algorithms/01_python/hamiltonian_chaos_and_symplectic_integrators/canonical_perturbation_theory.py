"""Lie Transform Canonical Perturbation Theory.

Averaging of non-resonant fast phase angles to derive adiabatic invariants
and secular drift equations.
"""
import numpy as np
from typing import Callable


def secular_drift_averaged(theta: np.ndarray, H1_gradient_fn: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    """Average perturbative force over 2*pi fast angle orbit to find secular drift."""
    n_samples = len(theta)
    drift = np.zeros_like(H1_gradient_fn(theta[0]))
    for th in theta:
        drift += H1_gradient_fn(th)
    return drift / n_samples
