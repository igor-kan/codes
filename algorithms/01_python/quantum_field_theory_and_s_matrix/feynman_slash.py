"""Feynman Slash Notation and Trace Theorems.

Calculates p_slash = gamma^mu * p_mu and evaluates exact Dirac traces.
"""
import numpy as np
from dirac_matrices import get_dirac_pauli_matrices, ETA

_GAMMAS = get_dirac_pauli_matrices()
_G_MU = [_GAMMAS["g0"], _GAMMAS["g1"], _GAMMAS["g2"], _GAMMAS["g3"]]


def feynman_slash(p: np.ndarray) -> np.ndarray:
    """Compute Feynman slash of 4-vector p (p^0, p^1, p^2, p^3).

    p_slash = gamma^0 p_0 + gamma^1 p_1 + gamma^2 p_2 + gamma^3 p_3
    with p_mu = eta_(mu,nu) p^nu -> p_0 = p^0, p_i = -p^i.
    """
    p_lower = ETA @ p
    slash = np.zeros((4, 4), dtype=complex)
    for mu in range(4):
        slash += _G_MU[mu] * p_lower[mu]
    return slash


def minkowski_dot(a: np.ndarray, b: np.ndarray) -> float:
    """Minkowski inner product a^mu b_mu = a^0 b^0 - a^1 b^1 - a^2 b^2 - a^3 b^3."""
    return float(np.dot(a, ETA @ b))


def trace_two_slashes(a: np.ndarray, b: np.ndarray) -> complex:
    """Evaluate Tr(slash(a) * slash(b)) = 4 * (a . b)."""
    slash_a = feynman_slash(a)
    slash_b = feynman_slash(b)
    return np.trace(slash_a @ slash_b)


def trace_four_slashes(a: np.ndarray, b: np.ndarray, c: np.ndarray, d: np.ndarray) -> complex:
    """Evaluate Tr(slash(a) * slash(b) * slash(c) * slash(d)).

    Analytical theorem: 4 * [(a.b)(c.d) - (a.c)(b.d) + (a.d)(b.c)].
    """
    sa = feynman_slash(a)
    sb = feynman_slash(b)
    sc = feynman_slash(c)
    sd = feynman_slash(d)
    return np.trace(sa @ sb @ sc @ sd)
