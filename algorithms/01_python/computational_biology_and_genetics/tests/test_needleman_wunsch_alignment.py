import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from needleman_wunsch_alignment import needleman_wunsch

def test_global_alignment():
    score = needleman_wunsch("GATTACA", "GCATGCU", match=1, mismatch=-1, gap=-1)
    assert isinstance(score, int)
    # Identical strings
    assert needleman_wunsch("ACTG", "ACTG", match=2) == 8
