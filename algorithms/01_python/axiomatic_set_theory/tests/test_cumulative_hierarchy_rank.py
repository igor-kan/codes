import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cumulative_hierarchy_rank import rank_of_nested_tuple

def test_rank():
    assert rank_of_nested_tuple(()) == 0
    assert rank_of_nested_tuple(((),)) == 1
    assert rank_of_nested_tuple((((),),)) == 2
