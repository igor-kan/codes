"""Unit tests for Plasma Frequency."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from plasma_frequency import PlasmaFrequency


class TestPlasmaFrequency(unittest.TestCase):
    def test_ionosphere_cutoff(self):
        # n_e = 1e12 m^-3 => f_pe approx 9 MHz
        w_pe = PlasmaFrequency.electron_plasma_frequency(1e12)
        f_pe = w_pe / (2.0 * 3.14159265)
        self.assertGreater(f_pe, 8e6)
        self.assertLess(f_pe, 10e6)
        # Below cutoff, dielectric constant is negative (reflects radio waves)
        eps = PlasmaFrequency.dielectric_permittivity(wave_omega=0.5 * w_pe, electron_density=1e12)
        self.assertLess(eps, 0.0)


if __name__ == "__main__":
    unittest.main()
