"""
Four-Momentum and Invariant Mass Computation.
References: Halliday, Resnick, Krane - Physics (Vol. 2).
"""
import numpy as np

def invariant_mass(four_momenta: list) -> float:
    """Calculate invariant mass M = sqrt(E_tot^2 - p_tot^2) from list of four-momenta [E, px, py, pz]."""
    tot = np.sum(four_momenta, axis=0)
    E = tot[0]
    p_sq = np.sum(tot[1:]**2)
    s = E**2 - p_sq
    return float(np.sqrt(max(0.0, s)))
