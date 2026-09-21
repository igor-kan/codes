import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ito_isometry_integration import ito_integral_euler

def test_ito_integral():
    # int_0^1 1 dW = W(1)
    time_grid = np.linspace(0.0, 1.0, 100)
    W_path = np.linspace(0.0, 0.75, 100)
    res = ito_integral_euler(lambda t: np.ones_like(t), W_path, time_grid)
    assert np.isclose(res, 0.75)
