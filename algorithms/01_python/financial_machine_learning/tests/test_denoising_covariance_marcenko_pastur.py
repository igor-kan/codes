import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from denoising_covariance_marcenko_pastur import marcenko_pastur_bounds

def test_mp_bounds():
    l_min, l_max = marcenko_pastur_bounds(var=1.0, q=4.0)
    # (1 - 1/2)^2 = 0.25, (1 + 1/2)^2 = 2.25
    assert np.isclose(l_min, 0.25)
    assert np.isclose(l_max, 2.25)
