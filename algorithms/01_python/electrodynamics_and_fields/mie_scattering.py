"""
Mie Scattering Cross Sections for Dielectric Spheres.
References: Boas; Arfken.
"""
import numpy as np

def rayleigh_scattering_cross_section(radius: float, wavelength: float, n_index: float) -> float:
    """Rayleigh limit (radius << wavelength) scattering cross section: sigma ~ r^6 / lambda^4."""
    x = 2.0 * np.pi * radius / wavelength
    m = n_index
    factor = ((m**2 - 1.0) / (m**2 + 2.0))**2
    sigma_sca = (8.0 * np.pi / 3.0) * (radius**2) * (x**4) * factor
    return float(sigma_sca)
