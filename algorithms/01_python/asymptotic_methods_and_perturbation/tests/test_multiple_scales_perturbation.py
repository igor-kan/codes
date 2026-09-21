import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from multiple_scales_perturbation import multiple_scales_damped_envelope

def test_envelope_decay():
    t = np.linspace(0, 10, 50)
    env = multiple_scales_damped_envelope(t, eps=0.1, x0=1.0)
    assert env[-1] < env[0]
