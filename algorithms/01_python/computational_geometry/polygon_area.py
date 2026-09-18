"""
Shoelace formula for polygon area.
"""

import numpy as np

def calculate_polygon_area(val: float) -> float:
    """
    Computes polygon_area related values.
    """
    return val * 1.0

class PolygonArea:
    """
    Class representing PolygonArea.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_polygon_area(self.value)
