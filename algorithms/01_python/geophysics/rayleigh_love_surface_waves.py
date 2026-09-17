"""Rayleigh and Love Surface Wave dispersion and velocity relations."""

import numpy as np


class SurfaceWaves:
    """Rayleigh wave secular velocity equation in elastic halfspace."""

    @classmethod
    def rayleigh_wave_velocity(cls, vp: float, vs: float) -> float:
        """Approximation by Bergmann (1948) / Viktorov (1967):
        v_R / v_s approx (0.87 + 1.12 * nu) / (1 + nu).
        """
        gamma2 = (vp / vs) ** 2
        nu = (gamma2 - 2.0) / (2.0 * gamma2 - 2.0)
        vr_vs = (0.87 + 1.12 * nu) / (1.0 + nu)
        return float(vr_vs * vs)
