import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lie_derivative import lie_bracket_vector_fields

def test_rotation_generators():
    # Vector fields: X = (-y, x, 0), Y = (0, -z, y)
    # [X, Y] = X(Y) - Y(X) = (-z, 0, x)
    X = lambda r: np.array([-r[1], r[0], 0.0])
    Y = lambda r: np.array([0.0, -r[2], r[1]])
    pt = np.array([1.0, 2.0, 3.0])
    bracket = lie_bracket_vector_fields(X, Y, pt)
    # For pt = (1, 2, 3), (-z, 0, x) = (-3, 0, 1)
    assert np.allclose(bracket, [-3.0, 0.0, 1.0], atol=1e-4)
