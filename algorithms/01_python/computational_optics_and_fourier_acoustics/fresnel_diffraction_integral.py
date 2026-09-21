"""Fresnel Diffraction via Angular Spectrum / Transfer Function FFT Method.

U(x, y, z) = IFFT2[ FFT2[U_0(x, y)] * H(fx, fy; z) ]
where H(fx, fy; z) = exp(i * k * z) * exp(-i * pi * lambda * z * (fx^2 + fy^2)).
"""
import numpy as np


def fresnel_propagate_1d(u0: np.ndarray, dx: float, wavelength: float, z: float) -> np.ndarray:
    """Propagate 1D optical field u0 across distance z."""
    n = len(u0)
    k = 2.0 * np.pi / wavelength
    fx = np.fft.fftfreq(n, d=dx)
    
    # Fresnel quadratic phase transfer function
    H = np.exp(1j * k * z) * np.exp(-1j * np.pi * wavelength * z * (fx**2))
    u_f = np.fft.fft(u0)
    return np.fft.ifft(u_f * H)
