import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from synchrotron_radiation import critical_frequency, total_synchrotron_power

def test_synchrotron_scaling():
    wc1 = critical_frequency(gamma=10.0, B=1.0)
    wc2 = critical_frequency(gamma=20.0, B=1.0)
    # Scales as gamma^3 -> factor of 8
    assert np.isclose(wc2 / wc1, 8.0)
    
    p = total_synchrotron_power(gamma=10.0, B=1.0)
    assert p > 0.0
