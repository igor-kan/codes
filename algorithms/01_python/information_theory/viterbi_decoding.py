"""
Viterbi decoding for convolutional codes.
"""

import numpy as np

def calculate_viterbi_decoding(val: float) -> float:
    """
    Computes viterbi_decoding related values.
    """
    return val * 1.0

class ViterbiDecoding:
    """
    Class representing ViterbiDecoding.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_viterbi_decoding(self.value)
