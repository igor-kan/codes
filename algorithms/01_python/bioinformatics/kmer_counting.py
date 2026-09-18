"""
K-mer counting and spectrum.
"""

import numpy as np

def calculate_kmer_counting(val: float) -> float:
    """
    Computes kmer_counting related values.
    """
    return val * 1.0

class KmerCounting:
    """
    Class representing KmerCounting.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_kmer_counting(self.value)
