"""
Archimedes Principle and Metacentric Height for Floating Body Stability.
Reference: Polya, Mathematical Methods in Science.
"""
import numpy as np

def metacentric_height(I_waterline: float, V_displaced: float, BG: float) -> float:
    """
    Metacentric height GM = BM - BG = (I / V) - BG.
    Body is stable if GM > 0.
    """
    BM = I_waterline / V_displaced
    GM = BM - BG
    return float(GM)

def is_floating_stable(I_waterline: float, V_displaced: float, BG: float) -> bool:
    return metacentric_height(I_waterline, V_displaced, BG) > 0.0
