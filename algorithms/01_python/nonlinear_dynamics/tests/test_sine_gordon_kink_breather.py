"""Unit tests for Sine-Gordon solitons."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sine_gordon_kink_breather import SineGordonSoliton


class TestSineGordon(unittest.TestCase):
    def test_kink_limits(self):
        x = np.array([-100.0, 0.0, 100.0])
        phi = SineGordonSoliton.kink(x, t=0.0, v=0.0)
        # At -infinity phi -> 0, at center phi -> pi, at +infinity phi -> 2*pi
        self.assertAlmostEqual(phi[0], 0.0, places=3)
        self.assertAlmostEqual(phi[1], np.pi, places=3)
        self.assertAlmostEqual(phi[2], 2.0 * np.pi, places=3)


if __name__ == "__main__":
    unittest.main()
