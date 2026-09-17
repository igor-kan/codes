"""Normal forms for 1D Bifurcations: Saddle-Node, Transcritical, Pitchfork."""

from typing import List
import numpy as np


class BifurcationNormalForms:
    """Fixed points and stability for codimension-1 bifurcations."""

    @classmethod
    def saddle_node_fixed_points(cls, r: float) -> List[float]:
        """dx/dt = r + x^2. Real fixed points exist for r <= 0."""
        if r > 0:
            return []
        sqrt_r = np.sqrt(-r)
        return [-sqrt_r, sqrt_r]

    @classmethod
    def transcritical_fixed_points(cls, r: float) -> List[float]:
        """dx/dt = r * x - x^2. Fixed points at x = 0 and x = r."""
        return [0.0, float(r)]

    @classmethod
    def supercritical_pitchfork_fixed_points(cls, r: float) -> List[float]:
        """dx/dt = r * x - x^3.
        For r <= 0: x = 0 (stable)
        For r > 0: x = 0 (unstable), x = +-sqrt(r) (stable).
        """
        if r <= 0:
            return [0.0]
        sqrt_r = np.sqrt(r)
        return [0.0, float(-sqrt_r), float(sqrt_r)]
