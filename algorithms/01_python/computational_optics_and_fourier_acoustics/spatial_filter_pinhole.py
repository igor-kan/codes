"""Fourier 4f Spatial Filtering System.

Simulates low-pass pinhole spatial filtering to clear high-frequency noise and speckle:
U_out(x, y) = IFFT2[ FFT2[U_in] * H_pinhole(fx, fy) ].
Pinhole diameter d_pinhole = 2 * 1.22 * lambda * f / D_beam.
"""
import numpy as np


def optimum_pinhole_diameter(wavelength: float, focal_length: float, beam_waist: float) -> float:
    """Optimum spatial filter pinhole diameter (Airy disk first zero)."""
    return float(2.0 * 1.22 * wavelength * focal_length / (2.0 * beam_waist))


def lowpass_spatial_filter_1d(u_in: np.ndarray, dx: float, cutoff_freq: float) -> np.ndarray:
    """Apply ideal low-pass filter in spatial frequency domain."""
    n = len(u_in)
    fx = np.fft.fftfreq(n, d=dx)
    H = (np.abs(fx) <= cutoff_freq).astype(float)
    u_f = np.fft.fft(u_in)
    return np.fft.ifft(u_f * H)
