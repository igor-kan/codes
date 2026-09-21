import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from van_dyke_matching_principle import verify_matching_constant

def test_matching():
    assert verify_matching_constant(2.71828, 2.71828)
