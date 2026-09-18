"""
Morse potential calculation.
"""

import numpy as np

def calculate_morse_potential(val: float) -> float:
    """
    Computes morse_potential related values.
    """
    return val * 1.0

class MorsePotential:
    """
    Class representing MorsePotential.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_morse_potential(self.value)
