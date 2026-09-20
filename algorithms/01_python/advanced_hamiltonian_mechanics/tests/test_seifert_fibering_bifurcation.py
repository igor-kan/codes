import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from seifert_fibering_bifurcation import standard_twist_map

def test_fixed_point():
    # Origin is fixed point
    t1, r1 = standard_twist_map(0.0, 0.0)
    assert t1 == 0.0 and r1 == 0.0
