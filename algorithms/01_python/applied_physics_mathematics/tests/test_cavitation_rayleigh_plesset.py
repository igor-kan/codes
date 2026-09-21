import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cavitation_rayleigh_plesset import bubble_radial_acceleration

def test_bubble_collapse():
    # If P_inf >> P_bubble, acceleration is strongly negative (collapse)
    acc = bubble_radial_acceleration(R=0.001, R_dot=0.0, P_bubble=1e3, P_inf=1e5, rho=1000.0)
    assert acc < 0.0
