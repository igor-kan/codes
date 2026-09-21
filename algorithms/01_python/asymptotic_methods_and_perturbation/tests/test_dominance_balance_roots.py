import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dominance_balance_roots import dominant_balance_cubic

def test_dominant_balance():
    eps = 1e-4
    r_reg, im1, im2 = dominant_balance_cubic(eps)
    assert np.isclose(r_reg, 1.0, atol=1e-3)
    assert np.isclose(im1, 100.0)
