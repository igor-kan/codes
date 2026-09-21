import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pedigree_linkage_analysis import lod_score

def test_tight_linkage():
    # 0 recombinants out of 20 offspring with theta = 0.05
    z = lod_score(0, 20, theta=0.05)
    # L(0.05) / L(0.5) = (0.95)^20 / (0.5)^20 = (1.9)^20 approx 375819 -> log10 approx 5.57
    assert z > 5.0
