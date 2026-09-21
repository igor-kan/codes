"""Gordon Decomposition of the Relativistic Electromagnetic Current.

Decomposes the Dirac current into convective and spin-magnetic components:
bar(u)(p') gamma^mu u(p) = bar(u)(p') [ (p' + p)^mu / (2m) + i sigma^(mu,nu) (p' - p)_nu / (2m) ] u(p).
"""
import numpy as np
from dirac_matrices import get_dirac_pauli_matrices, ETA

_GAMMAS = get_dirac_pauli_matrices()
_G_MU = [_GAMMAS["g0"], _GAMMAS["g1"], _GAMMAS["g2"], _GAMMAS["g3"]]


def sigma_tensor(mu: int, nu: int) -> np.ndarray:
    """Compute sigma^(mu,nu) = (i/2) * [gamma^mu, gamma^nu]."""
    comm = _G_MU[mu] @ _G_MU[nu] - _G_MU[nu] @ _G_MU[mu]
    return 0.5j * comm


def convective_term(p_prime: np.ndarray, p: np.ndarray, m: float, mu: int) -> float:
    """(p' + p)^mu / (2m)."""
    return float((p_prime[mu] + p[mu]) / (2.0 * m))


def spin_magnetic_operator(p_prime: np.ndarray, p: np.ndarray, m: float, mu: int) -> np.ndarray:
    """i * sigma^(mu,nu) * (p' - p)_nu / (2m)."""
    q = p_prime - p
    q_lower = ETA @ q
    op = np.zeros((4, 4), dtype=complex)
    for nu in range(4):
        op += 1j * sigma_tensor(mu, nu) * q_lower[nu] / (2.0 * m)
    return op
