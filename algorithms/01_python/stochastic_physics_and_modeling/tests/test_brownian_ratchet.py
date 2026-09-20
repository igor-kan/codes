import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from brownian_ratchet import sawtooth_force

def test_sawtooth_force():
    f_steep = sawtooth_force(0.1, L=1.0, alpha=0.2, F0=1.0)
    f_gentle = sawtooth_force(0.5, L=1.0, alpha=0.2, F0=1.0)
    assert f_steep < 0.0
    assert f_gentle > 0.0
