"""Unit tests for Guiding Center Drifts."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from guiding_center_drifts import GuidingCenterDrifts


class TestGuidingCenter(unittest.TestCase):
    def test_exb_orthogonal_direction(self):
        e = [0.0, 100.0, 0.0]
        b = [0.0, 0.0, 2.0]
        # v_E = (E_y * B_z) / B^2 = (100 * 2) / 4 = 50 in +x direction
        v_e = GuidingCenterDrifts.exb_drift(e, b)
        np.testing.assert_allclose(v_e, [50.0, 0.0, 0.0])


if __name__ == "__main__":
    unittest.main()
