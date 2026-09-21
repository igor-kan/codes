import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bateman_decay_chains import bateman_activity_chain

def test_single_decay():
    half_life = 10.0
    N = bateman_activity_chain(t=10.0, half_lives=[half_life], n0=100.0)
    assert np.isclose(N[0], 50.0)
