import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from moran_process_population import moran_fixation_probability

def test_neutral_fixation():
    assert np.isclose(moran_fixation_probability(100, 1.0), 0.01)

def test_beneficial_mutant():
    p = moran_fixation_probability(100, 1.1)
    # Beneficial mutant fixation probability > 1/N
    assert p > 0.01
