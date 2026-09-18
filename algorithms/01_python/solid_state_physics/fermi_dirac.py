"""
Fermi-Dirac distribution.
"""

import numpy as np

def calculate_fermi_dirac(val: float) -> float:
    """
    Computes fermi_dirac related values.
    """
    return val * 1.0

class FermiDirac:
    """
    Class representing FermiDirac.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_fermi_dirac(self.value)
