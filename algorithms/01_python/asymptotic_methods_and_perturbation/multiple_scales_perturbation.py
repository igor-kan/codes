"""
Method of Multiple Scales for Damped Weakly Nonlinear Oscillators.
Reference: Mauch, Intro to Applied Mathematics, Ch. 28.
"""
import numpy as np

def multiple_scales_damped_envelope(t: np.ndarray, eps: float, x0: float) -> np.ndarray:
    """
    Slow scale tau = eps * t.
    Envelope A(tau) = x0 * exp(-eps * t / 2).
    """
    return x0 * np.exp(-0.5 * eps * t)
