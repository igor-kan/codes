"""
Calculate density of states for free electron gas.
"""

import numpy as np

def calculate_density_of_states(val: float) -> float:
    """
    Computes density_of_states related values.
    """
    return val * 1.0

class DensityOfStates:
    """
    Class representing DensityOfStates.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_density_of_states(self.value)
