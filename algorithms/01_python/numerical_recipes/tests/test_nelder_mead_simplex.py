import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from nelder_mead_simplex import nelder_mead

def test_rosenbrock_optimization():
    # Rosenbrock banana function: f(x, y) = (1-x)^2 + 100(y-x^2)^2, minimum at (1, 1)
    rosen = lambda x: (1.0 - x[0])**2 + 100.0 * (x[1] - x[0]**2)**2
    min_pt = nelder_mead(rosen, [-1.2, 1.0], max_iter=1000)
    assert np.allclose(min_pt, [1.0, 1.0], atol=1e-3)
