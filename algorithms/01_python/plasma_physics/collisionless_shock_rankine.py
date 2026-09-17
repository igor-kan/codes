"""Collisionless Magnetized Shock Jump Relations and Alfven Mach Number.

Calculates density compression ratio across perpendicular collisionless plasma shocks.
"""

import numpy as np


class CollisionlessShock:
    """Perpendicular magnetized shock jump conditions."""

    @staticmethod
    def max_compression_ratio(polytropic_gamma: float = 5.0 / 3.0) -> float:
        """Maximum density compression for strong shock: r_max = (gamma + 1) / (gamma - 1)."""
        return float((polytropic_gamma + 1.0) / (polytropic_gamma - 1.0))
