"""Timoshenko Beam vs. Classical Euler-Bernoulli Beam Deflection.

Includes both bending deflection and shear deflection:
w_Timoshenko = w_bending + w_shear.
For simply supported beam with midpoint point load P:
w_bending = P * L^3 / (48 * E * I)
w_shear = P * L / (4 * kappa * G * A)
where kappa is Timoshenko shear coefficient (5/6 for rectangular cross section).
"""
import numpy as np


def timoshenko_midspan_deflection(P: float, L: float, E: float, G: float,
                                  b: float, h: float, kappa: float = 5.0 / 6.0) -> tuple:
    """Calculate center deflection for simply supported beam under load P."""
    A = b * h
    I = b * (h**3) / 12.0
    w_euler = P * (L**3) / (48.0 * E * I)
    w_shear = P * L / (4.0 * kappa * G * A)
    w_total = w_euler + w_shear
    return float(w_euler), float(w_shear), float(w_total)
