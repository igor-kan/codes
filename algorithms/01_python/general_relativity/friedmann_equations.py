"""
Solve Friedmann equations for cosmology.
"""

import numpy as np

def calculate_friedmann_equations(val: float) -> float:
    """
    Computes friedmann_equations related values.
    """
    return val * 1.0

class FriedmannEquations:
    """
    Class representing FriedmannEquations.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_friedmann_equations(self.value)
