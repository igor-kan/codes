"""
Thin lens equation and magnification.
"""

import numpy as np

def calculate_thin_lens(val: float) -> float:
    """
    Computes thin_lens related values.
    """
    return val * 1.0

class ThinLens:
    """
    Class representing ThinLens.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_thin_lens(self.value)
