import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from borell_resummation_divergent import borel_transform_geometric

def test_borel():
    assert borel_transform_geometric(0.0) == 1.0
    assert borel_transform_geometric(1.0) == 0.5
