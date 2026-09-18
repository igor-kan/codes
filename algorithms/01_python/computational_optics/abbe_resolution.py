"""
Abbe resolution limit of a microscope.
"""

import numpy as np

def calculate_abbe_resolution(val: float) -> float:
    """
    Computes abbe_resolution related values.
    """
    return val * 1.0

class AbbeResolution:
    """
    Class representing AbbeResolution.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_abbe_resolution(self.value)
