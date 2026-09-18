"""
Blahut-Arimoto algorithm for channel capacity.
"""

import numpy as np

def calculate_channel_capacity(val: float) -> float:
    """
    Computes channel_capacity related values.
    """
    return val * 1.0

class ChannelCapacity:
    """
    Class representing ChannelCapacity.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_channel_capacity(self.value)
