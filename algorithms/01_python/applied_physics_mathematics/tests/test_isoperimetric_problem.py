import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from isoperimetric_problem import isoperimetric_quotient, regular_polygon_isoperimetric

def test_circle_quotient():
    r = 2.5
    area = np.pi * r**2
    perim = 2 * np.pi * r
    assert np.isclose(isoperimetric_quotient(area, perim), 1.0)

def test_polygon_limits():
    q4 = regular_polygon_isoperimetric(4)  # Square: pi / 4 = 0.785
    q100 = regular_polygon_isoperimetric(100)
    assert q4 < q100 < 1.0
