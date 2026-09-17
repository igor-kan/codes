"""Sweet-Parker Steady 2D Magnetic Reconnection Model.

Calculates reconnection inflow velocity v_in = v_A / sqrt(S) with Lundquist number S = mu_0 L v_A / eta.
"""

import numpy as np


class SweetParkerReconnection:
    """Sweet-Parker resistive MHD reconnection."""

    @staticmethod
    def lundquist_number(length_l: float, alfven_speed: float, magnetic_diffusivity_eta: float) -> float:
        """S = L * v_A / eta."""
        return float(length_l * alfven_speed / magnetic_diffusivity_eta)

    @classmethod
    def reconnection_rate(cls, length_l: float, alfven_speed: float, magnetic_diffusivity_eta: float) -> float:
        """Reconnection inflow Mach number: M_in = v_in / v_A = 1 / sqrt(S)."""
        s = cls.lundquist_number(length_l, alfven_speed, magnetic_diffusivity_eta)
        return float(1.0 / np.sqrt(s))
