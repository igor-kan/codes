import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from transfer_matrix_tunneling import barrier_transmission

def test_barrier_limits():
    # As E >> V0, T -> 1
    T_high = barrier_transmission(E=100.0, V0=5.0, a=1.0)
    assert T_high > 0.99
    # For E < V0, T is exponentially suppressed
    T_tunnel = barrier_transmission(E=2.0, V0=10.0, a=2.0)
    assert 0.0 < T_tunnel < 0.05
