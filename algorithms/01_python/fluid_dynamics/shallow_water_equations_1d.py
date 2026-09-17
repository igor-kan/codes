"""1D Non-Linear Shallow Water Equations (Saint-Venant System).

Models free-surface gravity waves: d h / dt + d(h u)/dx = 0, d(hu)/dt + d(hu^2 + 1/2 g h^2)/dx = 0.
"""

from typing import Tuple
import numpy as np


class ShallowWater1D:
    """1D Saint-Venant shallow water solver."""

    G = 9.80665

    @classmethod
    def wave_speed(cls, water_depth_h: float) -> float:
        """Gravity wave celerity c = sqrt(g h)."""
        return float(np.sqrt(cls.G * water_depth_h))

    @classmethod
    def froude_number(cls, flow_velocity_u: float, water_depth_h: float) -> float:
        """Fr = u / sqrt(g h). Subcritical < 1, Supercritical > 1."""
        c = cls.wave_speed(water_depth_h)
        return float(abs(flow_velocity_u) / c)
