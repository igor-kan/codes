"""Unit tests for Anharmonic Oscillators."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from anharmonic_oscillators import AnharmonicOscillator


class TestAnharmonicOscillators(unittest.TestCase):
    def test_duffing_quartic_hardening(self):
        # Pure quartic potential V = 1/2 w0^2 x^2 + 1/4 beta x^4 => beta > 0 increases frequency
        ao = AnharmonicOscillator(omega_0=1.0, beta=1.0)
        w_perturbed = ao.perturbed_frequency(amplitude=2.0)
        # Delta w = (3 * 1 / 8) * 4 = 1.5 => w = 2.5
        self.assertAlmostEqual(w_perturbed, 2.5)


if __name__ == "__main__":
    unittest.main()
