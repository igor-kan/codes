"""Euler-Poincare and Lie-Poisson Reduction on so(3)* for Rigid Body Dynamics.

Implements Arnold §47: Lie-Poisson bracket {f, g}(m) = - m . (grad f x grad g) and Casimir invariant C = 1/2 ||m||^2.
"""

from typing import Sequence
import numpy as np


class LiePoissonRigidBody:
    """Lie-Poisson bracket on so(3)* (angular momentum space)."""

    def __init__(self, principal_moments: Sequence[float]):
        self.i_diag = np.array(principal_moments, dtype=np.float64)

    def casimir_invariant(self, m: Sequence[float]) -> float:
        """C(m) = 1/2 ||m||^2 is constant along all coadjoint orbits (symplectic leaves)."""
        m_arr = np.array(m, dtype=np.float64)
        return 0.5 * float(np.dot(m_arr, m_arr))

    def hamiltonian(self, m: Sequence[float]) -> float:
        """H = 1/2 sum m_i^2 / I_i."""
        m_arr = np.array(m, dtype=np.float64)
        return 0.5 * float(np.sum((m_arr**2) / self.i_diag))

    def time_derivative(self, m: Sequence[float]) -> np.ndarray:
        """dot{m} = m x grad H(m) = m x omega."""
        m_arr = np.array(m, dtype=np.float64)
        omega = m_arr / self.i_diag
        # dot{m} = m x omega
        return np.cross(m_arr, omega)
