"""
Stellar Hydrostatic Equilibrium and Central Pressure Estimate.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 10).
"""
import numpy as np

def central_pressure_estimate(mass: float, radius: float, G: float = 6.6743e-11) -> float:
    """P_c approx G M^2 / R^4."""
    return float(G * (mass**2) / (radius**4))
