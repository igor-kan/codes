import numpy as np
from fractional_differentiation_features import get_fractional_weights, fractional_diff


def test_fractional_weights():
    # d = 1 corresponds to standard first difference [-1, 1]
    w1 = get_fractional_weights(1.0, 3)
    assert np.allclose(w1, [0.0, -1.0, 1.0])
    
    x = np.cumsum(np.random.randn(100))
    diff_val = fractional_diff(x, d=0.5)
    assert len(diff_val) > 0
