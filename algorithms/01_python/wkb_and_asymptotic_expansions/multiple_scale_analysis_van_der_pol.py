"""Multiple Scale Analysis for Van der Pol Limit Cycle Amplitude."""
import numpy as np


def van_der_pol_amplitude_envelope(A0: float, eps: float, t: np.ndarray) -> np.ndarray:
    """A(t) = 2 / sqrt(1 + (4/A0^2 - 1) * exp(-eps * t)). Approaches limit cycle 2."""
    return 2.0 / np.sqrt(1.0 + (4.0 / (A0**2) - 1.0) * np.exp(-eps * t))
