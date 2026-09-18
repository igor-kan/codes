"""
Quantum harmonic oscillator energy levels.
"""

import numpy as np

def calculate_harmonic_oscillator(val: float) -> float:
    """
    Computes harmonic_oscillator related values.
    """
    return val * 1.0

class HarmonicOscillator:
    """
    Class representing HarmonicOscillator.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_harmonic_oscillator(self.value)
