import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blasius_boundary_layer import blasius_shooting

def test_blasius_asymptote():
    eta, y = blasius_shooting()
    # At eta = 8, f'(eta) = y[1] should reach 1.0
    f_prime_inf = y[1, -1]
    assert np.isclose(f_prime_inf, 1.0, atol=1e-2)
