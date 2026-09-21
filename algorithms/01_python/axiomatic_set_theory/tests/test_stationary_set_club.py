import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stationary_set_club import is_unbounded

def test_unbounded():
    assert is_unbounded({1, 5, 99}, 100)
    assert not is_unbounded({1, 5, 10}, 100)
