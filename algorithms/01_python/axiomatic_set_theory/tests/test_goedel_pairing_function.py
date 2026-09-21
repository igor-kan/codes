import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from goedel_pairing_function import goedel_pair, goedel_unpair

def test_pairing_bijection():
    pairs = [(0, 0), (1, 0), (0, 1), (3, 5), (100, 250)]
    for x, y in pairs:
        z = goedel_pair(x, y)
        rx, ry = goedel_unpair(z)
        assert (rx, ry) == (x, y)
