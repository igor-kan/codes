import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kovalevskaya_top import kovalevskaya_invariant

def test_kovalevskaya_non_negative():
    K = kovalevskaya_invariant(1.0, 0.5, 0.2, 0.1)
    assert K >= 0.0
