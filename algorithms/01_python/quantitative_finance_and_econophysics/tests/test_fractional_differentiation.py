import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fractional_differentiation import fractional_differentiation_ffd

def test_integer_diff():
    # d = 1 should match regular first difference x_t - x_{t-1}
    x = np.array([1.0, 3.0, 6.0, 10.0, 15.0])
    diff1 = fractional_differentiation_ffd(x, d=1.0)
    expected = np.diff(x)
    assert np.allclose(diff1, expected)
