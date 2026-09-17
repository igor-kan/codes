"""Seismic Reflection and Normal Moveout (NMO) correction."""

import numpy as np


class SeismicReflectionNMO:
    """Hyperbolic reflection travel time and normal moveout correction:
    t^2(x) = t_0^2 + x^2 / v_rms^2.
    """

    @classmethod
    def travel_time(cls, offset_x: float, zero_offset_time_t0: float, v_rms: float) -> float:
        """t(x) = sqrt(t_0^2 + x^2 / v_rms^2)."""
        return float(np.sqrt(zero_offset_time_t0**2 + (offset_x**2) / (v_rms**2)))

    @classmethod
    def normal_moveout(cls, offset_x: float, zero_offset_time_t0: float, v_rms: float) -> float:
        """Delta t_NMO = t(x) - t_0."""
        return cls.travel_time(offset_x, zero_offset_time_t0, v_rms) - zero_offset_time_t0
