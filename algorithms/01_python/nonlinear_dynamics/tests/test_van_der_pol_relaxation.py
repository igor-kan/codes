"""Unit tests for Van der Pol oscillator."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from van_der_pol_relaxation import VanDerPolOscillator


class TestVanDerPol(unittest.TestCase):
    def test_limit_cycle_amplitude(self):
        # For small mu, limit cycle radius in phase space is approx 2.0
        vdp = VanDerPolOscillator(mu=0.1)
        traj = vdp.integrate(np.array([2.0, 0.0]), dt=0.01, steps=2000)
        # Check that it stays close to amplitude 2
        max_x = np.max(traj[1000:, 0])
        self.assertAlmostEqual(max_x, 2.0, places=1)


if __name__ == "__main__":
    unittest.main()
