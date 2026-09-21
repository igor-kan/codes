import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from markov_cpg_island_detector import cpg_observed_to_expected_ratio

def test_cpg_ratio():
    seq = "CGCGCGCG"
    ratio = cpg_observed_to_expected_ratio(seq)
    # CG appears 4 times in 8 bp, C=4, G=4 -> (4 * 8) / (4 * 4) = 32 / 16 = 2.0
    assert np.isclose(ratio, 2.0)
