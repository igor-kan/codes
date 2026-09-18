"""
Linearized gravity and gravitational wave propagation.
"""

import numpy as np

def calculate_gravitational_waves(val: float) -> float:
    """
    Computes gravitational_waves related values.
    """
    return val * 1.0

class GravitationalWaves:
    """
    Class representing GravitationalWaves.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_gravitational_waves(self.value)
