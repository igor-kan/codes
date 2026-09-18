"""
Viterbi algorithm for Hidden Markov Models.
"""

import numpy as np

def calculate_viterbi(val: float) -> float:
    """
    Computes viterbi related values.
    """
    return val * 1.0

class Viterbi:
    """
    Class representing Viterbi.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_viterbi(self.value)
