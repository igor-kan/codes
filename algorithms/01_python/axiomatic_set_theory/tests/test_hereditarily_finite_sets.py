import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hereditarily_finite_sets import ackermann_encode, ackermann_decode

def test_ackermann_bijection():
    orig = {0, 2, 5}
    code = ackermann_encode(orig)
    assert code == 1 + 4 + 32  # 37
    assert ackermann_decode(code) == orig
