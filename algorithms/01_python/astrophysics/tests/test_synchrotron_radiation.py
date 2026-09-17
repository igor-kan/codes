"""Unit tests for synchrotron radiation."""

import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from synchrotron_radiation import SynchrotronRadiation


class TestSynchrotron(unittest.TestCase):
    def test_power_positive(self):
        p = SynchrotronRadiation.total_emitted_power(gamma=1e3, magnetic_field_t=1e-4)
        nu_c = SynchrotronRadiation.critical_frequency(gamma=1e3, magnetic_field_t=1e-4)
        self.assertTrue(p > 0)
        self.assertTrue(nu_c > 0)


if __name__ == "__main__":
    unittest.main()
