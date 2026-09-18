"""
Rotating calipers for bounding box and diameter.
"""

import numpy as np

def calculate_rotating_calipers(val: float) -> float:
    """
    Computes rotating_calipers related values.
    """
    return val * 1.0

class RotatingCalipers:
    """
    Class representing RotatingCalipers.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_rotating_calipers(self.value)
