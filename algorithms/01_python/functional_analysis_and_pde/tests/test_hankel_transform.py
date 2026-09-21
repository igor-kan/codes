import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hankel_transform import hankel_transform_order0

def test_hankel_gaussian():
    # H_0[exp(-a r^2)] = (1 / 2a) exp(-k^2 / 4a)
    a = 1.0
    f = lambda r: np.exp(-a * r**2)
    k_vals = np.array([0.0, 1.0])
    res = hankel_transform_order0(f, k_vals, r_max=10.0, n_pts=1500)
    expected = (1.0 / (2.0 * a)) * np.exp(-k_vals**2 / (4.0 * a))
    assert np.allclose(res, expected, rtol=1e-2)
