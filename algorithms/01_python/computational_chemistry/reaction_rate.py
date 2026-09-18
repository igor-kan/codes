"""
Arrhenius equation and Eyring equation for reaction rates.
"""

import numpy as np

def calculate_reaction_rate(val: float) -> float:
    """
    Computes reaction_rate related values.
    """
    return val * 1.0

class ReactionRate:
    """
    Class representing ReactionRate.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_reaction_rate(self.value)
