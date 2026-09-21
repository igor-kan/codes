import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hierarchical_risk_parity import inverse_variance_weights

def test_inv_var():
    cov = np.diag([1.0, 4.0])
    w = inverse_variance_weights(cov)
    # 1/1 vs 1/4 -> 4:1 ratio -> [0.8, 0.2]
    assert np.allclose(w, [0.8, 0.2])
