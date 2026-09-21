import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lane_emden_polytrope import lane_emden_solve

def test_lane_emden_n1():
    # For n=1, exact analytical solution is theta(xi) = sin(xi)/xi, zero at xi_1 = pi approx 3.14159
    xi, theta, xi_1 = lane_emden_solve(n=1.0, xi_max=5.0)
    assert np.isclose(xi_1, np.pi, atol=0.05)
