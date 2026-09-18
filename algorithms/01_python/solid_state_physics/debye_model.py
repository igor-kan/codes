"""
Debye model for specific heat.
"""

import numpy as np

def calculate_debye_model(val: float) -> float:
    """
    Computes debye_model related values.
    """
    return val * 1.0

class DebyeModel:
    """
    Class representing DebyeModel.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_debye_model(self.value)
