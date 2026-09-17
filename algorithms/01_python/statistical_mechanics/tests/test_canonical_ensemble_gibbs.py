"""Unit tests for Canonical Ensemble."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from canonical_ensemble_gibbs import CanonicalEnsemble


class TestCanonicalEnsemble(unittest.TestCase):
    def test_two_level_system_heat_capacity(self):
        # Two-level system E = [0, 1] exhibits Schottky anomaly (peak in C_V)
        ce = CanonicalEnsemble(energy_levels=[0.0, 1.0], degeneracies=[1, 1], temperature=1.0)
        cv = ce.heat_capacity()
        self.assertGreater(cv, 0.0)


if __name__ == "__main__":
    unittest.main()
