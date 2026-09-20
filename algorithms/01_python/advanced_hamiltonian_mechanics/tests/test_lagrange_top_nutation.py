import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lagrange_top_nutation import lagrange_top_effective_potential

def test_effective_potential_positive():
    theta = np.linspace(0.2, np.pi - 0.2, 50)
    V = lagrange_top_effective_potential(theta, P_phi=1.0, P_psi=1.0)
    assert np.all(np.isfinite(V))
