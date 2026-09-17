"""Magnetic Mirroring, Adiabatic Invariant mu, and Loss Cone Angle.

Calculates magnetic moment mu = 1/2 m v_perp^2 / B and loss cone sin(alpha_loss) = sqrt(B_min / B_max).
"""

import numpy as np


class MagneticMirror:
    """Magnetic bottle confinement and mirror reflection."""

    @staticmethod
    def magnetic_moment(mass: float, v_perp: float, b_mag: float) -> float:
        """mu = 1/2 m v_perp^2 / B (first adiabatic invariant)."""
        return float(0.5 * mass * (v_perp**2) / b_mag)

    @staticmethod
    def loss_cone_angle_radians(b_min: float, b_max: float) -> float:
        """alpha_loss = arcsin(sqrt(B_min / B_max))."""
        mirror_ratio = b_max / b_min
        if mirror_ratio < 1.0:
            raise ValueError("B_max must be >= B_min")
        return float(np.arcsin(np.sqrt(1.0 / mirror_ratio)))
