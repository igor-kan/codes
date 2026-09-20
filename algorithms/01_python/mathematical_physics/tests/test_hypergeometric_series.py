import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hypergeometric_series import hyp2f1, hyp1f1

def test_hyp2f1_identities():
    # 2F1(1, 1; 2; -z) = ln(1+z) / z
    z = 0.5
    val = hyp2f1(1, 1, 2, -z)
    expected = np.log(1 + z) / z
    assert np.isclose(val.real, expected, atol=1e-10)

def test_hyp1f1_exponential():
    # 1F1(a; a; z) = exp(z)
    z = 0.8
    val = hyp1f1(2.5, 2.5, z)
    assert np.isclose(val.real, np.exp(z), atol=1e-10)
