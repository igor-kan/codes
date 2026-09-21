"""Temporal Coherence and Michelson Interferometer Fringe Visibility.

Fringe visibility: V(Delta_L) = (I_max - I_min) / (I_max + I_min) = |gamma(tau)|.
Wiener-Khinchin theorem: degree of temporal coherence is the Fourier transform
of the normalized optical power spectral density S(nu).
"""
import numpy as np


def gaussian_spectral_visibility(delta_path: float, coherence_length: float) -> float:
    """Visibility envelope for a Gaussian light spectrum with coherence length L_c."""
    return float(np.exp(- (np.pi * delta_path / (2.0 * coherence_length))**2))


def fringe_visibility_from_intensity(I_max: float, I_min: float) -> float:
    """Calculate visibility metric V = (I_max - I_min) / (I_max + I_min)."""
    return float((I_max - I_min) / (I_max + I_min))
