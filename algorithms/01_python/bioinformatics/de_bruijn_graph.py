"""
De Bruijn graph for genome assembly.
"""

import numpy as np

def calculate_de_bruijn_graph(val: float) -> float:
    """
    Computes de_bruijn_graph related values.
    """
    return val * 1.0

class DeBruijnGraph:
    """
    Class representing DeBruijnGraph.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_de_bruijn_graph(self.value)
