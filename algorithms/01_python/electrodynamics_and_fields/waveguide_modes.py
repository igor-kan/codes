"""
Rectangular Waveguide Cutoff Frequencies and Dispersion.
References: Arfken, Weber, Harris - Mathematical Methods for Physicists (Ch. 14).
"""
import numpy as np

def rectangular_waveguide_cutoff(m: int, n: int, a: float, b: float, c: float = 3e8) -> float:
    """Cutoff frequency f_c = (c / 2) sqrt((m/a)^2 + (n/b)^2)."""
    return float(0.5 * c * np.sqrt((m / a)**2 + (n / b)**2))

def waveguide_propagation_constant(f: float, f_c: float, c: float = 3e8) -> float:
    """Guide wavelength / propagation wavenumber beta = (2 pi / c) sqrt(f^2 - f_c^2)."""
    if f <= f_c:
        return 0.0
    return float((2.0 * np.pi / c) * np.sqrt(f**2 - f_c**2))
