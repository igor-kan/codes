"""
Michaelis-Menten Enzyme Kinetics and Lineweaver-Burk Transformation.
Reference: Campbell Biology (12th Ed.), Ch. 8 (An Introduction to Metabolism).
"""
import numpy as np
from typing import Tuple

def reaction_velocity(S: np.ndarray, V_max: float, K_m: float) -> np.ndarray:
    """v = V_max * [S] / (K_m + [S])."""
    return (V_max * S) / (K_m + S)

def lineweaver_burk_parameters(S: np.ndarray, v: np.ndarray) -> Tuple[float, float]:
    """
    Fits 1/v = (K_m / V_max) * (1/[S]) + (1 / V_max).
    Returns (V_max, K_m).
    """
    inv_S = 1.0 / S
    inv_v = 1.0 / v
    slope, intercept = np.polyfit(inv_S, inv_v, 1)
    V_max = 1.0 / intercept
    K_m = slope * V_max
    return float(V_max), float(K_m)
