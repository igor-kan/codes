import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dna_melting_temperature import marmur_doty_tm

def test_short_primer_tm():
    primer = "ATGCGATC"  # 8 bp: 4 AT, 4 GC -> 4*2 + 4*4 = 24 C
    assert marmur_doty_tm(primer) == 24.0
