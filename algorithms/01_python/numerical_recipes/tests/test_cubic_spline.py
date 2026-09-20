import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cubic_spline import CubicSpline

def test_cubic_spline_exact():
    # Spline interpolates nodes exactly
    x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])
    y = np.sin(x)
    spline = CubicSpline(x, y)
    assert np.allclose(spline.evaluate(x), y, atol=1e-12)
