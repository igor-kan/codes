"""Poincare Surface of Section for Non-Integrable Hamiltonian Systems.

Computes discrete intersections with transverse hypersurface (e.g. Henon-Heiles potential: regular islands vs chaotic sea).
"""

from typing import Callable, Sequence, List, Tuple
import numpy as np


class PoincareSection:
    """Detects transverse crossings of a hyperplane (e.g. x = 0 with p_x > 0)."""

    @staticmethod
    def extract_crossings(trajectory_t: Sequence[float],
                          trajectory_z: Sequence[Sequence[float]],
                          cross_dim: int = 0, cross_val: float = 0.0) -> List[np.ndarray]:
        """Finds interpolated state vectors z where z[cross_dim] crosses cross_val with positive derivative."""
        z_arr = np.array(trajectory_z, dtype=np.float64)
        n = len(z_arr)
        crossings = []

        for i in range(n - 1):
            z1 = z_arr[i]
            z2 = z_arr[i + 1]
            val1 = z1[cross_dim] - cross_val
            val2 = z2[cross_dim] - cross_val
            # Check for crossing with positive velocity
            if val1 <= 0.0 < val2:
                # Linear interpolation for crossing point
                frac = - val1 / (val2 - val1)
                z_cross = z1 + frac * (z2 - z1)
                crossings.append(z_cross)
        return crossings
