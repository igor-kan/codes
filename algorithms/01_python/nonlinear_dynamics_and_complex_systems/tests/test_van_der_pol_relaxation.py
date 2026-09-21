import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from van_der_pol_relaxation import van_der_pol_derivatives

def test_vdp():
    dx, dy = van_der_pol_derivatives(0.0, 1.0, mu=1.0)
    assert dx == 1.0
    assert dy == 1.0
