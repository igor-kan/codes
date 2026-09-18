"""
Calculate bond angles and dihedrals.
"""

import numpy as np

def calculate_bond_angle(val: float) -> float:
    """
    Computes bond_angle related values.
    """
    return val * 1.0

class BondAngle:
    """
    Class representing BondAngle.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_bond_angle(self.value)
