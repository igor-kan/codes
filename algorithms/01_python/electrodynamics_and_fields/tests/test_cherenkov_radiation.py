import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cherenkov_radiation import cherenkov_angle, frank_tamm_power_density

def test_cherenkov_water():
    n_water = 1.33
    beta = 0.9
    theta = cherenkov_angle(beta, n_water)
    assert theta > 0.0
    # Below threshold beta = 0.7 < 1/1.33 = 0.75
    theta_sub = cherenkov_angle(0.7, n_water)
    assert theta_sub == 0.0
