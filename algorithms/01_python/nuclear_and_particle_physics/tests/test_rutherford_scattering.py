import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from rutherford_scattering import rutherford_impact_parameter

def test_impact_head_on():
    # theta = pi (head-on) -> b = 0
    b = rutherford_impact_parameter(np.pi, 2, 79, 5.0)
    assert np.isclose(b, 0.0, atol=1e-10)
