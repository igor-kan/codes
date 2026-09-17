"""Unit tests for Grand Canonical Ensemble."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from grand_canonical_ensemble import GrandCanonicalEnsemble


class TestGrandCanonical(unittest.TestCase):
    def test_potential_sign(self):
        phi = GrandCanonicalEnsemble.grand_potential(temperature=2.0, grand_partition_func=10.0)
        self.assertLess(phi, 0.0)


if __name__ == "__main__":
    unittest.main()
