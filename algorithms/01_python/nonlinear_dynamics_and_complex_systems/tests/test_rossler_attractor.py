import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rossler_attractor import integrate_rossler

def test_rossler_shape():
    traj = integrate_rossler(500)
    assert traj.shape == (500, 3)
