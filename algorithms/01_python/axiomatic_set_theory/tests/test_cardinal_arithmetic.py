import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cardinal_arithmetic import Cardinal, cardinal_add

def test_infinite_addition():
    aleph0 = Cardinal(aleph_idx=0)
    aleph1 = Cardinal(aleph_idx=1)
    n = Cardinal(finite_val=42)
    assert cardinal_add(aleph0, n).aleph_idx == 0
    assert cardinal_add(aleph0, aleph1).aleph_idx == 1
