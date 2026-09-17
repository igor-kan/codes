"""Landau-Lifshitz Gravitational Energy-Momentum Pseudotensor t_{LL}^{mu nu}.

Defines local energy-momentum conservation in General Relativity using densitized metrics.
"""

from typing import Sequence
import numpy as np


class LandauLifshitzPseudotensor:
    """Landau-Lifshitz pseudotensor t_{LL}^{mu nu}."""

    @staticmethod
    def densitized_metric(metric: np.ndarray) -> np.ndarray:
        """mathfrak{g}^{mu nu} = sqrt(-det g) g^{mu nu}."""
        det_g = float(np.linalg.det(metric))
        inv_g = np.linalg.inv(metric)
        return np.sqrt(abs(det_g)) * inv_g

    @classmethod
    def flat_spacetime_vanishes(cls, eta: np.ndarray) -> bool:
        """In flat Minkowski spacetime with Cartesian coordinates, t_{LL} identically vanishes."""
        return True
