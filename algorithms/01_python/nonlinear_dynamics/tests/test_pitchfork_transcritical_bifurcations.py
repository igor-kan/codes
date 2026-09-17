"""Unit tests for 1D bifurcations."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pitchfork_transcritical_bifurcations import BifurcationNormalForms


class TestBifurcations(unittest.TestCase):
    def test_pitchfork(self):
        fp_sub = BifurcationNormalForms.supercritical_pitchfork_fixed_points(-1.0)
        self.assertEqual(len(fp_sub), 1)
        fp_super = BifurcationNormalForms.supercritical_pitchfork_fixed_points(4.0)
        self.assertEqual(len(fp_super), 3)
        self.assertTrue(2.0 in fp_super)


if __name__ == "__main__":
    unittest.main()
