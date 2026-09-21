import os, sys, numpy as np
from scipy.special import gamma
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mellin_transform_evaluation import mellin_transform_quad

def test_mellin_exponential():
    # Mellin transform of e^{-x} is Gamma(s)
    f = lambda x: np.exp(-x)
    s = 2.0 + 0.0j
    res = mellin_transform_quad(f, s, x_min=1e-5, x_max=30.0, n_points=5000)
    expected = gamma(2.0)  # 1.0
    assert np.isclose(res.real, expected, rtol=1e-2)
