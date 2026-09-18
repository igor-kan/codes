"""
Basic principles of hologram recording and reconstruction.
"""

import numpy as np

def calculate_holography(val: float) -> float:
    """
    Computes holography related values.
    """
    return val * 1.0

class Holography:
    """
    Class representing Holography.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_holography(self.value)
