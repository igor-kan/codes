import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stochastic_resonance import bistable_stochastic_step

def test_bistable_step():
    np.random.seed(42)
    x = 1.0
    x_next = bistable_stochastic_step(x, A=0.1, omega=1.0, t=0.0, D=0.05, dt=0.01)
    assert np.isfinite(x_next)
