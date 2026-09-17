"""Unit tests for GW inspiral."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gravitational_wave_inspiral_waveform import GravitationalWaveInspiral


class TestGWInspiral(unittest.TestCase):
    def test_chirp_mass(self):
        m1 = 30.0 * 1.989e30
        m2 = 30.0 * 1.989e30
        mc = GravitationalWaveInspiral.chirp_mass(m1, m2)
        # For m1=m2=M, M_chirp = M / 2^(1/5) ~ 0.87055 * M
        self.assertAlmostEqual(mc / m1, 2.0**(-0.2), places=3)


if __name__ == "__main__":
    unittest.main()
