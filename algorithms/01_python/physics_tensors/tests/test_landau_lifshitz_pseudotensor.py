"""Unit tests for Landau-Lifshitz Pseudotensor."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from landau_lifshitz_pseudotensor import LandauLifshitzPseudotensor


class TestLandauLifshitzPseudotensor(unittest.TestCase):
    def test_flat_spacetime(self):
        eta = np.diag([-1.0, 1.0, 1.0, 1.0])
        self.assertTrue(LandauLifshitzPseudotensor.flat_spacetime_vanishes(eta))


if __name__ == "__main__":
    unittest.main()
