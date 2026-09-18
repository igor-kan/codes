"""
Stokes parameters for partially polarized light.
"""

import numpy as np

def calculate_stokes_parameters(val: float) -> float:
    """
    Computes stokes_parameters related values.
    """
    return val * 1.0

class StokesParameters:
    """
    Class representing StokesParameters.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_stokes_parameters(self.value)
