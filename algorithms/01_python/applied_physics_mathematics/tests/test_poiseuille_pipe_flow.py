import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poiseuille_pipe_flow import velocity_profile, volumetric_flow_rate

def test_poiseuille():
    R = 0.01
    dp = 100.0
    L = 1.0
    eta = 0.001
    v = velocity_profile(np.array([0.0, R]), R, dp, L, eta)
    assert v[0] > 0.0 and np.isclose(v[1], 0.0)
    q = volumetric_flow_rate(R, dp, L, eta)
    assert q > 0.0
