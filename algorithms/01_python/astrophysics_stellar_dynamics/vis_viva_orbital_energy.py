"""
Vis-Viva Equation and Specific Orbital Energy.
References: Carroll & Ostlie - An Introduction to Modern Astrophysics (Ch. 2).
"""
import numpy as np

def orbital_velocity(r: float, a: float, GM: float = 1.0) -> float:
    """Vis-viva: v^2 = GM (2/r - 1/a)."""
    return float(np.sqrt(GM * (2.0 / r - 1.0 / a)))
