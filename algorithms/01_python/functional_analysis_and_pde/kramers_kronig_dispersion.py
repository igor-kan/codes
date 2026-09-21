"""
Kramers-Kronig Dispersion Relations connecting real and imaginary parts of susceptibility.
Reference: Hassani, Mathematical Methods for Physics, Ch. 11; Jackson, Classical Electrodynamics.
"""
import numpy as np

def compute_real_chi_from_imag(omega: np.ndarray, imag_chi: np.ndarray) -> np.ndarray:
    """
    Re[chi(omega)] = (2 / pi) P.V. int_0^infty (s Im[chi(s)]) / (s^2 - omega^2) ds.
    Discrete approximation with pole exclusion.
    """
    n = len(omega)
    real_chi = np.zeros(n)
    d_omega = omega[1] - omega[0]
    
    for i, w in enumerate(omega):
        # Exclude pole at s = w
        mask = np.abs(omega - w) > (d_omega * 0.5)
        s = omega[mask]
        im_s = imag_chi[mask]
        integrand = (2.0 / np.pi) * (s * im_s) / (s**2 - w**2)
        real_chi[i] = np.trapz(integrand, s)
    return real_chi
