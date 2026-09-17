"""Continental 1D Steady-State Conductive Geotherm."""

import numpy as np


class ContinentalGeotherm:
    """Calculates steady-state crustal temperature with radiogenic heat production:
    T(z) = T_0 + (q_0 * z / k) - (A * z^2 / (2 * k))
    """

    @classmethod
    def temperature(
        cls,
        depth_z: float,
        surface_temp_t0: float = 0.0,
        surface_heat_flow_q0: float = 0.065,
        thermal_conductivity_k: float = 2.5,
        heat_production_a: float = 1e-6,
    ) -> float:
        """T(z) in degrees Celsius."""
        term1 = (surface_heat_flow_q0 * depth_z) / thermal_conductivity_k
        term2 = (heat_production_a * (depth_z**2)) / (2.0 * thermal_conductivity_k)
        return float(surface_temp_t0 + term1 - term2)
