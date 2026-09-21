"""Casimir Operators of the Poincaré Lie Algebra.

1. Mass-squared invariant: P^2 = P_mu P^mu = M^2.
2. Pauli-Lubanski spin Casimir: W^2 = W_mu W^mu = -M^2 s (s + 1).
"""
import numpy as np
from feynman_slash import minkowski_dot


def mass_casimir(p: np.ndarray) -> float:
    """Evaluate mass invariant M^2 = p^mu p_mu."""
    return minkowski_dot(p, p)


def pauli_lubanski_spin_casimir(mass: float, spin: float) -> float:
    """Evaluate Pauli-Lubanski eigenvalue W^2 = -m^2 * s * (s + 1) for massive particles."""
    return - (mass**2) * spin * (spin + 1.0)
