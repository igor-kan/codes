import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from supersonic_rankine_hugoniot import normal_shock_relations

def test_sonic_limit():
    res = normal_shock_relations(1.0)
    assert np.isclose(res["p2_over_p1"], 1.0)
    assert np.isclose(res["mach2"], 1.0)

def test_strong_shock():
    res = normal_shock_relations(3.0, gamma=1.4)
    assert res["p2_over_p1"] > 10.0
    assert res["mach2"] < 1.0
