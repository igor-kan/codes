import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hierarchical_risk_parity import inverse_variance_weights

def test_inv_var_weights():
    cov = np.diag([1.0, 4.0])
    w = inverse_variance_weights(cov)
    # w1 / w2 = 4 -> w = [0.8, 0.2]
    assert np.allclose(w, [0.8, 0.2])
