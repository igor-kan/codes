"""
Method of Stationary Phase for Rapidly Oscillating Integrals int g(t) exp(i k f(t)) dt.
Reference: Mauch, Intro to Applied Mathematics, Ch. 27; Blennow.
"""
import numpy as np

def stationary_phase_eval(g_t0: float, f_t0: float, f_double_prime: float, k: float) -> complex:
    """
    I(k) approx sqrt(2 pi / (k |f''(t0)|)) g(t0) exp(i k f(t0) + i (pi / 4) sgn(f''(t0))).
    """
    if f_double_prime == 0.0:
        raise ValueError("f''(t0) must be non-zero for simple stationary phase.")
    sigma = np.sign(f_double_prime)
    amp = np.sqrt(2.0 * np.pi / (k * abs(f_double_prime))) * g_t0
    phase = k * f_t0 + sigma * (np.pi / 4.0)
    return complex(amp * np.exp(1j * phase))
