"""Unit tests for seismic wave speeds."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from seismic_wave_speeds import SeismicWaveSpeeds


class TestSeismicSpeeds(unittest.TestCase):
    def test_poisson_solid(self):
        # K = (5/3)*mu -> vp/vs = sqrt(3) -> nu = 0.25
        mu = 3.0e10
        k = (5.0 / 3.0) * mu
        rho = 2700.0
        vp, vs = SeismicWaveSpeeds.velocities(k, mu, rho)
        self.assertAlmostEqual(vp / vs, np.sqrt(3.0), places=3)
        nu = SeismicWaveSpeeds.poissons_ratio(vp, vs)
        self.assertAlmostEqual(nu, 0.25, places=3)


if __name__ == "__main__":
    unittest.main()
