"""Unit tests for gravity anomalies."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gravitational_bouguer_anomaly import GravityAnomalies


class TestGravity(unittest.TestCase):
    def test_corrections(self):
        fa = GravityAnomalies.free_air_correction(100.0)
        self.assertAlmostEqual(fa, 30.86, places=2)
        bp = GravityAnomalies.bouguer_plate_correction(100.0, rho=2670.0)
        self.assertAlmostEqual(bp, 11.19, places=1)


if __name__ == "__main__":
    unittest.main()
