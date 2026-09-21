import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from smith_waterman_alignment import smith_waterman

def test_local_match():
    s1 = "AAAGGGTTT"
    s2 = "CCCGGGAAA"
    # Exact match of "GGG" gives 3 * 2 = 6
    score = smith_waterman(s1, s2, match=2, mismatch=-1, gap=-1)
    assert score == 6
