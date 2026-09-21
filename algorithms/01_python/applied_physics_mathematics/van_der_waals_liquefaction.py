"""
Van der Waals Isotherm and Maxwell Equal-Area Construction.
Reference: Zeldovich, Higher Mathematics for Beginners.
"""
import numpy as np

def vdw_pressure(v: np.ndarray, T: float, a: float = 3.59, b: float = 0.0427, R: float = 0.08206) -> np.ndarray:
    """
    P(v) = R T / (v - b) - a / v^2.
    """
    return (R * T) / (v - b) - a / (v**2)

def critical_constants(a: float = 3.59, b: float = 0.0427, R: float = 0.08206):
    """
    T_c = 8a / (27 R b)
    P_c = a / (27 b^2)
    v_c = 3b
    """
    T_c = (8.0 * a) / (27.0 * R * b)
    P_c = a / (27.0 * (b**2))
    v_c = 3.0 * b
    return T_c, P_c, v_c
