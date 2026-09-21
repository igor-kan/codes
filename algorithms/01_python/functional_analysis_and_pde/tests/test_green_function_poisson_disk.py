import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from green_function_poisson_disk import greens_function_unit_disk

def test_boundary_zero():
    # On the boundary r=1, Green's function must vanish
    theta = 0.7
    xb, yb = np.cos(theta), np.sin(theta)
    g = greens_function_unit_disk(xb, yb, 0.3, 0.2)
    assert np.isclose(g, 0.0, atol=1e-10)
