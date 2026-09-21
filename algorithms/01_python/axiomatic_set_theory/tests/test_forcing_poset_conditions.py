import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from forcing_poset_conditions import are_cohen_conditions_compatible

def test_compatibility():
    p = {0: 1, 1: 0}
    q = {1: 0, 2: 1}
    r = {1: 1, 3: 0}
    assert are_cohen_conditions_compatible(p, q)
    assert not are_cohen_conditions_compatible(p, r)
