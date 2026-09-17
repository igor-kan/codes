"""Earthquake Seismic Moment and Moment Magnitude Scale (Mw)."""

import numpy as np


class MomentMagnitude:
    """Calculates seismic scalar moment M0 and Hanks-Kanamori moment magnitude Mw."""

    @classmethod
    def seismic_moment(cls, shear_modulus_mu: float, fault_area_m2: float, slip_m: float) -> float:
        """M_0 = mu * A * D [N * m]."""
        return float(shear_modulus_mu * fault_area_m2 * slip_m)

    @classmethod
    def moment_magnitude(cls, seismic_moment_nm: float) -> float:
        """M_w = (2/3) * log10(M_0) - 6.07 (using M_0 in N*m).
        Equivalent to (2/3) * (log10(M_0_dyne_cm) - 16.1) with M_0 [N*m] = 10^7 dyne*cm.
        """
        # log10(M0_dyne_cm) = log10(M0_nm) + 7
        # Mw = (2/3) * (log10(M0_nm) + 7 - 16.1) = (2/3) * (log10(M0_nm) - 9.1) = (2/3)*log10(M0_nm) - 6.0667
        return float((2.0 / 3.0) * np.log10(seismic_moment_nm) - 6.07)
