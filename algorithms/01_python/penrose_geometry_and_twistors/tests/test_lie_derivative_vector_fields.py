import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lie_derivative_vector_fields import lie_bracket_numerical

def test_commuting_vector_fields():
    # Translation generators d/dx and d/dy commute: [X, Y] = 0
    X = lambda pt: np.array([1.0, 0.0])
    Y = lambda pt: np.array([0.0, 1.0])
    bracket = lie_bracket_numerical(X, Y, np.array([2.0, 3.0]))
    assert np.allclose(bracket, 0.0, atol=1e-5)

def test_rotation_generators():
    # Generator of rotation in xy-plane: X = (-y, x)
    # Generator of scaling: Y = (x, y) -> [X, Y] = 0
    X = lambda pt: np.array([-pt[1], pt[0]])
    Y = lambda pt: np.array([pt[0], pt[1]])
    bracket = lie_bracket_numerical(X, Y, np.array([1.0, 1.0]))
    assert np.allclose(bracket, 0.0, atol=1e-5)
