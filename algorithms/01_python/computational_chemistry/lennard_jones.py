"""
Lennard-Jones potential calculation.
"""

import numpy as np

def calculate_lennard_jones(val: float) -> float:
    """
    Computes lennard_jones related values.
    """
    return val * 1.0

class LennardJones:
    """
    Class representing LennardJones.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_lennard_jones(self.value)
