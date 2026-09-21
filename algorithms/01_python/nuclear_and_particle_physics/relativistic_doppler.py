"""
Relativistic Longitudinal and Transverse Doppler Effects.
References: Halliday, Resnick, Krane - Physics (Vol. 2).
"""
import numpy as np

def relativistic_longitudinal_doppler(f0: float, beta: float) -> float:
    """f = f0 * sqrt((1 - beta)/(1 + beta)) for receding source (beta > 0)."""
    return float(f0 * np.sqrt((1.0 - beta) / (1.0 + beta)))

def relativistic_transverse_doppler(f0: float, beta: float) -> float:
    """Pure time dilation transverse Doppler shift f = f0 * sqrt(1 - beta^2)."""
    return float(f0 * np.sqrt(1.0 - beta**2))
