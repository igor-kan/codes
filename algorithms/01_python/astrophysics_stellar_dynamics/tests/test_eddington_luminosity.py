import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from eddington_luminosity import eddington_luminosity

def test_eddington():
    assert eddington_luminosity(1.0) == 1.26e31
