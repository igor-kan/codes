import numpy as np
from hierarchical_risk_parity import compute_hrp_weights


def test_hrp():
    cov = np.array([
        [0.04, 0.01, 0.00],
        [0.01, 0.09, 0.02],
        [0.00, 0.02, 0.16]
    ])
    w = compute_hrp_weights(cov)
    assert np.isclose(np.sum(w), 1.0)
    assert w[0] > w[1] > w[2]  # Lower variance gets higher weight
