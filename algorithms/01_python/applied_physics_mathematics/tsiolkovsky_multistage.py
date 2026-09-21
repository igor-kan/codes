"""
Multi-stage Tsiolkovsky Rocket Equation and Stage Optimization.
Reference: Zeldovich, Higher Mathematics for Beginners, Ch. 1.
"""
import numpy as np
from typing import List

def multistage_delta_v(stage_exhaust_velocities: List[float],
                       stage_mass_ratios: List[float]) -> float:
    """
    Computes total delta V = sum_i v_{e, i} ln(m_{0, i} / m_{f, i}).
    """
    total_dv = 0.0
    for ve, mr in zip(stage_exhaust_velocities, stage_mass_ratios):
        total_dv += ve * np.log(mr)
    return float(total_dv)
