"""
Einstein model for specific heat.
"""

import numpy as np

def calculate_einstein_model(val: float) -> float:
    """
    Computes einstein_model related values.
    """
    return val * 1.0

class EinsteinModel:
    """
    Class representing EinsteinModel.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_einstein_model(self.value)
