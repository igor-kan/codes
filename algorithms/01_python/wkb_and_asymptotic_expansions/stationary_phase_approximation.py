"""Stationary Phase Approximation for Rapidly Oscillating Fourier Integrals."""
import numpy as np


def stationary_phase_fourier(phi0: float, phi_double_prime: float, k: float) -> complex:
    """I(k) approx sqrt(2 * pi / (k * |phi''(c)|)) * exp(i * k * phi0 + i * pi/4 * sgn(phi''))."""
    sgn = 1.0 if phi_double_prime > 0 else -1.0
    amp = np.sqrt(2.0 * np.pi / (k * abs(phi_double_prime)))
    phase = k * phi0 + (np.pi / 4.0) * sgn
    return complex(amp * np.exp(1j * phase))
