import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pulsar_dispersion import dispersion_delay

def test_dispersion():
    delay = dispersion_delay(1400.0, 1000.0, DM_pc_cm3=10.0)
    # Higher frequency arrives earlier -> negative delay from f1 to f2
    assert delay < 0.0
