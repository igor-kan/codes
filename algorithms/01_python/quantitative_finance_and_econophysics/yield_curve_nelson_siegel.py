"""
Nelson-Siegel Yield Curve Term Structure Model.
References: Pal - Practical Time Series Analysis.
"""
import numpy as np

def nelson_siegel_zero_rate(t: np.ndarray, beta0: float, beta1: float, beta2: float, tau: float) -> np.ndarray:
    """
    Nelson-Siegel forward/zero curve:
    y(t) = beta0 + beta1 * (1 - exp(-t/tau))/(t/tau) + beta2 * ((1 - exp(-t/tau))/(t/tau) - exp(-t/tau)).
    """
    t = np.asarray(t, dtype=float)
    ratio = np.where(t > 1e-6, (1.0 - np.exp(-t / tau)) / (t / tau), 1.0)
    exp_term = np.exp(-t / tau)
    return beta0 + beta1 * ratio + beta2 * (ratio - exp_term)
