import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from birkhoff_normal_form import harmonic_action, birkhoff_frequency_shift

def test_action_positive():
    assert harmonic_action(1.0, 1.0) == 1.0
    assert birkhoff_frequency_shift(1.0) == 1.1
