"""Collisionless Landau Damping Rate for Electrostatic Waves in Warm Plasmas.

Calculates wave-particle resonance damping gamma = - sqrt(pi/8) omega_pe / (k lambda_D)^3 exp(- 1/(2 k^2 lambda_D^2) - 3/2).
"""

import numpy as np


class LandauDamping:
    """Collisionless wave damping."""

    @staticmethod
    def damping_rate(k_wavenumber: float, debye_length: float, omega_pe: float) -> float:
        """Calculates decay rate gamma < 0."""
        kld = k_wavenumber * debye_length
        factor = - np.sqrt(np.pi / 8.0) * omega_pe / (kld**3)
        exponent = - 0.5 / (kld**2) - 1.5
        return float(factor * np.exp(exponent))
