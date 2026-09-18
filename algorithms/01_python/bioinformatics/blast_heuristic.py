"""
Basic Local Alignment Search Tool heuristic.
"""

import numpy as np

def calculate_blast_heuristic(val: float) -> float:
    """
    Computes blast_heuristic related values.
    """
    return val * 1.0

class BlastHeuristic:
    """
    Class representing BlastHeuristic.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_blast_heuristic(self.value)
