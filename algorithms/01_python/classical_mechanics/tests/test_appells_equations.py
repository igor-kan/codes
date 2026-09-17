"""Unit tests for Appell's Equations."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from appells_equations import AppellsMechanics


class TestAppellsEquations(unittest.TestCase):
    def test_appell_acceleration(self):
        acc = AppellsMechanics.appell_equations_particle(mass=2.5, applied_force=10.0)
        self.assertAlmostEqual(acc, 4.0)


if __name__ == "__main__":
    unittest.main()
