"""Roche Lobe Geometry in binary star systems."""

import numpy as np


class RocheLobe:
    """Analytical approximation of the Roche lobe effective radius."""

    @classmethod
    def eggleton_radius_ratio(cls, mass_ratio_q: float) -> float:
        """P. P. Eggleton (1983) formula for effective Roche lobe radius r_L / a:
        r_L / a = 0.49 * q^(2/3) / [0.6 * q^(2/3) + ln(1 + q^(1/3))]
        where q = M_1 / M_2.
        """
        q = float(mass_ratio_q)
        q23 = q ** (2.0 / 3.0)
        q13 = q ** (1.0 / 3.0)
        numerator = 0.49 * q23
        denominator = 0.6 * q23 + np.log(1.0 + q13)
        return float(numerator / denominator)

    @classmethod
    def effective_radius(cls, semi_major_axis: float, m1: float, m2: float) -> float:
        """Returns the physical Roche lobe radius in meters."""
        q = m1 / m2
        return semi_major_axis * cls.eggleton_radius_ratio(q)
