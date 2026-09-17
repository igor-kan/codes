"""Unit tests for Bianchi Identities."""

import unittest
import sys
import os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bianchi_identities import BianchiIdentities


class TestBianchiIdentities(unittest.TestCase):
    def test_algebraic_bianchi(self):
        r_zero = np.zeros((4, 4, 4, 4))
        self.assertTrue(BianchiIdentities.verify_algebraic_bianchi(r_zero))

    def test_contracted_bianchi(self):
        div_g = [1e-9, -2e-8, 0.0, 1e-10]
        self.assertTrue(BianchiIdentities.verify_contracted_bianchi(div_g))
        div_bad = [0.1, 0.0, 0.0, 0.0]
        self.assertFalse(BianchiIdentities.verify_contracted_bianchi(div_bad))


if __name__ == "__main__":
    unittest.main()
