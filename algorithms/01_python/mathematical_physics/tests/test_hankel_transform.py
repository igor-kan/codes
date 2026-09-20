import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hankel_transform import hankel_transform_0

def test_gaussian_hankel():
    # Hankel transform of exp(-a r^2) is 1/(2a) exp(-k^2 / 4a)
    a = 1.0
    k_vals = np.array([0.5, 1.0, 1.5])
    H = hankel_transform_0(lambda r: np.exp(-a * r**2), k_vals, r_max=10.0, n_points=500)
    expected = (1.0 / (2.0 * a)) * np.exp(-k_vals**2 / (4.0 * a))
    assert np.allclose(H, expected, atol=1e-3)
