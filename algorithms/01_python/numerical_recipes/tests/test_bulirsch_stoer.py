import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bulirsch_stoer import bulirsch_stoer_step

def test_exponential_decay():
    # dy/dt = -y -> y(t) = exp(-t)
    derivs = lambda t, y: -y
    y0 = np.array([1.0])
    H = 0.5
    y_bs = bulirsch_stoer_step(derivs, y0, 0.0, H)
    assert np.isclose(y_bs[0], np.exp(-H), atol=1e-8)
