"""Reynolds Transport Theorem for Deforming Material Volumes.

Relates material volume time derivatives to control volume surface fluxes.
"""

from typing import Sequence
import numpy as np


class ReynoldsTransport:
    """Evaluates control volume rate of change: D/Dt int rho phi dV = d/dt int rho phi dV + oint rho phi (v . n) dA."""

    @staticmethod
    def mass_flux_rate(density: float, normal_velocity: float, surface_area: float) -> float:
        """m_dot = rho * v_n * A."""
        return density * normal_velocity * surface_area
