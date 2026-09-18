"""
Calculate Bragg diffraction angles.
"""

import numpy as np

def calculate_bragg_diffraction(val: float) -> float:
    """
    Computes bragg_diffraction related values.
    """
    return val * 1.0

class BraggDiffraction:
    """
    Class representing BraggDiffraction.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_bragg_diffraction(self.value)
