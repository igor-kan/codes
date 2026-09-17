"""Airy-Heiskanen and Pratt-Hayford Isostasy Models."""

from typing import Tuple


class IsostasyModels:
    """Calculates isostatic crustal compensation for topography."""

    @classmethod
    def airy_root_thickness(
        cls, topography_h: float, crust_density_rho_c: float = 2700.0, mantle_density_rho_m: float = 3300.0
    ) -> float:
        """Airy isostatic root depth:
        r = h * rho_c / (rho_m - rho_c).
        """
        return float(topography_h * crust_density_rho_c / (mantle_density_rho_m - crust_density_rho_c))

    @classmethod
    def pratt_density(
        cls, topography_h: float, compensation_depth_d: float, standard_density_rho_0: float = 2700.0
    ) -> float:
        """Pratt isostatic column density:
        rho * (D + h) = rho_0 * D  =>  rho = rho_0 * D / (D + h).
        """
        return float(standard_density_rho_0 * compensation_depth_d / (compensation_depth_d + topography_h))
