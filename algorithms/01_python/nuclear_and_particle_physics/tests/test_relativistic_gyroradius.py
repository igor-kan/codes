import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from relativistic_gyroradius import relativistic_gyroradius

def test_lhc_beam():
    # 7000 GeV proton in 8.33 Tesla dipole -> radius approx 2800 m
    r = relativistic_gyroradius(7000.0, 8.33)
    assert 2700 < r < 2900
