"""
Calculate gravitational and cosmological redshift.
"""

import numpy as np

def calculate_redshift(val: float) -> float:
    """
    Computes redshift related values.
    """
    return val * 1.0

class Redshift:
    """
    Class representing Redshift.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_redshift(self.value)
