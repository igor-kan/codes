import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from semi_empirical_mass_formula import nuclear_binding_energy, binding_energy_per_nucleon

def test_fe56_binding():
    # Iron-56 peak binding energy per nucleon is approx 8.8 MeV
    b_per_a = binding_energy_per_nucleon(Z=26, A=56)
    assert 8.5 < b_per_a < 9.0
