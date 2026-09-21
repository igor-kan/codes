"""
Synchrotron Radiation Critical Photon Energy.
References: Kenneth S. Krane - Modern Physics.
"""
import numpy as np

def synchrotron_critical_photon_energy(E_beam_GeV: float, B_Tesla: float) -> float:
    """Critical photon energy epsilon_c [keV] = 0.665 * E^2 [GeV] * B [Tesla]."""
    return float(0.665 * (E_beam_GeV**2) * B_Tesla)
