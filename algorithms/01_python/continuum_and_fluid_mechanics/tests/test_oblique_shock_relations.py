import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from oblique_shock_relations import normal_shock_mach_downstream, normal_shock_pressure_ratio

def test_shock_jump():
    M1 = 2.0
    M2 = normal_shock_mach_downstream(M1)
    # Downstream of normal shock is subsonic
    assert M2 < 1.0
    pr = normal_shock_pressure_ratio(M1)
    # Pressure increases across shock
    assert pr > 1.0
