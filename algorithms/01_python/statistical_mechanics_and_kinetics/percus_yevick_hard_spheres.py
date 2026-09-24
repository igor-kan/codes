"""Percus-Yevick Integral Equation for Hard Sphere Fluid Compressibility."""
def percus_yevick_compressibility_factor(eta: float) -> float:
    """Z = (1 + eta + eta^2) / (1 - eta)^3."""
    if eta >= 1.0 or eta < 0:
        raise ValueError("Packing fraction eta must be in [0, 1)")
    return float((1.0 + eta + eta**2) / (1.0 - eta)**3)
