import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from frank_kamenetskii_explosion import will_explode, frank_kamenetskii_critical_parameter

def test_explosion_criterion():
    assert will_explode(1.5, "slab")
    assert not will_explode(0.5, "slab")
    assert not will_explode(2.5, "sphere")
    assert will_explode(3.5, "sphere")
