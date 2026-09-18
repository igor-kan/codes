"""
Calculate Boltzmann distribution and partition function.
"""

import numpy as np

def calculate_boltzmann_distribution(val: float) -> float:
    """
    Computes boltzmann_distribution related values.
    """
    return val * 1.0

class BoltzmannDistribution:
    """
    Class representing BoltzmannDistribution.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_boltzmann_distribution(self.value)
