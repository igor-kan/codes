"""Photon Polarization Sum and Ward Identity.

Completeness relation for real transverse photons:
sum_(lambda=1,2) eps_mu(k, lambda) eps_nu*(k, lambda) = -eta_munu - (k_mu k_nu - k_mu nbar_nu - ...)
In physical gauges, the contraction with physical current J satisfies k^mu J_mu = 0 (Ward Identity).
"""
import numpy as np
from feynman_slash import ETA


def photon_polarization_sum_feynman_gauge() -> np.ndarray:
    """Feynman gauge effective polarization sum: -eta_munu."""
    return -ETA


def check_ward_identity(current: np.ndarray, photon_k: np.ndarray) -> bool:
    """Verify Ward identity k_mu * J^mu = 0."""
    divergence = np.dot(photon_k, ETA @ current)
    return np.isclose(divergence, 0.0, atol=1e-10)
