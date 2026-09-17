"""Snell's Law and Seismic Refraction Surveying."""

from typing import Tuple
import numpy as np


class SeismicRefraction:
    """Calculates critical angle, head wave travel times, and crossover distance."""

    @classmethod
    def critical_angle(cls, v1: float, v2: float) -> float:
        """theta_c = arcsin(v1 / v2) for v2 > v1."""
        if v1 >= v2:
            raise ValueError("Refraction requires v2 > v1.")
        return float(np.arcsin(v1 / v2))

    @classmethod
    def head_wave_travel_time(cls, offset_x: float, layer_thickness_h: float, v1: float, v2: float) -> float:
        """t(x) = x / v2 + (2 * h * cos(theta_c)) / v1."""
        theta_c = cls.critical_angle(v1, v2)
        t_intercept = (2.0 * layer_thickness_h * np.cos(theta_c)) / v1
        return float(offset_x / v2 + t_intercept)

    @classmethod
    def crossover_distance(cls, layer_thickness_h: float, v1: float, v2: float) -> float:
        """Distance where direct wave (x/v1) and refracted wave cross over:
        x_cross = 2 * h * sqrt((v2 + v1) / (v2 - v1)).
        """
        return float(2.0 * layer_thickness_h * np.sqrt((v2 + v1) / (v2 - v1)))
