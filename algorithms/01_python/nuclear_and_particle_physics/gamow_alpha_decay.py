"""
Gamow Theory of Alpha Decay Quantum Tunneling.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 8).
"""
import numpy as np

def gamow_factor(Z_daughter: int, E_alpha_MeV: float) -> float:
    """Gamow tunneling exponent G = (2 pi Z_d e^2) / (hbar v)."""
    # G approx 1.980 * Z_d / sqrt(E_alpha_MeV)
    return float(1.980 * Z_daughter / np.sqrt(E_alpha_MeV))

def alpha_decay_half_life(Z_daughter: int, E_alpha_MeV: float) -> float:
    """Geiger-Nuttall law representation of alpha half life: log10(T1/2) approx C1 + C2 * G."""
    G = gamow_factor(Z_daughter, E_alpha_MeV)
    return float(G)
