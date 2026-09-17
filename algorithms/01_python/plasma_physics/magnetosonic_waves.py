"""Fast and Slow Magnetosonic Compressional MHD Waves.

Calculates v_{f,s}^2 = 1/2 [ (v_A^2 + c_s^2) +- sqrt((v_A^2 + c_s^2)^2 - 4 v_A^2 c_s^2 cos^2(theta)) ].
"""

from typing import Tuple
import numpy as np


class MagnetosonicWaves:
    """Compressible MHD wave modes."""

    @staticmethod
    def phase_speeds(alfven_speed: float, sound_speed: float, propagation_angle_theta: float) -> Tuple[float, float]:
        """Returns (v_fast, v_slow)."""
        va2 = alfven_speed**2
        cs2 = sound_speed**2
        sum_sq = va2 + cs2
        disc = np.sqrt(max(0.0, sum_sq**2 - 4.0 * va2 * cs2 * (np.cos(propagation_angle_theta)**2)))
        vf = np.sqrt(0.5 * (sum_sq + disc))
        vs = np.sqrt(0.5 * (sum_sq - disc))
        return float(vf), float(vs)
