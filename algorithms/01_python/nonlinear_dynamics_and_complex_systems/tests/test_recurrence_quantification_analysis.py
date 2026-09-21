import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from recurrence_quantification_analysis import recurrence_rate

def test_rqa_rr():
    pts = np.array([[0.0], [0.0], [10.0]])
    rr = recurrence_rate(pts, threshold=1.0)
    # Self-recurrences (3) + pair (0, 1) and (1, 0) = 5 / 9
    assert np.isclose(rr, 5.0 / 9.0)
