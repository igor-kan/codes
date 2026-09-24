"""Morse Potential for Diatomic Molecule Vibrational States.

V(r) = D_e * (1 - exp(-a * (r - r_e)))^2.
Eigenvalues: E_v = hbar * omega_0 * (v + 1/2) - (hbar * omega_0 * (v + 1/2))^2 / (4 * D_e).
"""
import numpy as np


def morse_potential(r: np.ndarray, D_e: float, a: float, r_e: float) -> np.ndarray:
    """Evaluate Morse potential energy curve."""
    return D_e * (1.0 - np.exp(-a * (r - r_e)))**2


def morse_energy_level(v: int, omega0: float, D_e: float, hbar: float = 1.0) -> float:
    """Calculate discrete bound state energy for vibrational quantum number v >= 0."""
    v_half = v + 0.5
    linear = hbar * omega0 * v_half
    anharmonic = (linear**2) / (4.0 * D_e)
    E = linear - anharmonic
    if E >= D_e:
        raise ValueError("State is in ionization continuum")
    return float(E)
