import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from magnetic_monopole_dirac import dirac_quantization_condition

def test_dirac_monopole_charge():
    g1 = dirac_quantization_condition(1, 1.0)
    assert np.isclose(g1, 0.5)
