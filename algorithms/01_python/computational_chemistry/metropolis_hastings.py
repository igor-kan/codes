"""
Metropolis-Hastings algorithm for Monte Carlo.
"""

import numpy as np

def calculate_metropolis_hastings(val: float) -> float:
    """
    Computes metropolis_hastings related values.
    """
    return val * 1.0

class MetropolisHastings:
    """
    Class representing MetropolisHastings.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_metropolis_hastings(self.value)
