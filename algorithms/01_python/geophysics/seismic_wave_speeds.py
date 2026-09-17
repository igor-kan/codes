"""Seismic body wave velocities and elastic moduli."""

from typing import Tuple
import numpy as np


class SeismicWaveSpeeds:
    """Calculates P-wave and S-wave velocities, Poisson's ratio, and elastic moduli."""

    @classmethod
    def velocities(cls, bulk_modulus_k: float, shear_modulus_mu: float, density_rho: float) -> Tuple[float, float]:
        """v_p = sqrt((K + (4/3)*mu) / rho)
        v_s = sqrt(mu / rho)
        """
        vp = np.sqrt((bulk_modulus_k + (4.0 / 3.0) * shear_modulus_mu) / density_rho)
        vs = np.sqrt(shear_modulus_mu / density_rho)
        return float(vp), float(vs)

    @classmethod
    def poissons_ratio(cls, vp: float, vs: float) -> float:
        """nu = ( (vp/vs)^2 - 2 ) / ( 2 * (vp/vs)^2 - 2 ).
        For Poisson solid (vp/vs = sqrt(3)), nu = 0.25.
        """
        gamma2 = (vp / vs) ** 2
        return float((gamma2 - 2.0) / (2.0 * gamma2 - 2.0))
