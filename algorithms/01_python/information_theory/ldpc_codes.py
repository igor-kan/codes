"""
Low-density parity-check codes.
"""

import numpy as np

def calculate_ldpc_codes(val: float) -> float:
    """
    Computes ldpc_codes related values.
    """
    return val * 1.0

class LdpcCodes:
    """
    Class representing LdpcCodes.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_ldpc_codes(self.value)
