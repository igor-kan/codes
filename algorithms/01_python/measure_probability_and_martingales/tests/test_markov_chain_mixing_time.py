import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from markov_chain_mixing_time import total_variation_distance, compute_mixing_time

def test_mixing_two_state():
    # Symmetric 2-state chain with transition prob 0.2
    P = np.array([[0.8, 0.2], [0.2, 0.8]])
    pi = np.array([0.5, 0.5])
    tmix = compute_mixing_time(P, pi, epsilon=0.1)
    assert tmix > 0
