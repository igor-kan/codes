"""Van der Waals Fluid Equation of State and Maxwell Equal-Area Construction."""
def vdw_pressure(V: float, T: float, a: float = 1.0, b: float = 0.05, R: float = 8.314) -> float:
    """P = R * T / (V - b) - a / V^2."""
    if V <= b:
        raise ValueError("Molar volume must exceed covolume b")
    return float(R * T / (V - b) - a / (V**2))
