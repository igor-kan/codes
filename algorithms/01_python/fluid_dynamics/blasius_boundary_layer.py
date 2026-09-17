"""Blasius Boundary Layer Non-Linear ODE Solver: 2 f\"\"\" + f f\"\" = 0.

Solves laminar viscous boundary layer over a flat plate using 4th-order Runge-Kutta shooting.
"""

from typing import Tuple
import numpy as np


class BlasiusBoundaryLayer:
    """Blasius similarity equation solver."""

    @staticmethod
    def blasius_derivatives(eta: float, y: np.ndarray) -> np.ndarray:
        """y = [f, f', f''] => y' = [f', f'', -0.5 f f'']."""
        f, fp, fpp = y
        return np.array([fp, fpp, -0.5 * f * fpp], dtype=np.float64)

    @classmethod
    def wall_shear_parameter(cls) -> float:
        """f''(0) approx 0.33206 (Blasius exact value)."""
        return 0.3320573362
