import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from codon_usage_bias import compute_rscu

def test_rscu():
    # Phenylalanine: UUU, UUC
    fam = {"TTT": "Phe", "TTC": "Phe"}
    seq = "TTTTTTTTT"  # 3x TTT, 0x TTC
    rscu = compute_rscu(seq, fam)
    assert rscu["TTT"] == 2.0
    assert rscu["TTC"] == 0.0
