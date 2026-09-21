"""Talbot Effect Near-Field Grating Self-Imaging.

Talbot distance: z_T = 2 * a^2 / lambda (for 1D grating of pitch a).
Integer Talbot planes at z = m * z_T replicate the original transmission mask.
Sub-harmonic fractional Talbot planes at z = (p/q) * z_T create frequency multiplication.
"""
import numpy as np


def talbot_distance(grating_period: float, wavelength: float) -> float:
    """Calculate fundamental Talbot length z_T = 2 * a^2 / lambda."""
    if wavelength <= 0 or grating_period <= 0:
        raise ValueError("Wavelength and period must be positive")
    return float(2.0 * (grating_period**2) / wavelength)


def fractional_talbot_distance(grating_period: float, wavelength: float, p: int, q: int) -> float:
    """Fractional Talbot distance z = (p/q) * z_T."""
    return float((p / q) * talbot_distance(grating_period, wavelength))
