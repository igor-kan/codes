import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tsiolkovsky_multistage import multistage_delta_v

def test_two_stage_rocket():
    ve = [3000.0, 4000.0]
    mr = [np.e, np.e]
    # Total dv = 3000*1 + 4000*1 = 7000 m/s
    dv = multistage_delta_v(ve, mr)
    assert np.isclose(dv, 7000.0)
