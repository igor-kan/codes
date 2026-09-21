"""Unit tests for Sedov blast wave."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sedov_blast_wave import SedovBlastWave


class TestSedovBlastWave(unittest.TestCase):
    def test_scaling(self):
        # Time increases by 32 = 2^5 -> radius increases by 2^2 = 4
        r1 = SedovBlastWave.shock_radius(1.0, 1e44, 1e-21)
        r2 = SedovBlastWave.shock_radius(32.0, 1e44, 1e-21)
        self.assertAlmostEqual(r2 / r1, 4.0, places=3)


if __name__ == "__main__":
    unittest.main()
