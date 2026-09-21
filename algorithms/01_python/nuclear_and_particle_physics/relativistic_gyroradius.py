"""
Relativistic Particle Gyroradius in Magnetic Fields.
References: Halliday, Resnick, Krane - Physics (Vol. 2).
"""
import numpy as np

def relativistic_gyroradius(p_GeV: float, B_Tesla: float, charge_e: int = 1) -> float:
    """Gyroradius r = p / (q B): r [m] approx 3.3356 * p [GeV/c] / (charge * B [Tesla])."""
    return float(3.33564 * p_GeV / (charge_e * B_Tesla))
