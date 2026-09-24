"""Boltzmann H-Theorem and Non-Equilibrium Entropy Production."""
import numpy as np


def boltzmann_h_function(f: np.ndarray, v: np.ndarray) -> float:
    """H = int f(v) * ln(f(v)) dv."""
    dv = v[1] - v[0]
    pos = f > 1e-15
    return float(np.sum(f[pos] * np.log(f[pos])) * dv)
