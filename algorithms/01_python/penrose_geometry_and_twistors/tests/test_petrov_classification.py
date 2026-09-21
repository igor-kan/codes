import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from petrov_classification import classify_petrov_type

def test_petrov_types():
    assert "Type I" in classify_petrov_type(np.array([1.0, 2.0, -3.0]))
    assert "Type D" in classify_petrov_type(np.array([2.0, 2.0, -4.0]))
    assert "Type O" in classify_petrov_type(np.array([0.0, 0.0, 0.0]))
