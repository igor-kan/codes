import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from matched_asymptotic_expansions import composite_boundary_layer_solution

def test_boundary_values():
    eps = 0.05
    x = np.array([0.0, 1.0])
    y = composite_boundary_layer_solution(x, eps)
    assert np.isclose(y[0], 0.0)
    assert np.isclose(y[1], 1.0, atol=1e-3)
