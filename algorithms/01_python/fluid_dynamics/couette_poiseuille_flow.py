"""Exact Solutions for Plane Couette, Poiseuille, and Hagen-Poiseuille Pipe Flow.

Calculates parabolic velocity profiles u(r) = Delta P / (4 mu L) (R^2 - r^2) and volumetric flow rates.
"""

import numpy as np


class ExactLaminarFlows:
    """Exact Navier-Stokes solutions."""

    @staticmethod
    def plane_couette_velocity(y: float, channel_height_h: float, wall_velocity_u: float) -> float:
        """u(y) = U * (y / h)."""
        return wall_velocity_u * (y / channel_height_h)

    @staticmethod
    def hagen_poiseuille_velocity(r: float, pipe_radius_r: float, pressure_gradient: float, dynamic_viscosity: float) -> float:
        """u(r) = (dp/dx) / (4 mu) * (r^2 - R^2)."""
        return (pressure_gradient / (4.0 * dynamic_viscosity)) * (r**2 - pipe_radius_r**2)

    @staticmethod
    def hagen_poiseuille_volumetric_flow(pipe_radius_r: float, delta_p: float, pipe_length: float, dynamic_viscosity: float) -> float:
        """Q = pi R^4 Delta P / (8 mu L)."""
        return float(np.pi * (pipe_radius_r**4) * delta_p / (8.0 * dynamic_viscosity * pipe_length))
