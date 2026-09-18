"""
Phonon dispersion relations for 1D chain.
"""

import numpy as np

def calculate_phonon_dispersion(val: float) -> float:
    """
    Computes phonon_dispersion related values.
    """
    return val * 1.0

class PhononDispersion:
    """
    Class representing PhononDispersion.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_phonon_dispersion(self.value)
