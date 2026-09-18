"""
Z-transform evaluation.
"""

import numpy as np

def calculate_z_transform(val: float) -> float:
    """
    Computes z_transform related values.
    """
    return val * 1.0

class ZTransform:
    """
    Class representing ZTransform.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_z_transform(self.value)
