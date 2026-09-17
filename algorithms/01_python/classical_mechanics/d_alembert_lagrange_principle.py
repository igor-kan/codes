"""D'Alembert's Principle of Virtual Work sum (F_i - m_i ddot{r}_i) . delta r_i = 0.

Eliminates workless constraint forces through projection onto the tangent space of virtual displacements.
"""

from typing import Sequence
import numpy as np


class DAlembertPrinciple:
    """Virtual displacements and constraint force elimination."""

    @staticmethod
    def virtual_work(applied_forces: Sequence[float], virtual_displacements: Sequence[float]) -> float:
        """delta W = sum F_i . delta r_i."""
        f = np.array(applied_forces, dtype=np.float64)
        dr = np.array(virtual_displacements, dtype=np.float64)
        return float(np.dot(f, dr))

    @staticmethod
    def verify_equilibrium(applied_forces: Sequence[float],
                           admissible_virtual_displacements: np.ndarray,
                           tol: float = 1e-6) -> bool:
        """In static equilibrium, delta W = 0 for all kinematically admissible virtual displacements."""
        for dr in admissible_virtual_displacements:
            if abs(DAlembertPrinciple.virtual_work(applied_forces, dr)) > tol:
                return False
        return True
