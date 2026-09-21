import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from hardy_weinberg_selection import next_generation_allele_frequency

def test_neutral_hardy_weinberg():
    # In absence of selection (w_AA = w_Aa = w_aa = 1), allele frequencies do not change
    p_next, mean_w = next_generation_allele_frequency(0.4, 1.0, 1.0, 1.0)
    assert np.isclose(p_next, 0.4)
    assert np.isclose(mean_w, 1.0)

def test_selection_against_recessive():
    # Lethal recessive allele a: w_aa = 0.0
    p_next, _ = next_generation_allele_frequency(0.5, 1.0, 1.0, 0.0)
    # p' = (0.25 + 0.25) / (0.25 + 0.5) = 0.5 / 0.75 = 2/3
    assert np.isclose(p_next, 2.0 / 3.0)
