"""Single-Particle Guiding Center Drifts (E x B, Grad-B, and Curvature Drifts).

Calculates drift velocity vectors in non-uniform electromagnetic fields.
"""

from typing import Sequence
import numpy as np


class GuidingCenterDrifts:
    """Guiding center velocity components."""

    @staticmethod
    def exb_drift(e_field: Sequence[float], b_field: Sequence[float]) -> np.ndarray:
        """v_E = (E x B) / B^2 (independent of charge and mass)."""
        e = np.array(e_field, dtype=np.float64)
        b = np.array(b_field, dtype=np.float64)
        b2 = float(np.dot(b, b))
        if b2 < 1e-15:
            raise ValueError("Magnetic field cannot be zero")
        return np.cross(e, b) / b2

    @staticmethod
    def grad_b_drift(b_field: Sequence[float], grad_b_mag: Sequence[float],
                     v_perp: float, charge: float, mass: float) -> np.ndarray:
        """v_{grad B} = 1/2 m v_perp^2 / (q B^3) * (B x grad |B|)."""
        b = np.array(b_field, dtype=np.float64)
        gb = np.array(grad_b_mag, dtype=np.float64)
        b_mag = float(np.linalg.norm(b))
        factor = 0.5 * mass * (v_perp**2) / (charge * (b_mag**3))
        return factor * np.cross(b, gb)
