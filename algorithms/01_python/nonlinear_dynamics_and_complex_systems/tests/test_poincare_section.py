import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poincare_section import find_poincare_intersections

def test_poincare_crossing():
    traj = np.array([[-1.0, 5.0], [1.0, 7.0]])
    pts = find_poincare_intersections(traj, plane_coord_idx=0, plane_val=0.0)
    assert len(pts) == 1
    assert np.isclose(pts[0, 0], 0.0)
    assert np.isclose(pts[0, 1], 6.0)
