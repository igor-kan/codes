import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from arnold_cat_map import arnold_cat_map, cat_map_lyapunov_exponent

def test_cat_map_origin():
    assert arnold_cat_map(0.0, 0.0, n_steps=5) == (0.0, 0.0)

def test_lyapunov_exponent():
    l = cat_map_lyapunov_exponent()
    assert np.isclose(l, 0.96242365)
