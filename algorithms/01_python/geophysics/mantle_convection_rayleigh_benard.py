"""Rayleigh-Bénard Mantle Convection and Dimensionless Rayleigh Number."""

class MantleConvection:
    """Thermal convection criteria in planetary mantles."""

    CRITICAL_RAYLEIGH_FREE_FREE = 657.51  # (27/4) * pi^4 for free-free boundaries
    CRITICAL_RAYLEIGH_RIGID_RIGID = 1707.76 # for rigid-rigid boundaries

    @classmethod
    def rayleigh_number(
        cls,
        density_rho: float,
        gravity_g: float,
        thermal_expansion_alpha: float,
        delta_temp_k: float,
        layer_thickness_d: float,
        thermal_diffusivity_kappa: float,
        dynamic_viscosity_eta: float,
    ) -> float:
        """Ra = (rho * g * alpha * Delta T * d^3) / (kappa * eta)."""
        numerator = density_rho * gravity_g * thermal_expansion_alpha * delta_temp_k * (layer_thickness_d**3)
        denominator = thermal_diffusivity_kappa * dynamic_viscosity_eta
        return float(numerator / denominator)

    @classmethod
    def is_convecting(cls, ra: float, boundary_type: str = "rigid") -> bool:
        thresh = cls.CRITICAL_RAYLEIGH_RIGID_RIGID if boundary_type == "rigid" else cls.CRITICAL_RAYLEIGH_FREE_FREE
        return ra > thresh
