"""
Gravitational lensing lens equation solver.
"""

import numpy as np

def calculate_lens_equation(val: float) -> float:
    """
    Computes lens_equation related values.
    """
    return val * 1.0

class LensEquation:
    """
    Class representing LensEquation.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_lens_equation(self.value)
