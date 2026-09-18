"""
Entropy rate of a Markov source.
"""

import numpy as np

def calculate_markov_source(val: float) -> float:
    """
    Computes markov_source related values.
    """
    return val * 1.0

class MarkovSource:
    """
    Class representing MarkovSource.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_markov_source(self.value)
