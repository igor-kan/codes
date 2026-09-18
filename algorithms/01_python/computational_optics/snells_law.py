"""
Snell's law of refraction.
"""

import numpy as np

def calculate_snells_law(val: float) -> float:
    """
    Computes snells_law related values.
    """
    return val * 1.0

class SnellsLaw:
    """
    Class representing SnellsLaw.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_snells_law(self.value)
