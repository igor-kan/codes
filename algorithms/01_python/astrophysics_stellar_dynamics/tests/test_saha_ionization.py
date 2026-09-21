import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from saha_ionization import saha_ionization_ratio

def test_saha_high_temp():
    # High temperature drastically increases ionization ratio
    r_cool = saha_ionization_ratio(T=5000.0, Pe=20.0, chi_eV=13.6)
    r_hot = saha_ionization_ratio(T=20000.0, Pe=20.0, chi_eV=13.6)
    assert r_hot > r_cool * 1e4
