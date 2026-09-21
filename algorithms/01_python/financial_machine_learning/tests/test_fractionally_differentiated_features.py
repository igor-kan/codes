import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fractionally_differentiated_features import get_fractional_weights, fractional_diff

def test_frac_weights():
    w = get_fractional_weights(d=1.0, size=5)
    # For d=1, w = [1, -1, 0, 0, 0] (integer first difference)
    assert np.isclose(w[0], 1.0)
    assert np.isclose(w[1], -1.0)
    assert np.allclose(w[2:], 0.0)
