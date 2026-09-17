"""Unit tests for Two-Stream Instability."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from two_stream_instability import TwoStreamInstability


class TestTwoStream(unittest.TestCase):
    def test_growth_rate_value(self):
        gamma = TwoStreamInstability.max_growth_rate(beam_plasma_frequency=1e6)
        expected = (np.sqrt(3.0) / (2.0**(4.0 / 3.0))) * 1e6
        self.assertAlmostEqual(gamma, expected)


if __name__ == "__main__":
    unittest.main()
