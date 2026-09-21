"""
Planck Blackbody Function, Wien's Law, and Stefan-Boltzmann Flux.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 3).
"""
import numpy as np

H_PLANCK = 6.62607015e-34
C_LIGHT = 2.99792458e8
K_BOLTZMANN = 1.380649e-23
SIGMA_SB = 5.670374419e-8
WIEN_B = 2.897771955e-3

def planck_spectral_radiance(wavelength: np.ndarray, T: float) -> np.ndarray:
    """Planck's law B_lambda(T) = (2 h c^2 / lambda^5) / (exp(h c / (lambda k T)) - 1)."""
    lam = np.asarray(wavelength, dtype=float)
    c1 = 2.0 * H_PLANCK * (C_LIGHT**2)
    c2 = H_PLANCK * C_LIGHT / (K_BOLTZMANN * T)
    exp_factor = np.exp(c2 / lam)
    return c1 / (lam**5 * (exp_factor - 1.0))

def wien_peak_wavelength(T: float) -> float:
    """Wien's displacement law: lambda_max = b / T."""
    return WIEN_B / T

def stefan_boltzmann_flux(T: float) -> float:
    """Stefan-Boltzmann total blackbody flux F = sigma * T^4."""
    return SIGMA_SB * (T**4)
