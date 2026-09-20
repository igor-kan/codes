"""
Kramers-Kronig Relations & Hilbert Transform.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists (Ch. 11).
"""
import numpy as np
from scipy.signal import hilbert

def kramers_kronig_real_from_imag(omega: np.ndarray, chi_imag: np.ndarray) -> np.ndarray:
    """
    Compute chi_real(omega) from chi_imag(omega) using Kramers-Kronig relation:
    chi_real(omega) = (2/pi) P.V. int_0^inf [s * chi_imag(s) / (s^2 - omega^2)] ds
    """
    # Use standard Hilbert transform property: chi_real = -H[chi_imag]
    # For causal response functions, hilbert(x) produces x + i H[x]
    analytic_signal = hilbert(chi_imag)
    return -analytic_signal.imag

def kramers_kronig_imag_from_real(omega: np.ndarray, chi_real: np.ndarray) -> np.ndarray:
    """Compute chi_imag(omega) from chi_real(omega)."""
    analytic_signal = hilbert(chi_real)
    return analytic_signal.imag
