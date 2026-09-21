import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from duffing_oscillator_bistability import duffing_derivatives

def test_duffing():
    dx, dv = duffing_derivatives(1.0, 0.0, 0.0, delta=0.2, alpha=-1.0, beta=1.0, gamma=0.3, omega=1.2)
    assert dx == 0.0
    assert dv != 0.0
