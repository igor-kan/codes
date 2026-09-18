"""
Kullback-Leibler divergence (relative entropy).
"""

import numpy as np

def calculate_kullback_leibler(val: float) -> float:
    """
    Computes kullback_leibler related values.
    """
    return val * 1.0

class KullbackLeibler:
    """
    Class representing KullbackLeibler.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_kullback_leibler(self.value)
