"""
Synchrotron Radiation Spectrum and Critical Frequency.
References: Landau & Lifshitz - The Classical Theory of Fields (Vol. 2, Ch. 9).
"""
import numpy as np

def critical_frequency(gamma: float, B: float, q: float = 1.0, m: float = 1.0, c: float = 1.0) -> float:
    """Critical synchrotron frequency omega_c = (3/2) gamma^3 (q B / m)."""
    omega_0 = q * B / (m * c)
    return 1.5 * (gamma**3) * omega_0

def total_synchrotron_power(gamma: float, B: float, q: float = 1.0, m: float = 1.0, c: float = 1.0) -> float:
    """Total relativistic emitted power P = (2/3) (q^4 B^2 / (m^2 c^3)) gamma^2 beta^2."""
    beta = np.sqrt(1.0 - 1.0 / (gamma**2))
    factor = (2.0 / 3.0) * (q**4 * B**2 / (m**2 * c**3))
    return float(factor * (gamma**2) * (beta**2))
