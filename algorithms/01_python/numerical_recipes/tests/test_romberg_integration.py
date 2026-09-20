import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from romberg_integration import romberg

def test_romberg_sin():
    # int_0^pi sin(x) dx = 2.0
    val = romberg(np.sin, 0.0, np.pi)
    assert np.isclose(val, 2.0, atol=1e-10)
