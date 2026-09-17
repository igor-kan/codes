"""Unit tests for focal mechanism."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from focal_mechanism_beachball import FocalMechanism


class TestFocalMechanism(unittest.TestCase):
    def test_orthogonality(self):
        # Fault normal and slip vector must be strictly orthogonal (n . u = 0)
        n, u = FocalMechanism.fault_normal_and_slip(strike_deg=45.0, dip_deg=60.0, rake_deg=-30.0)
        self.assertAlmostEqual(np.dot(n, u), 0.0, places=6)


if __name__ == "__main__":
    unittest.main()
