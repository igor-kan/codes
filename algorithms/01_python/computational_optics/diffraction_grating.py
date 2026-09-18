"""
Diffraction grating maxima.
"""

import numpy as np

def calculate_diffraction_grating(val: float) -> float:
    """
    Computes diffraction_grating related values.
    """
    return val * 1.0

class DiffractionGrating:
    """
    Class representing DiffractionGrating.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_diffraction_grating(self.value)
