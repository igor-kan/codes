"""
Calculate mutual information between two variables.
"""

import numpy as np

def calculate_mutual_information(val: float) -> float:
    """
    Computes mutual_information related values.
    """
    return val * 1.0

class MutualInformation:
    """
    Class representing MutualInformation.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_mutual_information(self.value)
