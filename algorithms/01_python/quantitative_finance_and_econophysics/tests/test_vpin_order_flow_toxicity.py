import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vpin_order_flow_toxicity import compute_vpin

def test_vpin_balanced():
    buys = np.array([50.0, 50.0, 50.0])
    sells = np.array([50.0, 50.0, 50.0])
    vpin = compute_vpin(buys, sells, bucket_volume=100.0)
    assert np.isclose(vpin, 0.0)
