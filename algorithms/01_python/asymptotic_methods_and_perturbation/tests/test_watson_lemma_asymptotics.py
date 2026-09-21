import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from watson_lemma_asymptotics import watson_leading_term

def test_watson():
    # int_0^inf e^{-s t} dt = 1/s (lambda=0, a0=1)
    val = watson_leading_term(0.0, 1.0, 10.0)
    assert np.isclose(val, 0.1)
