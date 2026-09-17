"""Unit tests for FLRW Cosmological Metric."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from flrw_metric import FLRWMetric


class TestFLRWMetric(unittest.TestCase):
    def test_hubble_and_deceleration(self):
        flrw = FLRWMetric(k=0)
        h = flrw.hubble_parameter(a=2.0, a_dot=140.0)
        self.assertAlmostEqual(h, 70.0)
        q = flrw.deceleration_parameter(a=2.0, a_dot=140.0, a_ddot=-4900.0)
        self.assertAlmostEqual(q, 0.5)


if __name__ == "__main__":
    unittest.main()
