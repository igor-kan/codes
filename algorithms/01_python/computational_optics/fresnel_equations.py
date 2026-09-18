"""
Fresnel reflection and transmission coefficients.
"""

import numpy as np

def calculate_fresnel_equations(val: float) -> float:
    """
    Computes fresnel_equations related values.
    """
    return val * 1.0

class FresnelEquations:
    """
    Class representing FresnelEquations.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_fresnel_equations(self.value)
