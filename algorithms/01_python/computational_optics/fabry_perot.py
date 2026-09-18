"""
Fabry-Perot interferometer transmission.
"""

import numpy as np

def calculate_fabry_perot(val: float) -> float:
    """
    Computes fabry_perot related values.
    """
    return val * 1.0

class FabryPerot:
    """
    Class representing FabryPerot.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_fabry_perot(self.value)
