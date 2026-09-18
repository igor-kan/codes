"""
Solve geodesic equations for massive and massless particles.
"""

import numpy as np

def calculate_geodesic_equation(val: float) -> float:
    """
    Computes geodesic_equation related values.
    """
    return val * 1.0

class GeodesicEquation:
    """
    Class representing GeodesicEquation.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_geodesic_equation(self.value)
