import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fitzhugh_nagumo_neuron import step_fitzhugh_nagumo

def test_fhn_step():
    v, w = step_fitzhugh_nagumo(0.0, 0.0, 0.5)
    assert v > 0.0
