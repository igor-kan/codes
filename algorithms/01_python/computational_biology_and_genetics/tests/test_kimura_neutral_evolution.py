import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kimura_neutral_evolution import neutral_heterozygosity, neutral_substitution_rate

def test_kimura_theory():
    h = neutral_heterozygosity(N_e=1e4, mu=1e-5)
    # theta = 4 * 1e4 * 1e-5 = 0.4 -> H = 0.4 / 1.4 approx 0.2857
    assert np.isclose(h, 0.4 / 1.4)
    assert neutral_substitution_rate(1e-8) == 1e-8
