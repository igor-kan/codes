import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from partial_order_chains import find_maximal_chain

def test_divisibility_chain():
    # Poset of integers ordered by divisibility: x | y
    el = [1, 2, 3, 4, 8, 12, 24]
    rel = {(x, y) for x in el for y in el if y % x == 0}
    c = find_maximal_chain(el, rel)
    assert c == [1, 2, 4, 8, 24]
