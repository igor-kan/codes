"""Unit tests for Wigner Function."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from wigner_quasiprobability import WignerFunction


class TestWignerFunction(unittest.TestCase):
    def test_harmonic_ground_state_wigner_origin(self):
        val = WignerFunction.evaluate_1d([], [], x=0.0, p=0.0)
        self.assertAlmostEqual(val, 1.0 / np.pi)


if __name__ == "__main__":
    unittest.main()
