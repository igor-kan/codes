"""
Simple 1D tight-binding model.
"""

import numpy as np

def calculate_tight_binding(val: float) -> float:
    """
    Computes tight_binding related values.
    """
    return val * 1.0

class TightBinding:
    """
    Class representing TightBinding.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_tight_binding(self.value)
