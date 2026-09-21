import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bragg_stopping_power import bethe_bloch_stopping_power

def test_stopping_power_increases_as_particle_slows():
    # Bragg peak: as particle slows down (lower beta), stopping power rises
    dE_fast = bethe_bloch_stopping_power(beta=0.8)
    dE_slow = bethe_bloch_stopping_power(beta=0.2)
    assert dE_slow > dE_fast
