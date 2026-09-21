import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from radioactive_diffusion_cascade import steady_state_decay_diffusion

def test_diffusion_length():
    D = 1e-4
    lam = 1.0
    x = np.array([0.01])
    c = steady_state_decay_diffusion(x, D, lam, 100.0)
    assert np.isclose(c[0], 100.0 * np.exp(-1.0))
