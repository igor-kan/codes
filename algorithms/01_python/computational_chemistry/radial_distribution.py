"""
Calculate radial distribution function.
"""

import numpy as np

def calculate_radial_distribution(val: float) -> float:
    """
    Computes radial_distribution related values.
    """
    return val * 1.0

class RadialDistribution:
    """
    Class representing RadialDistribution.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_radial_distribution(self.value)
