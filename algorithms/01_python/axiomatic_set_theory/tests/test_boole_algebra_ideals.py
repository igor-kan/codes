import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from boole_algebra_ideals import is_ideal

def test_trivial_ideal():
    X = frozenset([1, 2, 3])
    # Trivial ideal contains only empty set
    assert is_ideal({frozenset()}, X)
