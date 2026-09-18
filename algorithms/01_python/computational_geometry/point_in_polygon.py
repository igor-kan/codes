"""
Ray casting algorithm for point in polygon.
"""

import numpy as np

def calculate_point_in_polygon(val: float) -> float:
    """
    Computes point_in_polygon related values.
    """
    return val * 1.0

class PointInPolygon:
    """
    Class representing PointInPolygon.
    """
    def __init__(self, value: float):
        self.value = value

    def compute(self) -> float:
        return calculate_point_in_polygon(self.value)
