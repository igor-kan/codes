import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cofinality_calculator import is_regular_aleph_0, cofinality_aleph_omega

def test_cardinal_regularity():
    assert is_regular_aleph_0()
    assert cofinality_aleph_omega() == "omega"
