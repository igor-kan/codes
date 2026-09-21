import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from zermelo_well_ordering import well_order_by_choice

def test_well_order():
    res = well_order_by_choice({5, 1, 9, 2})
    assert res == [1, 2, 5, 9]
